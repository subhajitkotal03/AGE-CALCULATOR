from flask import Flask, request, render_template, Response
import os, csv
from datetime import datetime as dt

app = Flask(__name__)
H = "history.csv"

def load_history():
    if not os.path.exists(H):
        return []
    with open(H, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def save_history(entry):
    file_exists = os.path.exists(H)
    with open(H, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["name","age","date"])
        if not file_exists:
            w.writeheader()
        w.writerow(entry)

@app.route("/", methods=["GET","POST"])
def index():
    result = ""
    if request.method == "POST":
        name = request.form.get("name",""
).strip()
        dob_str = request.form.get("dob")
        try:
            year,month,day = map(int, dob_str.split("-"))
            dob = dt(year,month,day)
        except Exception:
            result = "Invalid date format. Please enter a valid date."
            return render_template("index.html", result=result)

        now = dt.now()
        if dob > now:
            result = "Date of birth cannot be in the future."
            return render_template("index.html", result=result)

        years = now.year - dob.year
        months = now.month - dob.month
        days = now.day - dob.day
        if days < 0:
            months -= 1
            prev_month = (now.month - 1) or 12
            prev_year = now.year if now.month != 1 else now.year - 1
            days += (dt(prev_year, prev_month + 1, 1) - dt(prev_year, prev_month, 1)).days
        if months < 0:
            years -= 1; months += 12

        result = f"{name}, your Age is: {years} years, {months} months, and {days} days."
        save_history({
            "name": name,
            "age": f"{years} years, {months} months, {days} days",
            "date": now.strftime("%Y-%m-%d %H:%M:%S")
        })
    return render_template("index.html", result=result)

@app.route("/history")
def history():
    if not os.path.exists(H):
        return "", 204
    with open(H, encoding="utf-8") as f:
        data = f.read()
    return Response(data, mimetype="text/csv")

if __name__ == "__main__":
    app.run(debug=True)
