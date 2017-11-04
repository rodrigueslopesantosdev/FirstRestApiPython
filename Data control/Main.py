from DataBaseConnection import DataBaseConnection
from DataSetResult import DataSetResult
import pymysql.cursors

'''
connection = pymysql.connect(host="rdstiagoaws.cteqiyblhicy.us-east-2.rds.amazonaws.com",
                                          port=3306,
                                     user="pythonTest",
                                     password="pythonTest2017",
                                     db="Vehicles",
                                     cursorclass=pymysql.cursors.DictCursor)

cursor  = connection.cursor()

cursor.execute("SELECT * FROM CARS")

results = cursor.fetchall()

print (str(results['Model']))
'''

connection = DataBaseConnection("rdstiagoaws.cteqiyblhicy.us-east-2.rds.amazonaws.com",
                           "pythonTest", "pythonTest2017", "Vehicles", 3306)



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

