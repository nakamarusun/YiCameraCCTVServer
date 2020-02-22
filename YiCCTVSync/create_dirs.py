import subprocess
import globals
import exceptions
from os import path

def createDirectory(dir: str):

    if not path.exists(dir):

        # Repeatedly creates folder, if the first folder does not exist, then creates it
        dirList = dir.split(globals.osSlash)
        mkdirCount = 0

        if globals.osSlash == "/": # Linux / Unix

            # Not on root dir
            root = False
            if dir[0] == "/":
                root = True
                dirList.pop(0)

            if globals.verbose:
                print("\n createDirectory")
                print("Operating system: Linux / Unix")
                print("Creating directory in", dir)

            for num in range(len(dirList)):
                currentDir = ("/" if root else "") + "/".join(dirList[:(num + 1)])

                if not path.exists(currentDir):
                    makeDir = subprocess.Popen(["mkdir", currentDir],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
                    out, err = makeDir.communicate()
                    mkdirCount += 1
                    if len(str(err)) > 5:
                        raise exceptions.ErrorMkdir("Error creating save directory. Please use sudo (Administrative rights).")
                    if globals.verbose: print("directory", currentDir, "initialized !")
                else:
                    if globals.verbose: print("directory", currentDir, "already exist.")

            if globals.verbose: print(mkdirCount, "Directories initialized.")
    
    else:
        if globals.verbose: print("Directory", dir, "already exist.")