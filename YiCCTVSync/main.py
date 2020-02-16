# Main file

from configparser import ConfigParser
import pathlib
import subprocess
from platform import system

from create_dirs import createDirectory
import globals

# Define the slash sign for os'es
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
globals.folderPath = globals.savePath + (globals.osSlash if globals.savePath[-1] != globals.osSlash else "") + str(configFile["DEFAULT"]["savefolder"])

# mkdir directories
createDirectory(globals.folderPath, globals.osSlash)


# Cleanup
del configFile