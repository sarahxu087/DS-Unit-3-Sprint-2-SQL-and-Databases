import pandas as pd
import sqlite3
import psycopg2
dbname ='jvwuxmwx'
user ='jvwuxmwx'
password = 	'AV8n6NcALgMpvL4gWlO6nTrYm-7bt9ap'
host = 'rajje.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,password=password, host=host)
dir(pg_conn)
pg_curs = pg_conn.cursor()

df = pd.read_csv('titanic.csv')
print(df.shape)
df_conn=sqlite3.connect('titanic.sqlite3')
df_curs = df_conn.cursor()
titanic=df_curs.execute('SELECT * FROM titanic').fetchall()
print(df_curs.execute('PRAGMA table_info(titanic);').fetchall())