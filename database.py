import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        roll_no TEXT PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# Create marks table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS marks (
        roll_no TEXT,
        subject TEXT,
        marks INTEGER,
        FOREIGN KEY (roll_no) REFERENCES students (roll_no)
    )
''')

print("Database and tables created successfully!")
conn.commit()
conn.close()