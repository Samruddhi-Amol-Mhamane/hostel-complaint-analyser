import csv
import os
import pandas as pd
import matplotlib.pyplot as plt

complaints = []

BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_FOLDER, "complaints.csv")


# ========================================
# CREATE CSV FILE
# ========================================

def create_csv_file():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Name",
                "Room",
                "Complaint",
                "Category",
                "Priority",
                "Status"
            ])


# ========================================
# LOAD COMPLAINTS
# ========================================

def load_complaints():

    with open(CSV_FILE, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            complaint = {
                "name": row["Name"],
                "room": row["Room"],
                "complaint": row["Complaint"],
                "category": row["Category"],
                "priority": row["Priority"],
                "status": row["Status"]
            }

            complaints.append(complaint)


# ========================================
# SAVE COMPLAINT
# ========================================

def save_complaint(complaint):

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            complaint["name"],
            complaint["room"],
            complaint["complaint"],
            complaint["category"],
            complaint["priority"],
            complaint["status"]
        ])


# ========================================
# UPDATE CSV FILE
# ========================================

def update_csv_file():

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Room",
            "Complaint",
            "Category",
            "Priority",
            "Status"
        ])

        for complaint in complaints:

            writer.writerow([
                complaint["name"],
                complaint["room"],
                complaint["complaint"],
                complaint["category"],
                complaint["priority"],
                complaint["status"]
            ])


# ========================================
# ANALYZE COMPLAINTS
# ========================================

def analyze_complaints():

    print("\n========== COMPLAINT ANALYSIS ==========")

    df = pd.read_csv(CSV_FILE)

    if df.empty:

        print("No complaints available for analysis.")
        return

    total = len(df)

    print("\nTotal Complaints:", total)


    # CATEGORY ANALYSIS

    print("\n----- CATEGORY-WISE COMPLAINTS -----")

    category_count = df["Category"].value_counts()

    for category, count in category_count.items():

        percentage = (count / total) * 100

        print(
            category + ":",
            count,
            "(" + str(round(percentage, 1)) + "%)"
        )

    most_common_category = category_count.idxmax()

    print("\nMost Common Category:", most_common_category)


    # PRIORITY ANALYSIS

    print("\n----- PRIORITY-WISE COMPLAINTS -----")

    priority_count = df["Priority"].value_counts()

    for priority, count in priority_count.items():

        print(priority + ":", count)

    most_common_priority = priority_count.idxmax()

    print("\nMost Common Priority:", most_common_priority)


    # STATUS ANALYSIS

    print("\n----- STATUS-WISE COMPLAINTS -----")

    status_count = df["Status"].value_counts()

    for status, count in status_count.items():

        print(status + ":", count)


    pending_count = len(df[df["Status"] == "Pending"])

    pending_percentage = (pending_count / total) * 100

    print(
        "\nPending Percentage:",
        round(pending_percentage, 1),
        "%"
    )


# ========================================
# SHOW CHARTS
# ========================================

def show_charts():

    print("\n========== SHOW CHARTS ==========")

    df = pd.read_csv(CSV_FILE)

    if df.empty:

        print("No complaints available for charts.")
        return


    # CATEGORY CHART

    category_count = df["Category"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(category_count.index, category_count.values)

    plt.title("Hostel Complaints by Category")

    plt.xlabel("Category")

    plt.ylabel("Number of Complaints")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


    # PRIORITY CHART

    priority_count = df["Priority"].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(priority_count.index, priority_count.values)

    plt.title("Hostel Complaints by Priority")

    plt.xlabel("Priority")

    plt.ylabel("Number of Complaints")

    plt.tight_layout()

    plt.show()


# ========================================
# UPDATE COMPLAINT STATUS
# ========================================

def update_status():

    print("\n========== UPDATE COMPLAINT STATUS ==========")

    room = input("Enter room number: ")

    found = False


    for complaint in complaints:

        if complaint["room"] == room:

            found = True

            print("\nComplaint Found!")

            print("Student:", complaint["name"])
            print("Room:", complaint["room"])
            print("Complaint:", complaint["complaint"])
            print("Category:", complaint["category"])
            print("Priority:", complaint["priority"])
            print("Current Status:", complaint["status"])


            print("\n1. Pending")
            print("2. Resolved")

            status_choice = input("\nEnter new status: ")


            if status_choice == "1":

                complaint["status"] = "Pending"

            elif status_choice == "2":

                complaint["status"] = "Resolved"

            else:

                print("\nInvalid status choice.")

                return


            # Save updated status to CSV

            update_csv_file()


            print("\nStatus updated successfully!")

            print("New Status:", complaint["status"])

            return


    if found == False:

        print("\nNo complaint found for room", room)


# ========================================
# START PROGRAM
# ========================================

create_csv_file()
load_complaints()


print("========================================")
print("       HOSTEL COMPLAINT ANALYZER")
print("========================================")


while True:

    print("\n1. Add Complaint")
    print("2. View Complaints")
    print("3. Search Complaint")
    print("4. Analyze Complaints")
    print("5. Show Charts")
    print("6. Exit")
    print("7. Update Complaint Status")

    choice = input("\nEnter your choice: ")


    # ========================================
    # 1. ADD COMPLAINT
    # ========================================

    if choice == "1":

        print("\n========== ADD COMPLAINT ==========")

        name = input("Enter student name: ")
        room = input("Enter room number: ")
        complaint = input("Enter your complaint: ")

        complaint_lower = complaint.lower()


        # CATEGORY

        if "water" in complaint_lower or "tap" in complaint_lower:

            category = "Water"

        elif "wifi" in complaint_lower or "internet" in complaint_lower:

            category = "WiFi"

        elif "food" in complaint_lower or "mess" in complaint_lower:

            category = "Food"

        elif (
            "fan" in complaint_lower
            or "light" in complaint_lower
            or "electricity" in complaint_lower
            or "electric" in complaint_lower
            or "switch" in complaint_lower
        ):

            category = "Electrical"

        elif "clean" in complaint_lower or "dirty" in complaint_lower:

            category = "Cleaning"

        else:

            category = "General"


        # PRIORITY

        if (
            "danger" in complaint_lower
            or "shock" in complaint_lower
            or "fire" in complaint_lower
        ):

            priority = "High"

        elif (
            "leak" in complaint_lower
            or "broken" in complaint_lower
            or "not working" in complaint_lower
        ):

            priority = "Medium"

        else:

            priority = "Low"


        status = "Pending"


        new_complaint = {
            "name": name,
            "room": room,
            "complaint": complaint,
            "category": category,
            "priority": priority,
            "status": status
        }


        complaints.append(new_complaint)

        save_complaint(new_complaint)


        print("\nComplaint added successfully!")

        print("Student:", name)
        print("Room:", room)
        print("Complaint:", complaint)
        print("Category:", category)
        print("Priority:", priority)
        print("Status:", status)


    # ========================================
    # 2. VIEW COMPLAINTS
    # ========================================

    elif choice == "2":

        print("\n========== ALL COMPLAINTS ==========")

        if len(complaints) == 0:

            print("No complaints found.")

        else:

            for complaint in complaints:

                print("\nStudent:", complaint["name"])
                print("Room:", complaint["room"])
                print("Complaint:", complaint["complaint"])
                print("Category:", complaint["category"])
                print("Priority:", complaint["priority"])
                print("Status:", complaint["status"])

                print("--------------------------------")


    # ========================================
    # 3. SEARCH COMPLAINT
    # ========================================

    elif choice == "3":

        print("\n========== SEARCH COMPLAINT ==========")

        search_room = input("Enter room number to search: ")

        found = False


        for complaint in complaints:

            if complaint["room"] == search_room:

                print("\nComplaint Found!")

                print("Student:", complaint["name"])
                print("Room:", complaint["room"])
                print("Complaint:", complaint["complaint"])
                print("Category:", complaint["category"])
                print("Priority:", complaint["priority"])
                print("Status:", complaint["status"])

                print("--------------------------------")

                found = True


        if found == False:

            print("\nNo complaint found for room", search_room)


    # ========================================
    # 4. ANALYZE
    # ========================================

    elif choice == "4":

        analyze_complaints()


    # ========================================
    # 5. CHARTS
    # ========================================

    elif choice == "5":

        show_charts()


    # ========================================
    # 6. EXIT
    # ========================================

    elif choice == "6":

        print("\nThank you for using Hostel Complaint Analyzer!")

        break


    # ========================================
    # 7. UPDATE STATUS
    # ========================================

    elif choice == "7":

        update_status()


    # ========================================
    # INVALID CHOICE
    # ========================================

    else:

        print("\nInvalid choice! Please enter a number from 1 to 7.")