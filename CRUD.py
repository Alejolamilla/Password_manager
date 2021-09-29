import psycopg2

'''
postgres_credentials = creates a list with variables to connect to the bd easly (db name, db user, db password, host, port)
postgres_connect = conect to BD with the credentials (credentials)
new_user = Create a new user in users table (name, password)
delete_user = delete a user from users table (name, password)
new_password = save a new password for an specific user (userid, site, password, site_user)
delete_password = Delete a site's password for an specific user(userid, site, password)
show = returns a list with a specific site info or all sites passwords (site='', userid=1)
'''
# ================================================================================================================
def postgres_credentials(dbname="postgres", user='postgres', password='toor', host='127.0.0.1', port= '5432'):

    global credentials

    credentials = [dbname, user, password, host, port]
    return credentials

# ================================================================================================================
def postgres_connect(dbname1="postgres", user1='postgres', password1='toor', host1='127.0.0.1', port1= '5432'):

    global cursor, conn

    #establishing the connection
    conn = psycopg2.connect(
    dbname="password_manager", user='postgres', password='toor', host='127.0.0.1', port= '5432'
    )
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

# ================================================================================================================
def new_user(name, password, email):

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to add a new user
    sql = '''INSERT INTO users (name,password,email)
    VALUES ('{}', '{}', '{}');'''.format(name, password,email)

    #Adding new user
    try:
        cursor.execute(sql)
        message = 'success'

    except psycopg2.errors.UniqueViolation:
        message = 'duplicate error'

    #Closing the connection
    conn.close()
    cursor.close()
    return message

# ================================================================================================================
def delete_user(name, password):

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to delete a user
    sql = '''DELETE FROM users WHERE name = '{}';'''.format(name)

    #Preparing query to verify a user password
    sql_verification = '''SELECT password FROM users WHERE name='{}';'''.format(name)

    #Make password readeable
    cursor.execute(sql_verification)
    password_verification = cursor.fetchone()

    #Verify user identity
    if password == password_verification[0]:
        cursor.execute(sql)
        message = 'success'
    else: message = 'password not match'

    #Close conections
    conn.close()
    cursor.close()

    return message

# ================================================================================================================
def new_password(userid, site, password, site_user):

    id = userid + site

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to add new password
    sql = '''INSERT INTO passwords (id, userID, site, password, site_user)
            VALUES ('{}', '{}', '{}', '{}', '{}')'''.format(id, userid, site, password, site_user)

    #Adding new user
    try:
        cursor.execute(sql)
        message = 'success'

    except psycopg2.errors.UniqueViolation:
        message = 'duplicate error'

    #Closing the connection
    conn.close()
    cursor.close()
    return message

# ================================================================================================================
def delete_password(userid, site, password):

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to delete a user
    sql = '''DELETE FROM passwords
             WHERE site = '{}'
             AND userid = '{}';'''.format(site, userid)

    #Verificates site existence
    sql_site_verification = '''SELECT site FROM passwords
                        WHERE site = '{}'
                        AND userid = '{}';'''.format(site, userid)
    cursor.execute(sql_site_verification)
    site_verification = cursor.fetchone()
    print(site_verification[0])

    if str(site_verification) == 'None': message = 'unexistent site'

    else:

        #Preparing query to verify a user password
        sql_verification = '''SELECT password FROM users WHERE userid='{}';'''.format(userid)

        #Make password readeable
        cursor.execute(sql_verification)
        password_verification = cursor.fetchone()

        #Verify user identity
        try:
            if password == password_verification[0]:
                cursor.execute(sql)
                message = 'success'
            else: message = 'password not match'

        except TypeError: message = 'unexistent user'

    #Close conections
    conn.close()
    cursor.close()

    return message
# ================================================================================================================
def show(site='', userid=1):

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to call one or all passwords
    if site == '':
        sql = '''SELECT * FROM passwords WHERE userid='{}';'''.format(userid)
    else:
        sql = '''SELECT * FROM passwords
                WHERE userid='{}'
                AND site= '{}';'''.format(userid, site)

    #Make password readeable
    cursor.execute(sql)
    data = cursor.fetchall()

    #Close conections
    conn.close()
    cursor.close()

    return data
# ================================================================================================================
def user_verification(user, password):

    #Connecting to BD
    postgres_connect(credentials)

    sql = '''SELECT * FROM users
            WHERE name ='{}' OR email='{}' '''.format(user,user)

    #Make data readeable
    cursor.execute(sql)
    data = cursor.fetchall()

    #Close conections
    conn.close()
    cursor.close()

    if data == []:
        return 'unexistent'
    else:
        if data[0][2] == password:
            return 'success'
        else: return 'unmatch_password'


# =============================================JUST FOR PROBES===================================================
if __name__ == '__main__':
    credentials = postgres_credentials(dbname="password_manager", user='postgres', password='toor', host='127.0.0.1', port= '5432')
    # print (new_user('alphale', 'alphapassword', 'alpha@htomail.com'))
    # print(delete_password('13', 'Facebook', 'mypassword'))
    # print(new_password('11', 'whatsapp', 'mywapppassword',''))
    # print (show('Instagram',11))
    print(user_verification('alpha@htomail.com', 'alphapassword'))