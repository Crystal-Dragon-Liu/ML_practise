import pymysql
def open_connect():

  mysql_host = 'the_second_house'
  mysql_name = 'localhost'
  mysql_user = 'root'
  mysql_port = 3306
  mysql_password = '1025058706zfr'
  dbconn = pymysql.connect(mysql_name, mysql_user, mysql_password, mysql_host, charset='utf8')
  #cursor = dbconn.cursor()
  return dbconn

def close_connect(dbconn):
  dbconn.close()



