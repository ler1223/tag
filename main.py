import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog
from game_window import game_window
from entrance import Entrance
from image_game import image_game
from user import User
from statistic import StaticWidget


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('start.ui', self)
        self.setWindowTitle('Start')
        self.user = User()
        if self.user.get_name() != "Гость":
            self.entrance_b.setText("Выйти из аккаута")
        self.game.clicked.connect(self.start_game)
        self.image_game.clicked.connect(self.start_image_game)
        self.entrance_b.clicked.connect(self.start_entrance)
        self.statistic.clicked.connect(self.start_statistic)
        self.game = None
        self.entrance = None
        self.dlg_user = None

    def start_statistic(self):
        if self.user.get_name() != "Гость":
            self.game = StaticWidget()
            self.game.signal.connect(self.show)
            self.game.show()
            self.hide()

    def start_game(self):
        self.game = game_window()
        self.game.signal.connect(self.show)
        self.game.show()
        self.hide()

    def start_image_game(self):
        self.game = image_game()
        self.game.signal.connect(self.show)
        self.game.show()
        self.hide()

    def start_entrance(self):
        if self.user.get_name() == "Гость":
            self.entrance = Entrance()
            self.entrance.signal.connect(self.rename_entrance)
            self.entrance.show()
            self.hide()
        else:
            self.dialog_user()

    def rename_entrance(self):
        if self.user.get_name() != "Гость":
            self.entrance_b.setText("Выйти из аккаута")
        self.show()

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
        self.dlg_user.accept()
        self.entrance_b.setText("Войти")

    def no(self):
        self.entrance_b.setText("Выйти из аккаута")
        self.dlg_user.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
