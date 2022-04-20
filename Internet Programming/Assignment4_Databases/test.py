import sqlite3

conn = sqlite3.connect('sqlite-sakila.sq')

try:
    c = conn.cursor()
    sql = "select * from payment where amount > 11"
    c.execute(sql)
    data = c.fetchall()
    result = len(data)
    print(result)
    print(type(data))
except:
    print('Error')
finally:
    conn.close()
