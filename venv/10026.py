import psycopg2
import psycopg2.extras

conn = psycopg2.connect(host = '127.0.0.1', port = 5432, database = 'test', user = 'postgres', password = 'admin')
cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
#cur.execute("insert into clients(name, lastname) values ('Vasya', 'Pupkin')")
cur.execute("select * from clients")
for row in cur:
    print(str(row['id']) + ' ' + row['name'] + ' ' + row['lastname'])
#conn.commit()
conn.close()
