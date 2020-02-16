import subprocess

def createDirectory(dir: str, osSlash: str):
    testDir = subprocess.Popen(['test', '-d', dir, '&&', 'echo', 'true', '||', 'echo', 'false'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    out, err = testDir.communicate()