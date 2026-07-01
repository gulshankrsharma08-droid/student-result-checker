import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Student data
students = [
    ("1001", "Gulshan"),
    ("1002", "Rajesh"),
    ("1003", "Harish"),
    ("1004", "Sala"),
    ("1005", "Abhi"),
    ("1006", "Gani"),
]

# Marks data
marks = [
    ("1001", "Python", 85), ("1001", "HTML", 90), ("1001", "CSS", 92), ("1001", "JavaScript", 98), ("1001", "Database", 100),
    ("1002", "Python", 55), ("1002", "HTML", 60), ("1002", "CSS", 58), ("1002", "JavaScript", 70), ("1002", "Database", 65),
    ("1003", "Python", 40), ("1003", "HTML", 35), ("1003", "CSS", 50), ("1003", "JavaScript", 45), ("1003", "Database", 90),
    ("1004", "Python", 85), ("1004", "HTML", 90), ("1004", "CSS", 78), ("1004", "JavaScript", 98), ("1004", "Database", 80),
    ("1005", "Python", 89), ("1005", "HTML", 55), ("1005", "CSS", 52), ("1005", "JavaScript", 98), ("1005", "Database", 90),
    ("1006", "Python", 80), ("1006", "HTML", 60), ("1006", "CSS", 92), ("1006", "JavaScript", 80), ("1006", "Database", 80),
]

# Insert students
cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?)", students)

# Insert marks
cursor.executemany("INSERT INTO marks VALUES (?, ?, ?)", marks)

conn.commit()
conn.close()
print("Student data inserted successfully!")