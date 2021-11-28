# %%
# 1. Creates a connection to our Server.
from typing import Concatenate
import mysql.connector 
from hw import Password as pw 



#code will connect us to server itself not db but server itself only
# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     auth_plugin='mysql_native_password'
# )
# my_cursor = mydb.cursor()


# 2. Creates a DATABASE called lab_server on our server. (NOT A TABLE. A DB.)

# sql_db = "CREATE database lab_server1"; 

# my_cursor.execute(sql_db)

# 3. Print out all the database on the server.

# print("list of databases")
# my_cursor.execute("SHOW DATABASES")
# print(my_cursor.fetchall())
# %%

# 4. Creates a Connection to our lab_server DATABASE.
# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()
# %%
# 5. Creates a TABLE called STUDENTS. The TABLE should have the following Columns. 
# An INT as the PRIMARY KEY called id that AUTO INCRIMENTS, a VARCHAR(255) as FIRST_NAME, and an INT as AVG_GRADE.
# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()
# my_cursor.execute("DROP TABLE STUDENTS")

# my_cursor.execute("CREATE TABLE STUDENTS (id INT AUTO_INCREMENT PRIMARY KEY, FIRST_NAME VARCHAR(255), AVG_GRADE INT)")

# print(my_cursor)

# %%
#6. Print all tables in our Schema
# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()
 
# my_cursor.execute("DESCRIBE STUDENTS")
 
# for x in my_cursor:
#   print(x)

# %%
# 7. Fill the table with Dummy Data. Names don't have to be unique. 
# Pass 0s as the AVG_GRADE for now.

# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()
# my_cursor.execute("INSERT INTO STUDENTS(FIRST_NAME, AVG_GRADE) VALUES (%s, %s)", ("Tim", 0))
# my_cursor.execute("INSERT INTO STUDENTS(FIRST_NAME, AVG_GRADE) VALUES (%s, %s)", ("Meron", 0))
# my_cursor.execute("INSERT INTO STUDENTS(FIRST_NAME, AVG_GRADE) VALUES (%s, %s)", ("Jake", 0))
# my_cursor.execute("INSERT INTO STUDENTS(FIRST_NAME, AVG_GRADE) VALUES (%s, %s)", ("Dan", 0))
# my_cursor.execute("INSERT INTO STUDENTS(FIRST_NAME, AVG_GRADE) VALUES (%s, %s)", ("Kiya", 0))
# mydb.commit()
#%% 

#7. Creates a TABLE called student_grades 
# that contains the columns student_id as an int,
#assignment_num as an int, assignment_grade as an int, 
# and assignment_name_and_student_id as a VARCHAR(255) which should be the primary key.

# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()

# my_cursor.execute(
#   "CREATE TABLE student_grades(student_id INT, assignemnt_num INT, assignment_grade INT, assignment_name_and_student_id VARCHAR(255) PRIMARY KEY)"
#   )

# %%
#8. Check to see that the TABLE exists.

# mydb = mysql.connector.connect(
#     host="localhost", 
#     user= "root", 
#     password=pw,
#     database = "lab_server"
# )
# my_cursor = mydb.cursor()

# my_cursor.execute("SELECT * FROM student_grades")
 
# for x in my_cursor:
#   print(x)
# %%
# 9. Add rows to the students_grades table. 
# Every student should have 4 assignments. 
# Grades can be random. assignment_name_and_student_id should be a string that combines the assignment number 
# and student ID to make a unique key.

mydb = mysql.connector.connect(
    host="localhost", 
    user= "root", 
    password=pw,
    database = "lab_server"
)
my_cursor = mydb.cursor()

 
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(1, 101, 95,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(2, 101, 93,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(3, 101, 90,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(4, 101, 85,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(5, 101, 90,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(1, 201, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(2, 201, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(3, 201, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(4, 201, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(5, 201, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(1, 301, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(2, 301, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(3, 301, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(4, 301, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(5, 301, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(1, 401, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(2, 401, 99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(3, 401, 79,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(4, 401 ,99,concat(student_id,'-',assignemnt_num))")
my_cursor.execute("INSERT INTO student_grades(student_id, assignemnt_num,assignment_grade,assignment_name_and_student_id)"
"values(5, 401,79,concat(student_id,'-',assignemnt_num))")


mydb.commit()


# %%
