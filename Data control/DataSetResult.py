import pymysql


class DataSetResult (object):


    def __init__(self, dataBaseAccess, sqlQuery):
        dataSet = ''
        self.setDataBaseAcces(dataBaseAccess)
        self.setSqlQuery(sqlQuery)
        self.setDataSet(dataBaseAccess, dataSet)

    def setDataBaseAcces(self, dataBaseAccess):
        self.dataBaseAccess = dataBaseAccess


    def setSqlQuery(self, sqlQuery):
        self.sqlQuery = sqlQuery

    def setDataSet(self, dataBaseAccess, dataSet):
        self.dataSet = dataBaseAccess.getConnectionCursor()

    def getDataSet(self):
        return self.dataSet

    def getDataBaseAccess(self):
        return self.dataBaseAccess

    def getSqlQuery(self):
        return self.sqlQuery

    def executeSql(self):
        return self.dataSet.execute(self.sqlQuery)

    def getAllRows(self):
        return self.dataSet.fetchall()