import mysql.connector



def get_connection():
  config = {
        'user': 'root',
        'password': 'helloworld01',
        'host': 'db',
        'port': '3306',
        'database': 'grpc',
        'auth_plugin': 'mysql_native_password'
    }
  return mysql.connector.connect(**config)

def select_user_by_user_id(conn, id, password):

    cursor = conn.cursor(buffered=True)

    query = ("SELECT u.user_id, u.user_name FROM user AS u WHERE user_id = %s AND password = %s")

    cursor.execute(query, (id, password))

    name = ''
    for (user_id, user_name) in cursor:
        name = user_name


    cursor.close()

    return name

def select_all_user(conn):

    cursor = conn.cursor(buffered=True)

    query = ("SELECT u.user_id, u.user_name FROM user AS u")

    cursor.execute(query)

    list = []
    for (user_id, user_name) in cursor:
        list.insert(user_id, user_name)
    cursor.close()

    return list

def create_user(conn, user_id, user_name, password):

    cursor = conn.cursor(buffered=True)
    # user_id = user.get["user_id"]
    # user_name = user.get["user_name"]
    # password = user.get["password"]
    # password_confirm = user.get["password_confirm"]

    insert_user = (
        "INSERT INTO user (user_id, user_name, password)"
        "VALUES (%s, %s, %s)")

    cursor.execute(insert_user, (user_id, user_name, password))

    conn.commit()
    cursor.close()




