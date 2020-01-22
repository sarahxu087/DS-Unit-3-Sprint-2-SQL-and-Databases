import pandas as pd
import sqlite3
import psycopg2
dbname ='jvwuxmwx'
user ='jvwuxmwx'
password = 	'YlamMuYszdQMmaD92Gtg4Ok40Xkfhgmf'
host = 'rajje.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,password=password, host=host)
dir(pg_conn)
pg_curs = pg_conn.cursor()

df = pd.read_csv('titanic.csv')
df['Name']= df['Name'].replace("Miss. Ellen O'Dwyer","Miss. Ellen ODwyer")
df['Name']= df['Name'].replace("Miss. Bridget O'Driscoll","Miss. Bridget ODriscoll")
df['Name']= df['Name'].replace("Mrs. Thomas (Johanna Godfrey) O'Brien","Mrs. Thomas (Johanna Godfrey) OBrien")
df['Name']= df['Name'].replace("Mr. Thomas O'Brien","Mr. Thomas OBrien")
df['Name']= df['Name'].replace("Mr. Maurice O'Connor","Mr. Maurice OConnor")
df['Name']= df['Name'].replace("Miss. Bridget Mary O'Sullivan","Miss. Bridget Mary OSullivan")
df['Name']= df['Name'].replace("Mr. Timothy O'Brien","Mr. Timothy OBrien")
df['Name']= df['Name'].replace("Mr. Patrick D O'Connell","Mr. Patrick D OConnell")
df['Name']= df['Name'].replace("Miss. Hanora O'Leary","Miss. Hanora OLeary")

print(df.shape)
df_conn=sqlite3.connect('titanic.sqlite3')
df_curs = df_conn.cursor()
df.to_sql('titanic',df_conn,if_exists='replace')
titanic=df_curs.execute('SELECT * FROM titanic').fetchall()
print(df_curs.execute('PRAGMA table_info(titanic);').fetchall())
create_titanic_table ="""
CREATE TABLE IF NOT EXISTS Titanic(
    index INT,
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex Text,
    Age REAL,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare REAL



);


"""
pg_curs.execute(create_titanic_table)
pg_conn.commit()
show_tables = """
SELECT
   *
FROM
   pg_catalog.pg_tables
WHERE
   schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
pg_curs.fetchall()

for x in titanic:
  insert_x = """
    INSERT INTO Titanic
    (Survived, Pclass, Name, Sex,Age, Siblings_Spouses_Aboard,  Parents_Children_Aboard, Fare)
    VALUES """ + str(x[1:]) + ";"
  pg_curs.execute(insert_x)

  pg_curs.execute('SELECT * FROM Titanic')
  pg_x=pg_curs.fetchall()
  pg_conn.commit()
  
  
  
  
