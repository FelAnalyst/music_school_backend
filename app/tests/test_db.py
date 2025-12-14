from app.db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * from teachers")
print(cur.fetchall())

cur.close()
conn.close()
