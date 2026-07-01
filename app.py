from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    roll = request.form["roll"]
    conn = get_db()
    cursor = conn.cursor()

    # Get student name
    student = cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?", (roll,)
    ).fetchone()

    if student:
        # Get marks
        marks_data = cursor.execute(
            "SELECT subject, marks FROM marks WHERE roll_no = ?", (roll,)
        ).fetchall()
        conn.close()

        marks = {row["subject"]: row["marks"] for row in marks_data}
        total = sum(marks.values())
        percentage = (total / 500) * 100
        grade = get_grade(percentage)
        passed = percentage >= 40

        return render_template("result.html",
            roll=roll,
            student=student,
            marks=marks,
            total=total,
            percentage=round(percentage, 1),
            grade=grade,
            passed=passed
        )
    else:
        conn.close()
        return render_template("index.html", error="Roll number not found!")

if __name__ == "__main__":
    app.run(debug=True)