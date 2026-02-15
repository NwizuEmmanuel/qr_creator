# 🎯 QR Creator

### (Quiz Royale Creator)

---

# 🎯 QR Creator (Quiz Royale Creator)

QR Creator is a desktop quiz authoring tool built with **Python** and **PySide6**.
It allows educators and developers to create, edit, manage, import, and export quiz files in JSON format.

The application supports:

* Multiple Choice (4 options required)
* Identification (short answer)

It features automatic saving with file selection on first save.

---

# 🚀 Features

* ✅ Create Multiple Choice questions (exactly 4 options)
* ✅ Create Identification questions
* ✅ Multi-line support for questions and answers
* ✅ Add / Update questions
* ✅ Delete questions
* ✅ View and edit questions from a list
* ✅ Import existing quiz JSON files
* ✅ Export quiz to new file
* ✅ Automatic saving to selected file

---

# 🖥️ How To Use The Application

## 1️⃣ Launch the App

```bash
python quiz_creator.py
```

---

## 2️⃣ Creating a New Quiz

1. Select **Question Type** from the dropdown:

   * `multiple_choice`
   * `identification`

2. Enter your question in the **Question** field.

3. If Multiple Choice:

   * Fill in all 4 options.
   * Enter the correct answer index (0–3).

4. If Identification:

   * Enter the correct answer text.

5. Click **Add / Update**.

👉 On the first save, you will be asked to choose:

* File name
* Save location

After that, the app automatically saves all changes to that file.

---

## 3️⃣ Editing a Question

1. Click a question from the left panel list.
2. Modify the fields.
3. Click **Add / Update**.
4. Changes are automatically saved.

---

## 4️⃣ Deleting a Question

1. Select a question from the list.
2. Click **Delete**.
3. The file auto-saves.

---

## 5️⃣ Importing a Quiz

1. Click **Import JSON**.
2. Select a `.json` file.
3. The imported file becomes the active working file.
4. Any changes will automatically save to that file.

---

## 6️⃣ Exporting a Quiz Copy

1. Click **Export As**.
2. Choose file name and location.
3. A new file will be created.
4. The current working file remains unchanged.

---

# 📁 JSON Format Structure

Example:

```json
{
  "questions": [
    {
      "type": "multiple_choice",
      "question": "What is 2 + 2?",
      "options": ["1", "2", "3", "4"],
      "answer": 3
    },
    {
      "type": "identification",
      "question": "Capital of France?",
      "answer": "Paris"
    }
  ]
}
```

---

# 🛠 Installation

## Requirements

* Python 3.9+
* PySide6

Install dependencies:

```bash
pip install pyside6
```

Run:

```bash
python quiz_creator.py
```

---

# 📦 Packaging The Application

QR Creator can be packaged into a standalone executable using **PyInstaller**.

---

## 🔹 Install PyInstaller

```bash
pip install pyinstaller
```

---

## 🔹 Option 1: One-File Executable (Single .exe)

Recommended for simple distribution.

```bash
pyinstaller --onefile --windowed --name "QR Creator" quiz_creator.py
```

### Output:

```
dist/QR Creator.exe
```

✔ Easy to share
✔ Single file
⚠ Slightly slower startup

---

## 🔹 Option 2: Folder Distribution (Faster Startup)

Recommended for better performance.

```bash
pyinstaller --windowed --name "QR Creator" quiz_creator.py
```

### Output:

```
dist/QR Creator/
```

✔ Faster startup
✔ More stable
✔ Professional distribution format

---

## 🔹 Adding an Icon (Optional)

```bash
pyinstaller --onefile --windowed --icon=icon.ico --name "QR Creator" quiz_creator.py
```

---

## ⚠ Important Notes

* You must build on the same OS you want to distribute on.

  * Windows → Build on Windows
  * Linux → Build on Linux
  * macOS → Build on macOS

* If packaging fails with PySide6 plugin issues:

```bash
pyinstaller --onefile --windowed --collect-all PySide6 quiz_creator.py
```

---

# 🧠 Recommended Distribution Strategy

For educational or institutional deployment:

✔ Use folder distribution
✔ Add a custom icon
✔ Create an installer (Inno Setup on Windows)

---

# 🔮 Future Improvements

* Radio button selection for correct MC answer
* Quiz metadata (title, author, timer)
* SQLite database backend
* Encrypted quiz export
* Flask web version
* Godot integration support

---

# 📄 License

MIT License

---

# 👤 Author

Developed as part of the **Quiz Royale System Project**.