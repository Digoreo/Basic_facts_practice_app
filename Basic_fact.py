from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QComboBox,
                             QProgressBar, QTableWidget, QTableWidgetItem, QCheckBox, QVBoxLayout)
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import QTime, QTimer, Qt
import random
import os, sys
if hasattr(sys, '_MEIPASS'):
    image_path = os.path.join(sys._MEIPASS, "Calculator.png")
else:
    image_path = "Calculator.png"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.win_screen()
        self.lineEdit()
        self.Add_image()
        self.combobox()
        # self.score_table()

        # Button
        self.btn_start.clicked.connect(self.startgame)
        self.btn_msg.clicked.connect(self.msg_box)
        self.btn_result.clicked.connect(self.start_progress)

        self.btn_result.clicked.connect(self.GetResult)

    # Window
    def win_screen(self):
        self.setGeometry(500, 150, 400, 500)
        self.setWindowTitle("Basic Facts")
        self.setWindowIcon(QIcon("calculater"))

        self.Score1 = 0
        font = QFont("Open Sans", 12, QFont.Bold)


        #Labels
        self.lbl_score = QLabel("Score:            ", self)
        self.lbl_score.move(250, 50)
        self.lbl_score.setFont(font)

        self.lbl_num1 = QLabel("       ", self)
        self.lbl_num1.move(50, 130)
        self.lbl_num1.setFont(font)
        # self.lbl_num1.setAlignment(Qt.setAlignCenter)

        self.lbl_num2 = QLabel("       ", self)
        self.lbl_num2.move(200, 130)
        self.lbl_num2.setFont(font)

        self.lbl_sign = QLabel("       ", self)
        self.lbl_sign.move(125, 130)
        self.lbl_sign.setFont(font)

        self.lbl_result = QLabel("                                      ", self)
        self.lbl_result.move(50, 330)
        self.lbl_result.setFont(font)

        self.lbl_time = QLabel("                              ", self)
        self.lbl_time.move(50, 380)
        self.lbl_time.setFont(font)




        # progress bar
        self.progress1 = QProgressBar(self)
        self.progress1.setGeometry(30, 290, 210, 30)


        # button
        self.btn_start = QPushButton("Start", self)
        self.btn_start.move(90, 90)

        self.btn_msg = QPushButton("Exit", self)
        self.btn_msg.move(90, 420)

        self.btn_result = QPushButton("Get the result", self)
        self.btn_result.move(90, 240)

    def start_progress(self):
        import time
        for i in range(101):
            time.sleep(0.00001)
            self.progress1.setValue(i)

    def reaction(self):
        if self.checkbox_plus.isChecked() == True:
            self.lbl_sign.setText("+")
        elif self.checkbox_minus.isChecked() == True:
            self.lbl_sign.setText("-")
        elif self.checkbox_multiply.isChecked() == True:
            self.lbl_sign.setText("X")
        elif self.checkbox_division.isChecked() == True:
            self.lbl_sign.setText("/")

    def lineEdit(self):
        self.lineEdit1 = QLineEdit(self)
        self.lineEdit1.setGeometry(100, 180, 50, 30)
        self.lineEdit1.returnPressed.connect(self.GetResult)
        self.lineEdit1.returnPressed.connect(self.start_progress)
        self.lineEdit1.returnPressed.connect(self.lineEdit1.clear)


    # Random digit
    def startgame(self):
        self.lineEdit1.clear()

        if self.sign == "+" or self.sign == "-":
            self.digit1 = random.choice(range(100))
            self.digit2 = random.choice(range(100))
        elif self.sign == "X":
            self.digit1 = random.choice(range(10))
            self.digit2 = random.choice(range(10))
        elif self.sign == "/":
            self.digit1 = random.choice(range(100))
            self.digit2 = random.choice(range(10))

        self.lbl_num1.setText(str(self.digit1))
        self.lbl_num2.setText(str(self.digit2))

        self.lineEdit1.setFocus()

        self.time1 = QTime.currentTime()
        print(self.time1.toString())

    def GetResult(self):
        self.time2 = QTime.currentTime()
        print(self.time2.toString("hh:mm:ss"))
        self.total_time = self.time1.msecsTo(self.time2) / 1000.0
        print(self.total_time)
        # print(self.total_time.toString("hh:mm:ss"))

        if self.sign == "+":
            self.Result1 = self.digit1 + self.digit2
        elif self.sign == "-":
            self.Result1 = self.digit1 - self.digit2
        elif self.sign == "X":
            self.Result1 = self.digit1 * self.digit2
        elif self.sign == "/":
            self.Result1 = self.digit1 // self.digit2


        self.input1 = int(self.lineEdit1.text())

        if self.Result1 == self.input1:
            self.Score1 = self.Score1 + 1
            self.lbl_result.setText("         Currect")
        else:
            self.Score1 = self.Score1 - 1
            self.lbl_result.setText(f"Currect Answer: {self.Result1}")

        self.lbl_score.setText("Score: " + str(self.Score1))
        #self.table.setItem(0, 1, QTableWidgetItem(str(self.lbl_score)))
        # self.lbl_score.setText(f"Score: {str(self.Score1)}")

        self.lbl_time.setText(f"   Time: {self.total_time} s")
        self.lbl_num1.setText("       ")
        self.lbl_num2.setText("       ")

    # Add image
    def Add_image(self):
        self.lbl_img = QLabel(self)
        self.Back_ground = QPixmap(image_path)
        self.lbl_img.setPixmap(self.Back_ground)
        self.lbl_img.move(180, 120)
        # self.lbl_img.setSizeIncrement(self, 200, 200)

    # combobox
    def combobox(self):
        self.combobox_1 = QComboBox(self)
        self.combobox_1.addItem("Plus", self)
        self.combobox_1.addItem("Minus", self)
        self.combobox_1.addItem("Multiply", self)
        self.combobox_1.addItem("Division", self)
        self.combobox_1.move(80, 50)
        self.combobox_1.resize(100, 20)

        self.combobox_1.activated.connect(self.test)

    def test(self):
        text = self.combobox_1.currentText()
        if text == "Plus":
            self.sign = "+"
        elif text == "Minus":
            self.sign = "-"
        elif text == "Multiply":
            self.sign = "X"
        elif text == "Division":
            self.sign = "/"

        self.lbl_sign.setText(self.sign)

        self.startgame()

    # Message
    def msg_box(self):
        msg = QMessageBox.question(
            self,
            "Exit",
            "Are you sure?",
            QMessageBox.Yes | QMessageBox.Cancel
        )

        if msg == QMessageBox.Yes:
            exit()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(app.exec())
