import psycopg2
from config import DATABASE


conn = psycopg2.connect(**DATABASE)
with conn.cursor() as cursor:
    cursor.execute("SET lc_monetary TO 'en_US.UTF-8';")
    cursor.execute("SELECT 1000.0::money")
    print(cursor.fetchall())
conn.close()