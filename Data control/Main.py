from DataBaseConnection import DataBaseConnection
from DataSetResult import DataSetResult
import pymysql.cursors


connection = DataBaseConnection("<hostname>",
                           "<user>", "<password>", "<database>", <port_number>)



print ("HostName: " + str(connection.getHostName()))
print ("User name: " + str(connection.getUserName()))
print ("Password: " + str(connection.getPassWord()))

sqlQuery = "SELECT * FROM CARS"

#dataSet is cursor
result = DataSetResult(connection, sqlQuery)
print ("Query: " + str(result.getSqlQuery()))

result.executeSql()
table = result.getAllRows()

print (table)

connection.closeConnection()

