from ftplib import FTP
from globals import cctvs, verbose, osSlash
from CCTV import CCTV
from time import time

from os import listdir
import string

def getFolderDetail(cameraList) -> str:
    try:
        alphabet = string.ascii_letters
        timeRange = [cameraList[0], cameraList[-1]]
        for time in len(range(timeRange)):
            for let in len(range(timeRange[time])):
                if timeRange[time][let] in string.ascii_letters:
                    timeRange[time][let] = "-"
            timeRange[time] += " Hour"
        
    except IndexError:
        timeRange = ["EMPTY", "EMPTY"]

    return "{dirList} \n recorded {dirLen} Folders(hours), from {early} to {latest}".format(cameraList, len(cameraList), timeRange[0], timeRange[-1])


def updateRoutine():

    startTime = time()

    for cams in cctvs:
        # Just for Convenience
        cams: CCTV

        name = cams.getName()
        ftp = FTP(cams.getHostname())

        cctvDir = "/tmp/sd/record"

        if verbose: print("\n\n[ Starting session with {name} \n]".format(name))
        if verbose: print("{name}: {ftpmsg}".format( name, ftp.login(user=cams.getLogin, passwd=cams.getPasswd) ))
        if verbose: print("{name}: {ftpmsg}".format( name, ftp.cwd(cctvDir)))

        # Check server's folder for files list

        if verbose: print("\n{name} Listing all file from server..".format(name))
        camServerFolders: dict = {}
        for fold in listdir(cams.getFolderName).sort():
            camServerFolders[fold] = listdir(cams.getFolderName + osSlash + fold)

        if verbose: print(getFolderDetail(list(camServerFolders.keys())))


        # Check camera's folder for files list

        if verbose: print("\n{name} Listing all file from camera..".format(name))

        camCCTVFolders: dict = {}
        for fold in filter(lambda fold : fold != "tmp.mp4.tmp" , ftp.nlst('/tmp/sd/record') ).sort():
            camCCTVFolders[fold] = ftp.nlst(cctvDir + "/" + fold)

        if verbose: print(getFolderDetail(list(camCCTVFolders.keys())))

        # Download whats not on the server's file list

        if verbose: print("\n Searching for file difference...")
        fileDiffs: list = []