import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from DB import entrance, registring
from game_window import game_window
from user import User


class Entrance(QMainWindow):
    def __init__(self):
        super().__init__()
        self.entrance_window()
        self.game = None

    signal = QtCore.pyqtSignal(str)

    def entrance(self):
        email = self.email_edit.text()
        password = self.password_edit.text()
        if email == "" and password == "":
            pass
        else:
            if entrance(email, password):
                print("--------------Yes--------------")
                user = User()
                user.entrance_user(email)
                self.close()
            else:
                pass

    def register_window(self):
        uic.loadUi('register.ui', self)
        self.setWindowTitle('Register')
        self.register_2.clicked.connect(self.register)
        self.back_btn.clicked.connect(self.entrance_window)

    def register(self):
        name = self.name_edit.text()
        password = self.password_edit.text()
        password2 = self.password_edit_2.text()
        email = self.email_edit.text()
        if password2 == password and password != "":
            registring(name, email, password)
            self.entrance_window()
        else:
            pass

    def sendSignal(self):
        self.signal.emit('1')

    def closeEvent(self, event):
        self.sendSignal()

    def game_window(self):
        self.game = game_window()
        self.game.signal.connect(self.show)
        self.game.show()
        self.hide()

    def entrance_window(self):
        uic.loadUi('entrance.ui', self)
        self.setWindowTitle('Entrance')
        self.entrance_b.clicked.connect(self.entrance)
        self.register_2.clicked.connect(self.register_window)
        self.back_btn.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Entrance()
    ex.show()
    sys.exit(app.exec_())
