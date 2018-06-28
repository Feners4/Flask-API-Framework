import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='Tulipanes5',
                             db='clients',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
def addUser(Fname,Lname):
    try:
        cursorObject = connection.cursor()
        cursorObject.execute("call sp_createUser('{}'".format(Fname)+",'{}')".format(Lname))
        connection.commit()
        connection.close()

    finally:
        return 'User data added succesfully!'