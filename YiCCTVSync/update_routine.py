from ftplib import FTP
from globals import cctvs, verbose, osSlash
from CCTV import CCTV
from time import time

from os import listdir
import string
from create_dirs import createDirectory

def getFolderDetail(cameraList) -> str:
    try:
        alphabet = string.ascii_letters
        timeRange = [cameraList[0], cameraList[-1]]
        for time in range(len(timeRange)):
            for let in range(len(timeRange[time])):
                if timeRange[time][let] in string.ascii_letters:
                    timeRange[time].replace(timeRange[time][let], " ")
            timeRange[time] += " Hour"
        
    except IndexError:
        timeRange = ["EMPTY", "EMPTY"]

    return "{} \n recorded {} Folders(hours), from {} to {}".format(cameraList, len(cameraList), timeRange[0], timeRange[-1])


def updateRoutine():

    startTime = time()

    for cams in cctvs:
        # Just for Convenience
        cams: CCTV

        name = cams.getName()
        ftp = FTP(cams.getHostName())

        cctvDir = "/tmp/sd/record"

        if verbose: print("\n\n[ Starting session with {name} ]\n".format(name=name))
        if verbose: print("{name}: {ftpmsg}".format( name=name, ftpmsg=ftp.login(user=cams.getLogin(), passwd=cams.getPasswd()) ))
        if verbose: print("{name}: {ftpmsg}".format( name=name, ftpmsg=ftp.cwd(cctvDir)))

        # Folders dictionary format:
        # ******Folders:dict = {folderDirectory: [files]}
        # Check server's folder for files list

        if verbose: print("\n{name}: Listing all file from server..".format(name=name))
        camServerFolders: dict = {}

        # For folders in the directory of camera (ex. 2020Y02M19D13H')
        for fold in sorted(listdir(cams.getFolderName())):
            camServerFolders[fold] = listdir(cams.getFolderName() + osSlash + fold)

        if verbose: print(getFolderDetail( list(camServerFolders.keys() )))

        # Check camera's folder for files list

        if verbose: print("\n{name}: Listing all files from camera..".format(name=name))

        camCCTVFolders: dict = {}
        for fold in sorted(filter(lambda fold : fold != "tmp.mp4.tmp" , ftp.nlst( cctvDir ) )):
            camCCTVFolders[fold] = ftp.nlst(cctvDir + "/" + fold)

        if verbose: print(getFolderDetail( list(camCCTVFolders.keys() )))

        # Download whats not on the server's file list


        if verbose: print("\n{name}: Searching for file differences...".format(name=name))
        fileDiffs: list = []

        for camDir in camCCTVFolders:
            # Current server directory camera (ex. foldername/2020Y02M19D13H)
            currentServerDir = cams.getFolderName() + osSlash + camDir
            # If camera directory is not already initialized in server, make it.
            if camDir not in list( camServerFolders.keys() ): createDirectory( currentServerDir )

            # Checks for files in the directory
            for camFile in camCCTVFolders[camDir]:
                if camFile not in currentServerDir:
                    fileDiffs.append( cctvDir + "/" + camDir + "/" + camFile )

        if verbose: print("\n{name}: The difference in files are:\n".format(name=name), fileDiffs)
        if verbose: print("{name}: Operation complete.".format(name=name))