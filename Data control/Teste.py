

def  MostPopularNumber (list):
    table = {}

    for x in range(len(list)):
        table[list[x]] = list.count(list[x])

    tableSorted = sorted(table, key=table.get)
    return tableSorted

a = [1,2,2,3]

x = MostPopularNumber(a)

print (x)


SELECT
    dateformat(ps.date_time) as Date,
    usr.Name as User_name,
    count(ps.idUser) as Number_logins
from
    Users usr inner join Logins_system ps
    on usr.idUser = ps.idUser
