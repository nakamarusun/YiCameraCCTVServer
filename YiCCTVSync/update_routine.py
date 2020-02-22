from ftplib import FTP
from globals import cctvs, verbose
from CCTV import CCTV
from time import time

def updateRoutine():

    startTime = time()

    for cams in cctvs:
        # Just for Convenience
        cams: CCTV

        name = cams.getName()
        ftp = FTP(cams.getHostname())

        if verbose: print("\n\n[ Starting session with {name} \n]".format(name))
        if verbose: print("{name}: {ftpmsg}".format( name, ftp.login(user=cams.getLogin, passwd=cams.getPasswd) ))
        if verbose: print("{name}: {ftpmsg}".format( name, ftp.cwd("/tmp/sd/record")))

        # Check server's folder for files list

        if verbose: print("Listing all file from server..")
        

        # Check camera's folder for files list

        # Download whats not on the server's file list