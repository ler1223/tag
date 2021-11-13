from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from DB import get_statistic
from user import User


class StaticWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('statistic.ui', self)
        self.setWindowTitle('Statistic')
        self.back_btn.clicked.connect(self.close)
        self.set_statistic()

    signal = QtCore.pyqtSignal(str)

    def set_statistic(self):
        restart, win, game = get_statistic()
        user = User()
        name = user.get_name()
        self.name_user.setText(name)
        self.game.setText(str(game))
        self.restart.setText(str(restart))
        self.wins.setText(str(win))

    def sendSignal(self):
        self.signal.emit('1')

    def closeEvent(self, event):
        self.sendSignal()
