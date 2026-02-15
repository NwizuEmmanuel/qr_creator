import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QTextEdit, QPushButton, QListWidget,
    QComboBox, QFileDialog, QMessageBox
)


class QuizCreator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Creator (Quiz Royale Creator)")
        self.setMinimumWidth(800)

        self.questions = []
        self.current_index = None
        self.current_file = None  # 🔥 No default file

        self.init_ui()

    # ----------------------------
    # UI
    # ----------------------------
    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        self.list_widget = QListWidget()
        self.list_widget.clicked.connect(self.load_selected_question)
        main_layout.addWidget(self.list_widget, 2)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout, 3)

        self.type_combo = QComboBox()
        self.type_combo.addItems(["multiple_choice", "identification"])
        self.type_combo.currentTextChanged.connect(self.toggle_options)
        right_layout.addWidget(QLabel("Question Type"))
        right_layout.addWidget(self.type_combo)

        self.question_edit = QTextEdit()
        right_layout.addWidget(QLabel("Question"))
        right_layout.addWidget(self.question_edit)

        self.option_edits = []
        for i in range(4):
            edit = QTextEdit()
            edit.setPlaceholderText(f"Option {i+1}")
            edit.setMaximumHeight(60)
            self.option_edits.append(edit)
            right_layout.addWidget(edit)

        self.answer_edit = QTextEdit()
        self.answer_edit.setMaximumHeight(60)
        right_layout.addWidget(QLabel("Answer (Index 0-3 for MC / Text for Identification)"))
        right_layout.addWidget(self.answer_edit)

        btn_layout = QHBoxLayout()
        right_layout.addLayout(btn_layout)

        self.add_btn = QPushButton("Add / Update")
        self.add_btn.clicked.connect(self.add_or_update_question)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_question)

        self.import_btn = QPushButton("Import JSON")
        self.import_btn.clicked.connect(self.import_json)

        self.export_btn = QPushButton("Export As")
        self.export_btn.clicked.connect(self.export_json)

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(self.import_btn)
        btn_layout.addWidget(self.export_btn)

        self.toggle_options()

    # ----------------------------
    # Save Logic
    # ----------------------------
    def save_to_file(self):
        # If no file selected yet → ask user
        if not self.current_file:
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Save Quiz",
                "",
                "JSON Files (*.json)"
            )

            if not file_name:
                return  # User cancelled save

            self.current_file = file_name

        # Save to selected file
        with open(self.current_file, "w") as f:
            json.dump({"questions": self.questions}, f, indent=4)

    # ----------------------------
    # Question Logic
    # ----------------------------
    def toggle_options(self):
        is_mc = self.type_combo.currentText() == "multiple_choice"
        for edit in self.option_edits:
            edit.setVisible(is_mc)

    def add_or_update_question(self):
        q_type = self.type_combo.currentText()
        question_text = self.question_edit.toPlainText().strip()

        if not question_text:
            QMessageBox.warning(self, "Error", "Question cannot be empty")
            return

        if q_type == "multiple_choice":
            options = [e.toPlainText().strip() for e in self.option_edits]

            if any(not opt for opt in options):
                QMessageBox.warning(self, "Error", "All 4 options required")
                return

            try:
                answer = int(self.answer_edit.toPlainText().strip())
                if answer < 0 or answer > 3:
                    raise ValueError
            except:
                QMessageBox.warning(self, "Error", "Answer must be 0-3")
                return

            question_data = {
                "type": "multiple_choice",
                "question": question_text,
                "options": options,
                "answer": answer
            }
        else:
            answer = self.answer_edit.toPlainText().strip()
            if not answer:
                QMessageBox.warning(self, "Error", "Answer required")
                return

            question_data = {
                "type": "identification",
                "question": question_text,
                "answer": answer
            }

        if self.current_index is not None:
            self.questions[self.current_index] = question_data
        else:
            self.questions.append(question_data)

        self.refresh_list()
        self.clear_form()
        self.save_to_file()  # 🔥 Auto-save

    def delete_question(self):
        if self.current_index is not None:
            del self.questions[self.current_index]
            self.refresh_list()
            self.clear_form()
            self.save_to_file()  # 🔥 Auto-save

    def load_selected_question(self):
        self.current_index = self.list_widget.currentRow()
        question = self.questions[self.current_index]

        self.type_combo.setCurrentText(question["type"])
        self.question_edit.setPlainText(question["question"])

        if question["type"] == "multiple_choice":
            for i, opt in enumerate(question["options"]):
                self.option_edits[i].setPlainText(opt)
            self.answer_edit.setPlainText(str(question["answer"]))
        else:
            self.answer_edit.setPlainText(question["answer"])

    def refresh_list(self):
        self.list_widget.clear()
        for i, q in enumerate(self.questions):
            preview = q["question"].split("\n")[0]
            self.list_widget.addItem(f"{i+1}. {preview}")

    def clear_form(self):
        self.current_index = None
        self.question_edit.clear()
        self.answer_edit.clear()
        for edit in self.option_edits:
            edit.clear()

    # ----------------------------
    # Import / Export
    # ----------------------------
    def import_json(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Open Quiz",
            "",
            "JSON Files (*.json)"
        )
        if file_name:
            with open(file_name, "r") as f:
                data = json.load(f)
                self.questions = data.get("questions", [])
                self.current_file = file_name  # 🔥 Imported file becomes active
                self.refresh_list()

    def export_json(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Export Quiz As",
            "",
            "JSON Files (*.json)"
        )
        if file_name:
            with open(file_name, "w") as f:
                json.dump({"questions": self.questions}, f, indent=4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizCreator()
    window.show()
    sys.exit(app.exec())