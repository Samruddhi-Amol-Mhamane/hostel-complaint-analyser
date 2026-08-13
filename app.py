from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(
    __name__,
    template_folder="web/templates",
    static_folder="web/static"
)

CSV_FILE = "complaints.csv"

FIELDNAMES = [
    "Student",
    "Room",
    "Complaint",
    "Category",
    "Priority",
    "Status"
]


# ==========================================
# CATEGORY DETECTION
# ==========================================

def get_category(complaint):

    text = complaint.lower()

    if any(word in text for word in ["wifi", "internet", "network"]):
        return "WiFi"

    elif any(word in text for word in ["water", "tap", "leak"]):
        return "Water"

    elif any(word in text for word in ["food", "mess", "meal"]):
        return "Food"

    elif any(word in text for word in [
        "fan",
        "light",
        "switch",
        "electric",
        "electricity",
        "shock"
    ]):
        return "Electrical"

    return "General"


# ==========================================
# PRIORITY DETECTION
# ==========================================

def get_priority(complaint):

    text = complaint.lower()

    if any(word in text for word in [
        "shock",
        "fire",
        "danger",
        "emergency"
    ]):
        return "High"

    elif any(word in text for word in [
        "leak",
        "broken",
        "not working",
        "problem"
    ]):
        return "Medium"

    return "Low"


# ==========================================
# READ COMPLAINTS
# ==========================================

def read_complaints():

    complaints = []

    if not os.path.exists(CSV_FILE):
        return complaints

    with open(
        CSV_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row.get("Student"):
                complaints.append(row)

    return complaints


# ==========================================
# HOME / DASHBOARD
# ==========================================

@app.route("/")
def home():

    complaints = read_complaints()

    total = len(complaints)

    pending = sum(
        1 for c in complaints
        if c.get("Status") == "Pending"
    )

    resolved = sum(
        1 for c in complaints
        if c.get("Status") == "Resolved"
    )

    # Category analysis
    categories = {}

    for c in complaints:

        category = c.get("Category", "General")

        categories[category] = categories.get(
            category, 0
        ) + 1

    # Priority analysis
    priorities = {}

    for c in complaints:

        priority = c.get("Priority", "Low")

        priorities[priority] = priorities.get(
            priority, 0
        ) + 1

    return render_template(
        "index.html",
        complaints=complaints,
        total=total,
        pending=pending,
        resolved=resolved,
        categories=categories,
        priorities=priorities
    )


# ==========================================
# ADD COMPLAINT
# ==========================================

@app.route("/add", methods=["POST"])
def add_complaint():

    student = request.form.get(
        "student", ""
    ).strip()

    room = request.form.get(
        "room", ""
    ).strip()

    complaint = request.form.get(
        "complaint", ""
    ).strip()

    if not student or not room or not complaint:
        return redirect("/")

    category = get_category(complaint)

    priority = get_priority(complaint)

    status = "Pending"

    file_exists = os.path.exists(CSV_FILE)

    file_empty = (
        not file_exists
        or os.path.getsize(CSV_FILE) == 0
    )

    with open(
        CSV_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if file_empty:

            writer.writerow(FIELDNAMES)

        writer.writerow([
            student,
            room,
            complaint,
            category,
            priority,
            status
        ])

    return redirect("/")


# ==========================================
# UPDATE STATUS
# ==========================================

@app.route("/update/<room>")
def update_status(room):

    complaints = read_complaints()

    found = False

    for complaint in complaints:

        if complaint.get("Room") == room:

            if complaint.get("Status") == "Pending":

                complaint["Status"] = "Resolved"

            else:

                complaint["Status"] = "Pending"

            found = True

            break

    if found:

        with open(
            CSV_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=FIELDNAMES
            )

            writer.writeheader()

            writer.writerows(complaints)

    return redirect("/")


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )