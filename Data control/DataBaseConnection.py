import pymysql.cursors


class DataBaseConnection (object):

    def __init__(self, hostName, userName, passWord, dbName, portNumber):
        self.setHostName(hostName)
        self.setUserName(userName)
        self.setPassWord(userName)
        self.setDbName(dbName)
        self.setPortNumber(portNumber)
        self.setConnection(hostName, userName, passWord, dbName, portNumber)


    def setHostName(self, hostName):
        self.hostName = hostName

    def setUserName (self, userName):
        self.userName = userName

    def setPassWord (self, passWord):
        self.passWord = passWord

    def setDbName (self, dbName):
        self.dbName = dbName

    def setPortNumber(self, portNumber):
        self.portNumber = portNumber

    def setConnection(self, hostName, userName, passWord, dbName, portNumber):
        self.connection = pymysql.connect(host=hostName,
                                          port=portNumber,
                                     user=userName,
                                     password=passWord,
                                     db=dbName,
                                     cursorclass=pymysql.cursors.DictCursor)

    def getConnectionCursor(self) :
        return self.connection.cursor()

    def getHostName(self):
        return self.hostName

    def getUserName(self):
        return self.userName

    def getPassWord(self):
        return self.passWord

    def getDbName(self):
        return self.dbName

    def getPortNumber(self):
        return self.portNumber

    def closeConnection(self):
        self.connection.close()
