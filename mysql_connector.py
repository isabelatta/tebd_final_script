# Conexão banco de dados
import mysql.connector
from mysql.connector import Error

class MysqlConnector(object):
    def __init__(self, host='localhost', user='root', password='', database=''):
      try:
        cnx = mysql.connector.connect(host=host,
                                      database=database,
                                      user=user,
                                      password=password,
                                      auth_plugin='mysql_native_password')
        self.__connection = cnx
        self.__session    = cnx.cursor()
      except Error as e:
        print("Error while connecting to MySQL", e)
    ## End def __init___

    def __close(self):
      self.__session.close()
      self.__connection.close()
    ## End def __close

    def check_connection(self):
      db_Info = self.__connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      cursor = self.__session
      cursor.execute("select database();")
      record = cursor.fetchone()
      print("You're connected to database: ", record)
    ## End def check_connection

    def insert(self, table, *args, **kwargs):
      values = None
      query = "INSERT INTO %s " % table
      if kwargs:
          keys = kwargs.keys()
          values = tuple(kwargs.values())
          query += "(" + ",".join(["`%s`"] * len(keys)) %  tuple (keys) + ") VALUES (" + ",".join(["%s"]*len(values)) + ")"
      elif args:
          values = args
          query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"
      self.__session.execute(query, values)
      self.__connection.commit()
      return self.__session.lastrowid
    ## End def insert
## End class