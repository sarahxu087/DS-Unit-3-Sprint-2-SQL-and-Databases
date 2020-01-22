import pandas as pd
import sqlite3
df = pd.read_csv('/Users/huanqingxu/Desktop/repos/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv')
print(df.shape)
conn=sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()
df.to_sql('review',conn,if_exists='replace')
review=curs.execute("SELECT * FROM review").fetchall()
print(curs.execute('PRAGMA table_info(review);').fetchall())
#print(review)

curs1 = conn.cursor()
query = """SELECT COUNT(*)
        FROM review ;"""
curs1.execute(query)
rows = curs1.fetchall()
#print(rows)

curs2 = conn.cursor()
query = """SELECT COUNT(*)
        FROM review
        WHERE Nature >= 100 
        AND Shopping >= 100;"""
curs2.execute(query)
users_reviewed = curs2.fetchall()
print(rows)