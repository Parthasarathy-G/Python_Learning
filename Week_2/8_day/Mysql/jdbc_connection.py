import pymysql

connection = pymysql.connect( host='localhost', 
                             user = 'root', 
                             password = 'root', 
                             database = 'test', 
                             cursorclass=pymysql.cursors.DictCursor)

