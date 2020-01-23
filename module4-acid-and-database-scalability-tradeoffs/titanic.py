import pandas as pd
import psycopg2
dbname ='jvwuxmwx'
user ='jvwuxmwx'
password = 	'YlamMuYszdQMmaD92Gtg4Ok40Xkfhgmf'
host = 'rajje.db.elephantsql.com'
pg_conn = psycopg2.connect(dbname=dbname, user=user,password=password, host=host)
dir(pg_conn)
pg_curs = pg_conn.cursor()
query="""
    SELECT COUNT(*) Survived
    FROM titanic
    WHERE Survived = 1
"""
pg_curs.execute(query)
survived = pg_curs.fetchall()
print(survived)
pg_curs1 = pg_conn.cursor()
query="""
    SELECT COUNT(*) Survived
    FROM titanic
    WHERE Survived = 0
"""
pg_curs1.execute(query)
notSurvived = pg_curs1.fetchall()
print(notSurvived)
pg_curs2 = pg_conn.cursor()
query="""
    SELECT COUNT(*)Pclass
    FROM titanic
    GROUP BY Pclass
"""
pg_curs2.execute(query)
peopleClass = pg_curs2.fetchall()
print(peopleClass)

pg_curs3 = pg_conn.cursor()
query="""
    SELECT COUNT(*)Pclass
    FROM titanic
    WHERE Survived = 1
    GROUP BY Pclass
"""
pg_curs3.execute(query)
peopleClassSurvived= pg_curs3.fetchall()
print(peopleClassSurvived)
pg_curs4 = pg_conn.cursor()
query="""
    SELECT COUNT(*)Pclass
    FROM titanic
    WHERE Survived = 0
    GROUP BY Pclass
"""
pg_curs4.execute(query)
peopleClassNoSurvived= pg_curs4.fetchall()
print(peopleClassNoSurvived)
pg_curs5 = pg_conn.cursor()
query="""
    SELECT ROUND(AVG(age)) age
     FROM titanic
    WHERE Survived = 0
"""
pg_curs5.execute(query)
noSurvivedAge= pg_curs5.fetchall()
print(noSurvivedAge)
pg_curs6 = pg_conn.cursor()
query="""
    SELECT ROUND(AVG(age)) age
     FROM titanic
    WHERE Survived = 1
"""
pg_curs6.execute(query)
survivedAge= pg_curs6.fetchall()
print(survivedAge)
pg_curs7 = pg_conn.cursor()
query="""
    SELECT Pclass,ROUND(AVG(age)) age
     FROM titanic
    GROUP BY Pclass
"""
pg_curs7.execute(query)
avgAge= pg_curs7.fetchall()
print(avgAge)

pg_curs8 = pg_conn.cursor()
query="""
    SELECT Pclass,ROUND(AVG(Fare)) Fare
     FROM titanic
    GROUP BY Pclass
"""
pg_curs8.execute(query)
fareClass= pg_curs8.fetchall()
print(fareClass)
pg_curs9= pg_conn.cursor()
query="""
    SELECT Survived,ROUND(AVG(Fare)) Fare
     FROM titanic
    GROUP BY Survived
"""
pg_curs9.execute(query)
sFare= pg_curs9.fetchall()
print(sFare)
pg_curs10= pg_conn.cursor()
query="""
    SELECT Pclass,AVG(Siblings_Spouses_Aboard)Siblings_Spouses_Aboard
    FROM titanic

    GROUP BY Pclass
    ORDER BY Pclass
"""
pg_curs10.execute(query)
ssaClass= pg_curs10.fetchall()
print(ssaClass)
pg_curs11= pg_conn.cursor()
query="""
    SELECT Survived,AVG(Siblings_Spouses_Aboard)Siblings_Spouses_Aboard
    FROM titanic

    GROUP BY Survived
    
"""
pg_curs11.execute(query)
ssaS= pg_curs11.fetchall()
print(ssaS)
pg_curs12= pg_conn.cursor()
query="""
    SELECT Pclass,AVG(Parents_Children_Aboard)Parents_Children_Aboard
    FROM titanic

    GROUP BY Pclass
    ORDER BY Pclass
"""
pg_curs12.execute(query)
pcaClass= pg_curs12.fetchall()
print(pcaClass)
pg_curs13= pg_conn.cursor()
query="""
    SELECT Survived,AVG(Parents_Children_Aboard)Parents_Children_Aboard
    FROM titanic

    GROUP BY Survived
    
"""
pg_curs13.execute(query)
pcaS= pg_curs13.fetchall()
print(pcaS)

pg_curs14= pg_conn.cursor()
query="""
    SELECT Name ,COUNT(*) 
    FROM titanic
    GROUP BY Name
    HAVING COUNT(*) >1
    
"""
pg_curs14.execute(query)
duplicateName= pg_curs14.fetchall()
print(duplicateName)