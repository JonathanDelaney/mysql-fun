import os
import pymysql


username = ''


connection = pymysql.connect(host="localhost",
                            user = username,
                            password= '',
                            db = 'Chinook')

try:
    #Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection to sql
    connection.close()