# Main file

from configparser import ConfigParser
import pathlib
import subprocess
from platform import system

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

test = subprocess.Popen(['test', '-d', folderPath, '&&', 'echo', 'true', '||', 'echo', 'false'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
out, err = test.communicate()
if out == 'true':
    pass
    # Don't create new directory
else:
    pass
    # Create directory recursively


# Cleanup
del savePath
del configFile