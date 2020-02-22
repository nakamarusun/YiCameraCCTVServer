class CCTV:

    def __init__(self, name, hostName, folderName, login, passwd):
        self.__name = name
        self.__hostName = hostName
        self.__folderName = folderName
        self.__login = login
        self.__passwd = passwd

    def getName(self): return self.__name
    def getHostName(self): return self.__hostName
    def getFolderName(self): return self.__folderName
    def getLogin(self): return self.__login
    def getPasswd(self): return self.__passwd