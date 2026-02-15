# 🎯 QR Creator

### (Quiz Royale Creator)

QR Creator is a desktop quiz authoring application built with **Python** and **PySide6**.
It allows educators and quiz makers to create, edit, manage, import, and export quizzes in JSON format.

The application supports both **Multiple Choice** and **Identification** type questions.

---

## 🚀 Features

* ✅ Create Multiple Choice questions (exactly 4 options)
* ✅ Create Identification questions
* ✅ Multi-line support for questions and answers
* ✅ Add new questions
* ✅ Update existing questions
* ✅ Delete questions
* ✅ View and edit questions from a list
* ✅ Import quizzes from JSON
* ✅ Export quizzes to JSON

---

## 🧠 Question Types

### 1️⃣ Multiple Choice

* Requires exactly **4 options**
* Correct answer is stored as an index (0–3)

Example:

```json
{
  "type": "multiple_choice",
  "question": "What is 2 + 2?",
  "options": ["1", "2", "3", "4"],
  "answer": 3
}
```

---

### 2️⃣ Identification

* Free-text answer
* Suitable for short answer questions

Example:

```json
{
  "type": "identification",
  "question": "Capital of France?",
  "answer": "Paris"
}
```

---

## 📁 JSON Structure

All quizzes are exported in the following format:

```json
{
  "questions": [
    { ... },
    { ... }
  ]
}
```

This makes it easy to:

* Integrate with game engines (e.g., Godot)
* Connect to web backends
* Use in API-based quiz systems

---

## 🛠 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/NwizuEmmanuel/qr_creator
cd qr-creator
```

### 2️⃣ Install Dependencies

```bash
pip install pyside6
```

### 3️⃣ Run the Application

```bash
python quiz_creator.py
```

---

## 🖥️ UI Overview

* **Left Panel** → Displays all created questions
* **Right Panel** → Question editor
* **Top Dropdown** → Select question type
* **Buttons**

  * Add / Update
  * Delete
  * Import JSON
  * Export JSON

---

## 🎮 Intended Use

QR Creator is designed for:

* Teachers building quizzes
* Game developers needing quiz data
* Students creating practice tests
* Educational game systems (Quiz Royale concept)

---

## 🔮 Future Improvements (Planned Ideas)

* Radio button selection for correct MC answer
* Question preview mode
* Quiz metadata (title, author, time limit)
* Encryption or scrambling of exported files
* SQLite database support
* Flask web version
* Godot integration pipeline

---

## 📦 Requirements

* Python 3.9+
* PySide6

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👤 Author

Created as part of the **Quiz Royale system development project**.