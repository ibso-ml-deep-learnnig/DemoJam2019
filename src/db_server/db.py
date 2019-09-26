import mysql.connector
from mysql.connector import Error
from logger import getJSONLogger

def get_connection(url, port):
  config = {
        'user': 'root',
        'password': 'helloworld01',
        'host': url,
        'port': port,
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

def selectAssetById(conn, asset_id):

    logger = getJSONLogger('account-server')
    logger.info("select asset by id: " +asset_id)

    asset = None

    try:
      cursor = conn.cursor(buffered=True)

      query = ("SELECT * FROM asset where asset_id = %s")

      count = cursor.execute(query, (asset_id))
      if count != 0:
          asset = cursor.fetchone()

    except Error as error:
        print("Failed to select asset from table {}".format(error))
        logger.info("Failed to select asset from table {}".format(error))

    finally:
        if (conn.is_connected()):
          cursor.close()

    return asset

def selectAssets(conn, user_id):

    logger = getJSONLogger('account-server')
    logger.info("select assets by id: " +user_id)

    assetList = None

    try:
        cursor = conn.cursor(buffered=True)

        if user_id == 'admin':
            query = ("SELECT * FROM asset")
            count = cursor.execute(query)
        else:
            query = ("SELECT * FROM asset where user_id = %s")
            count = cursor.execute(query, [user_id])

        if count != 0:
            assetList = cursor.fetchall()

    except Error as error:
        logger.info("Failed to select asset from table {}".format(error))
        print("Failed to select asset from table {}".format(error))

    finally:
        if (conn.is_connected()):
          cursor.close()

    return assetList

def insertAsset(conn, asset):

    logger = getJSONLogger('account-server')
    logger.info("insert asset " +str(asset))

    e = False

    try:
        cursor = conn.cursor(buffered=True)

        insert_asset = (
            "INSERT INTO asset "
            "(asset_id, asset_class, description, picture, company_code, asset_number, asset_subno, cost_center, acquisition_date, amount, ul_year, ul_period, user_id, create_date, create_time)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        cursor.execute(insert_asset, asset)

        conn.commit()

    except Error as error:
        conn.rollback()
        logger.info("FFailed to insert asset into table {}".format(error))
        print("Failed to insert asset into table {}".format(error))
        e = True

    finally:
        if (conn.is_connected()):
            cursor.close()

    return e
