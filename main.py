
import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
)

cursor = conn.cursor()

# Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS School_Record")
print("Database Created Sucessfully")

# To use School_Record
cursor.execute("USE School_Record")
print("Using School_Record")


# To Create a Table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        age INT,
        grade FLOAT
    )
""")
print("Table Created Sucessfully")


# Insert a new student record
cursor.execute("""
    INSERT INTO students (first_name, last_name, age, grade)
    VALUES ('Alice', 'Smith', 18, 95.5)
""")
conn.commit()
print("Data Inserted sucessfully")


# # Update the grade of the student with the first name "Alice"
cursor.execute("""
    UPDATE students
    SET grade = 97.0
    WHERE first_name = 'Alice' AND last_name = 'Smith'
""")
conn.commit()
print("Data Updated Sucessfully")


# # # Delete the student with the last name "Smith"
cursor.execute("""
    DELETE FROM students
    WHERE last_name = 'Smith'
""")
conn.commit()
print("Data deleted sucessfully where last name is 'Smith' ")

# Fetch and display all student records
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()
for student in students:
    print(student)

# Close the connection
conn.close()








