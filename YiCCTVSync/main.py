# Main file

from configparser import ConfigParser
import pathlib
import subprocess
from platform import system

from create_dirs import createDirectory

# Define the slash sign for os'es
if system == "Windows":
    osSlash = "\"
else:
    osSlash = "/"



# Create ConfigParser object to read conf file
configFile = ConfigParser()

# Read the conf file
path: str = str(pathlib.Path().absolute())
configFile.read( path + osSlash + "settings.conf" )


# Assign variables
savePath: str = str(configFile["DEFAULT"]["savepath"])

updateInterval: int = int(configFile["DEFAULT"]["interval"])
folderPath: str = savePath + (osSlash if savePath[-1] != osSlash else "") + str(configFile["DEFAULT"]["savefolder"])

# mkdir directories
createDirectory(folderPath)


# Cleanup
del savePath
del configFile