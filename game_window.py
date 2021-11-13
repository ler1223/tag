import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel
from PyQt5 import QtCore
from user import User
from DB import set_statistic


class game_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('game_layout.ui', self)
        self.setWindowTitle('Game')
        self.pushButton_1.clicked.connect(self.button)
        self.pushButton_2.clicked.connect(self.button)
        self.pushButton_3.clicked.connect(self.button)
        self.pushButton_4.clicked.connect(self.button)
        self.pushButton_5.clicked.connect(self.button)
        self.pushButton_6.clicked.connect(self.button)
        self.pushButton_7.clicked.connect(self.button)
        self.pushButton_8.clicked.connect(self.button)
        self.pushButton_9.clicked.connect(self.button)
        self.pushButton_10.clicked.connect(self.button)
        self.pushButton_11.clicked.connect(self.button)
        self.pushButton_12.clicked.connect(self.button)
        self.pushButton_13.clicked.connect(self.button)
        self.pushButton_14.clicked.connect(self.button)
        self.pushButton_15.clicked.connect(self.button)
        self.pushButton_16.clicked.connect(self.button)
        self.back_btn.clicked.connect(self.close)
        self.restart_count = 0
        self.win_count = 0
        self.game_count = 0
        self.flag_game = False
        self.restart.clicked.connect(self.restart_b)
        self.name.clicked.connect(self.dialog_user_show)
        self.user = User()
        self.set_name()
        self.zero_button = self.pushButton_16
        self.zero_button_text = ""
        self.arr_button = [[self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4],
                           [self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8],
                           [self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12],
                           [self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16]]
        self.arr_number = []
        self.res_arr_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ""]
        self.completion_arr()

    signal = QtCore.pyqtSignal(str)

    def restart_b(self):
        self.restart_count += 1
        self.completion_arr()

    def completion_arr(self):
        self.arr_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        random.shuffle(self.arr_number)
        self.arr_number.append("")
        self.zero_button = self.pushButton_16
        for x in range(4):
            arr = []
            for y in range(4):
                index = x * 4 + y
                arr.append(self.arr_number[index])
                self.arr_button[x][y].setText(str(self.arr_number[index]))
        self.flag_game = False

    def button(self):
        action = self.sender()
        if not self.flag_game:
            self.game_count += 1
            self.flag_game = True
        if action == self.zero_button:
            pass
        else:
            text = int(action.text())
            x, y = self.indexing(action)
            x_zero, y_zero = self.indexing(self.zero_button)
            if (x == x_zero + 1 and y == y_zero) or (x == x_zero - 1 and y == y_zero) \
                    or (y == y_zero - 1 and x == x_zero) or (y == y_zero + 1 and x == x_zero):
                self.arr_number[x * 4 + y * 1], self.arr_number[x_zero * 4 + y_zero * 1] \
                    = self.arr_number[x_zero * 4 + y_zero * 1], self.arr_number[x * 4 + y * 1]
                text2 = self.zero_button_text
                self.zero_button.setText(str(text))
                action.setText(text2)
                self.zero_button = action
        if self.res_arr_number == self.arr_number:
            self.win_count += 1
            self.dialog()

    def indexing(self, button):
        for x in range(len(self.arr_button)):
            for y in range(len(self.arr_button[x])):
                if self.arr_button[x][y] == button:
                    return x, y

    def sendSignal(self):
        self.signal.emit('1')

    def closeEvent(self, event):
        self.sendSignal()
        if self.user.get_name() != "Гость":
            set_statistic(self.restart_count, self.win_count, self.game_count)

    def set_name(self):
        self.name.setText(self.user.get_name())

    def dialog(self):
        self.dlg = QDialog()
        text_win = QLabel("Вы победили", self.dlg)
        text_win.move(90, 10)
        text = QLabel("Хотите начать заново", self.dlg)
        text.move(70, 30)
        no_b = QPushButton("Нет", self.dlg)
        no_b.move(50, 50)
        no_b.clicked.connect(self.no_b)
        yes_b = QPushButton("Да", self.dlg)
        yes_b.move(150, 50)
        yes_b.clicked.connect(self.yes_b)
        self.dlg.setWindowTitle("Dialog")
        self.dlg.show()

    def yes_b(self):
        self.completion_arr()
        self.dlg.close()

    def no_b(self):
        self.close()
        self.dlg.close()

    def dialog_user_show(self):
        if self.user.get_name() == "Гость":
            pass
        else:
            self.dialog_user()

    def dialog_user(self):
        self.dlg_user = QDialog()
        text = QLabel("Хотите выйти из аккаунта", self.dlg_user)
        text.move(50, 30)
        no_b = QPushButton("Нет", self.dlg_user)
        no_b.move(50, 50)
        no_b.clicked.connect(self.no)
        yes_b = QPushButton("Да", self.dlg_user)
        yes_b.move(150, 50)
        yes_b.clicked.connect(self.yes)
        self.dlg_user.setWindowTitle("Dialog")
        self.dlg_user.show()

    def yes(self):
        self.user.guest()
        self.set_name()
        self.dlg_user.close()

    def no(self):
        self.dlg_user.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = game_window()
    ex.show()
    sys.exit(app.exec_())
