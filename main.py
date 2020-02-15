# Main file

from configparser import ConfigParser
import pathlib

# Create ConfigParser object to read conf file
configFile = ConfigParser()

# Read the conf file
path = str(pathlib.Path().absolute())
configFile.read( path + "\settings.conf" )

# Assign variables
updateInterval: int = int(configFile["DEFAULT"]["interval"])
