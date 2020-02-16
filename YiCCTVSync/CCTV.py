class CCTV:

    def __init__(self, name, hostName, folderName):
        self.__name = name
        self.__hostName = hostName
        self.__folderName = folderName

    def getName(self): return self.__name
    def getHostName(self): return self.__hostName
    def getFolderName(self): return self.__folderName