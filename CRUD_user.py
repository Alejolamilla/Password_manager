import psycopg2

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
def new_user(name, password):

    #Connecting to BD
    postgres_connect(credentials)

    #Preparing query to add a new user
    sql = '''INSERT INTO users (name,password)
    VALUES ('{}', '{}');'''.format(name, password)

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

    sql_verification = '''SELECT password FROM users WHERE name='{}';'''.format(name)

    cursor.execute(sql_verification)
    password_verification = cursor.fetchone()

    if password == password_verification[0]:
        cursor.execute(sql)
        message = 'success'
    else: message = 'password not match'

    conn.close()
    cursor.close()

    return message

# =============================================JUST FOR PROBES===================================================
# if __name__ == '__main__':
#     credentials = postgres_credentials(dbname="password_manager", user='postgres', password='toor', host='127.0.0.1', port= '5432')
#     print(delete_user('Alphalejo', 'mypassword')) 