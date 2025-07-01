import psycopg2

conn = psycopg2.connect(
    dbname="base",
    user="postgres",
    password="20062007",
    host="localhost"
)
cur = conn.cursor()
cur.execute("SELECT * FROM users2;")
a = cur.fetchall()
print(a)

cur.close()
conn.close()
