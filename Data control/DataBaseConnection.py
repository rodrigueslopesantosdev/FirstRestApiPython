import pymysql.cursors


class DataBaseConnection (object):

    def __init__(self, hostName, userName, passWord, dbName):
        self.setHostName(hostName)
        self.setUserName(userName)
        self.setPassWord(userName)
        self.setDbName(dbName)
        self.setConnection(hostName, userName, passWord, dbName)


    def setHostName(self, hostName):
        self.hostName = hostName

    def setUserName (self, userName):
        self.userName = userName

    def setPassWord (self, passWord):
        self.passWord = passWord

    def setDbName (self, dbName):
        self.dbName = dbName


    def setConnection(self, hostName, userName, passWord, dbName):
        connection = pymysql.connect(host=hostName,
                                     user=userName,
                                     password=passWord,
                                     db=dbName)
        # cursorclass = pymysql.cursors.DictCursor)

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

    def closeConnection(self):
        self.connection.close()
