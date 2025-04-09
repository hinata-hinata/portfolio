import MySQLdb

def get_connection():
      connection = MySQLdb.connect(user='root', 
                                 password='hinata0703',
                                 host='localhost',
                                 database='spell_game')
      return connection

def insert_spell(spell, mean):
  connection = get_connection()
  cursor = connection.cursor()
  
  sql = 'INSERT INTO spells (spell, mean) VALUES(%s, %s)'
  
  cursor.execute(sql, (spell, mean))
  connection.commit()
  
  cursor.close()
  connection.close()