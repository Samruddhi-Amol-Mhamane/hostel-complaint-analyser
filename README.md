# 🏠 Hostel Complaint Analyzer

A Python and Flask-based web application designed to manage, track, and analyze hostel complaints efficiently.

## 📌 About the Project

The Hostel Complaint Analyzer provides a simple digital platform where hostel students can submit their complaints and hostel management can track, update, and analyze them.

The system automatically identifies the **complaint category** and **priority**, stores complaint data, and provides useful analysis of the complaints.

## 🎯 Problem Statement

In hostels, complaints related to water, electricity, Wi-Fi, food, maintenance, and other facilities are often managed manually.

This project aims to provide a simple system to:

* Record hostel complaints digitally
* Categorize complaints automatically
* Identify complaint priority
* Track complaint status
* Analyze complaint data
* Display complaint statistics

## ✨ Features

* 📝 Add new complaints
* 🏷️ Automatic complaint categorization
* ⚡ Automatic priority detection
* 📋 View all complaints
* 🔍 Search complaints
* 🔄 Update complaint status
* 📊 Analyze complaints
* 📈 Display complaint statistics and charts
* 💾 Store complaint data using CSV

## 🛠️ Technologies Used

* **Python**
* **Flask**
* **Pandas**
* **Matplotlib**
* **HTML**
* **CSS**
* **JavaScript**
* **CSV**

## ⚙️ How It Works

1. The student enters complaint details through the web application.
2. The complaint is processed using Python.
3. The system identifies the complaint category.
4. The system determines the priority of the complaint.
5. Complaint information is stored in a CSV file.
6. Users can view and search complaints.
7. Complaint status can be updated.
8. Pandas is used to analyze the complaint data.
9. Matplotlib is used to generate charts for visualization.

## 📂 Project Structure

```text
hostel_complaint_analyser/
│
├── app.py
├── main.py
├── complaints.csv
│
└── web/
    ├── templates/
    │   └── index.html
    │
    └── static/
        ├── style.css
        └── script.js
│
└── README.md
```

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

### 2. Open the project folder

```bash
cd hostel_complaint_analyser
```

### 3. Install required libraries

```bash
pip install flask pandas matplotlib
```

### 4. Run the Flask application

```bash
python app.py
```

### 5. Open the application

Open the local URL shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

## 📊 Example Analysis

The application can provide information such as:

* Total number of complaints
* Category-wise complaints
* Priority-wise complaints
* Most common complaint category
* Complaint status

## 🚀 Future Improvements

Some possible improvements for future versions include:

* User login and authentication
* Database integration using MySQL or SQLite
* Admin dashboard
* Email notifications
* Advanced complaint classification using Machine Learning
* Deployment of the application online

## 👩‍💻 Project Developed By

**Samruddhi Mhamane**

B.Tech – Artificial Intelligence & Machine Learning

## ⭐ Conclusion

The Hostel Complaint Analyzer demonstrates how Python, Flask, data analysis, and web technologies can be combined to create a practical solution for managing hostel complaints.
