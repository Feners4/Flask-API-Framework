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

def addPassword(Username,Userpassword):
    try:
        cursorObject = connection.cursor()
        cursorObject.execute("call sp_createPassword('{}'".format(Username)+",'{}')".format(Userpassword))
        connection.commit()
        connection.close()

    finally:
        return 'User added succesfully!'

def getLoginUser(username):
    try:
        cursorObject = connection.cursor()
        #username = request.form['username']
        cursorObject.execute("SELECT * FROM tbl_passwords WHERE user_name =%s", [username])
        data = cursorObject.fetchone()
        password = data['user_password']
        db_username = data['user_name']

    finally:
        return password,db_username