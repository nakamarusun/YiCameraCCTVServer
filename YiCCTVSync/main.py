# Main file

from configparser import ConfigParser
import pathlib
import subprocess
from platform import system
import os

from create_dirs import createDirectory
import globals
import exceptions
from CCTV import CCTV


if system == "Windows":
    globals.osSlash = "\\"
else:
    globals.osSlash = "/"

# Create ConfigParser object to read conf file
configFile = ConfigParser()

# Read the conf file
path: str = str(pathlib.Path().absolute())
configFile.read( path + globals.osSlash + "settings.conf" )


# Assign globals
globals.savePath = str(configFile["DEFAULT"]["savepath"])
globals.updateInterval = int(configFile["DEFAULT"]["interval"])
globals.verbose = True if configFile["DEFAULT"]["verbose"] == "1" else False
if globals.savePath == "":
    globals.folderPath = str(configFile["DEFAULT"]["savefolder"])
else:
    globals.folderPath = globals.savePath + (globals.osSlash if globals.savePath[-1] != globals.osSlash else "") + str(configFile["DEFAULT"]["savefolder"])
cctvSections = configFile.sections()
for camera in cctvSections:
    globals.cctvs.append( CCTV(camera,
                        configFile.get(camera, "hostname"),
                        configFile.get(camera, "folder")) )

# Cleanup
del configFile

# mkdir directories
if globals.verbose: print("Creating save directory..")
createDirectory(globals.folderPath)


# Initialize cctv directories
if globals.verbose: print("Creating CCTV Directories..")