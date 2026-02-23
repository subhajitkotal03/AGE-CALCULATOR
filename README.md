# 🎂 Age Calculator Web App

A simple Flask-based web application that calculates a user's exact age in years, months, and days based on their date of birth and stores calculation history.

---

## 📌 Description

This project is built using Python (Flask) for the backend and HTML, CSS, and JavaScript for the frontend. Users enter their name and date of birth, and the application calculates their precise age relative to the current system date. Each calculation is stored in a CSV file and can be viewed later through a history modal.

The application demonstrates form handling, server-side processing, file-based storage, template rendering, and frontend-backend integration. It is lightweight, beginner-friendly, and suitable for learning Flask fundamentals.

---

## 🚀 Features

- Accurate age calculation (Years, Months, Days)
- Input validation (prevents future dates)
- History stored in CSV file
- Modal-based history display
- Clean and responsive UI

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- CSV (File Storage)

---

## 📂 Project Structure

age-calculator/
│
├── app.py  
├── history.csv  
├── templates/  
│   └── index.html  
├── README.md  
└── requirements.txt  

---

## ⚙️ Installation

1. Clone the repository:

   git clone https://github.com/your-username/age-calculator.git  
   cd age-calculator  

2. Create a virtual environment (optional but recommended):

   python -m venv venv  

   Activate (Windows):
   venv\Scripts\activate  

   Activate (Mac/Linux):
   source venv/bin/activate  

3. Install dependencies:

   pip install flask  

4. Run the application:

   python app.py  

5. Open in browser:

   http://127.0.0.1:5000/

---

## 📊 How It Works

1. User submits name and date of birth.
2. Backend validates input.
3. Age is calculated based on current date.
4. Result is displayed on the webpage.
5. Entry is saved in history.csv.
6. History can be viewed in the modal.

---

## 🔮 Future Improvements

- Replace CSV with SQLite database
- Add delete history option
- Add authentication system
- Deploy to a cloud platform
- Improve age calculation using date libraries

---

## 📜 License

This project is open-source and available under the MIT License.
