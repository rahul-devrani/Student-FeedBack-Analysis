# 🎓 Student Feedback Analysis System

A simple yet powerful feedback analysis web application built using **Flask (Python)**, **MySQL**, and **HTML/CSS/JS**.  
Students can log in and submit feedback, while admins can view a stylish dashboard with analytics, charts, and recent comments.

---

## 📸 Project Overview

> 🔒 Role-based Login | 📊 Dashboard Analytics | 📝 Feedback Forms | 🌙 Dark Theme UI

### 👥 Roles
- **Student**: Can log in and submit feedback
- **Admin**: Can log in to view total feedbacks, charts, and suggestions

---

## 💻 Technologies Used

| Layer      | Tech                      |
|------------|---------------------------|
| Frontend   | HTML, CSS, JavaScript     |
| Backend    | Python (Flask)            |
| Database   | MySQL                     |
| Charts     | Chart.js (JS)             |

---

## 📁 Folder Structure

<pre> Student-Feedback-System/ │ ├── app.py # Flask backend logic ├── static/ │ └── style.css # Theme and layout styles (dark mode) ├── templates/ │ ├── login.html # Login page (student/admin) │ ├── feedback.html # Feedback form for students │ └── dashboard.html # Admin dashboard with charts └── README.md # Project documentation </pre>





---

## 🗃️ Database Setup

1. **Create Database**
   ```sql
   CREATE DATABASE feedback_system;
   USE feedback_system;

2. **Create Tables (users and feedback)**
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100),
    role VARCHAR(20)
);

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    teaching INT,
    content INT,
    facilities INT,
    suggestion TEXT
);
```

2. **Insert Values in users table**
```sql
INSERT INTO users (username, password, role) VALUES ('admin1', 'admin1', 'admin');
INSERT INTO users (username, password, role) VALUES ('student1', 'pass1', 'student');

```

🧪 How to Run Locally

1️⃣ Clone the Repo
git clone https://github.com/rahul-devrani/Student-Feedback-Analysis.git
cd student-feedback-system

2️⃣ Install Requirements
pip install flask mysql-connector-python

3️⃣ Run the App
python app.py

4️⃣ Open in Browser
http://localhost:5000

---
