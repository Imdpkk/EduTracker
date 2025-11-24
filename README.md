📘 EduTracker – Python-based Learning Management System (CLI App)

EduTracker is a Python-based command-line LMS that allows users to enroll in courses, track their progress, and view personalized study dashboards. The system supports multi-user functionality and stores data using JSON for persistence.

🔥 Features

Multi-user LMS system

Course enrollment

Progress tracking (0–100%)

Automatic study-hour recommendations

JSON-based permanent data storage

Clean CLI-based dashboard

Input validation & error handling

🛠️ Tech Used

Python

JSON Storage

Functions & Modular Code

CLI Interaction

Error Handling

🚀 How It Works

User enters their name

If user exists → loads their previous progress

If new user → enrolls in a course

User provides course progress

A personalized dashboard is displayed

Data is saved in edutracker_data.json

📂 Project Structure
│── edutracker.py
│── edutracker_data.json
│── README.md

💡 Future Enhancements

SQLite database support

GUI using Tkinter

Web version using Django or Flask

Cloud deployment (AWS EC2 + S3)
