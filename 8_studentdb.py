import sqlite3
connection = sqlite3.connect("SSPstud.db")
cursor = connection.cursor()

#CREATION OF TABLE
cursor.execute("""CREATE TABLE sdb18(
s_id INTEGER PRIMARY KEY,
s_name VARCHAR(20),
sem INTEGER(1),
dob DATE)""")

print ("table created!!!")


#INSERTION OF VALUES
cursor.execute("""INSERT INTO sdb18 VALUES(417,"SALINA",5,"13-09-1999")""")
cursor.execute("""INSERT INTO sdb18 VALUES(419,"SHUBHA",5,"20-10-1999")""")
cursor.execute("""INSERT INTO sdb18 VALUES(420,"SHWETA",5,"18-04-1999")""")
cursor.execute("""INSERT INTO sdb18 VALUES(421,"TEJASHWINI",5,"01-10-1999")""")
cursor.execute("""INSERT INTO sdb18 VALUES(423,"YAMUNA",5,"28-12-1999")""")
connection.commit()
print("Vlaues inserted!!")


#DISPLAY OF VALUES
cursor.execute("""SELECT * FROM sdb18""")
table=cursor.fetchall()
for i in table:
    print (i)

#FETCHING THE REQUIRED DATA OF THE STUDENT
print("RETRIEVE DATA OF SPECIFIC STUDENT")   
cursor.execute("""SELECT s_id FROM sdb18 WHERE s_name="YAMUNA" """ )
result= cursor.fetchall()
print(result)


#UPDATE STUDENT INFO
cursor.execute("""UPDATE sdb18 SET s_name = 'SHUBHAPATIL' where s_id='419'""")
connection.commit()
print ("Row updated :")
#DISPLAY OF VALUES AFTER UPDATION
cursor.execute("""SELECT * FROM sdb18""")
table=cursor.fetchall()
for i in table:
    print (i)


#DELETE STUDENT INFO
cursor.execute("""DELETE FROM sdb18 WHERE s_id='419' """)
print ("Row deleted :")
#DISPLAY OF VALUES after delete
cursor.execute("""SELECT * FROM sdb18""")
table=cursor.fetchall()
for i in table:
    print (i)

connection.commit()
#print ("Total number of rows updated :", cursor.total_changes)


connection.close()

""" 
   output
   
   
   
   table created!!!
Vlaues inserted!!
(417, 'SALINA', 5, '13-09-1999')
(419, 'SHUBHA', 5, '20-10-1999')
(420, 'SHWETA', 5, '18-04-1999')
(421, 'TEJASHWINI', 5, '01-10-1999')
(423, 'YAMUNA', 5, '28-12-1999')
RETRIEVE DATA OF SPECIFIC STUDENT
[(423,)]
Row updated :
(417, 'SALINA', 5, '13-09-1999')
(419, 'SHUBHAPATIL', 5, '20-10-1999')
(420, 'SHWETA', 5, '18-04-1999')
(421, 'TEJASHWINI', 5, '01-10-1999')
(423, 'YAMUNA', 5, '28-12-1999')
Row deleted :
(417, 'SALINA', 5, '13-09-1999')
(420, 'SHWETA', 5, '18-04-1999')
(421, 'TEJASHWINI', 5, '01-10-1999')
(423, 'YAMUNA', 5, '28-12-1999')



"""
