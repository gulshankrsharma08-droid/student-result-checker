#Part 1 — Import Flask & Create App
from flask import Flask, render_template, request

app = Flask(__name__)

#Part 2 — Adding Student Data
students = {
    "1001": {"name": "Gulshan", "marks": {"Python": 85, "HTML": 90, "CSS": 92, "JavaScript": 98, "Database": 100}},
    "1002": {"name": "Rajesh",  "marks": {"Python": 55, "HTML": 60, "CSS": 58, "JavaScript": 70, "Database": 65}},
    "1003": {"name": "Harish",  "marks": {"Python": 40, "HTML": 35, "CSS": 50, "JavaScript": 45, "Database": 90}},
    "1004": {"name": "Sala",    "marks": {"Python": 85, "HTML": 90, "CSS": 78, "JavaScript": 98, "Database": 80}},
    "1005": {"name": "Abhi",    "marks": {"Python": 89, "HTML": 55, "CSS": 52, "JavaScript": 98, "Database": 90}},
    "1006": {"name": "Rohith",  "marks": {"Physics":78, "Chemistry": 76, "Bio": 87, "Micro":88, "Zool": 89}}
}

#Part 3 — Adding Grade Logic
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
        return "F"

#Part 4 — Adding Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    roll = request.form["roll"]
    student = students.get(roll)

    if student:
        marks = student["marks"]
        total = sum(marks.values())
        percentage = (total / 500) * 100
        grade = get_grade(percentage)
        passed = percentage >= 40
        return render_template("result.html", student=student, total=total, percentage=percentage, grade=grade, passed=passed)
    else:
        return render_template("index.html", error="Roll number not found!")

if __name__ == "__main__":
    app.run(debug=True)