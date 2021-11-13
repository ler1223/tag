import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication
from user import User
from game_window import game_window
from image import image
from choice_image_window import main


class image_game(game_window):
    def __init__(self):
        super().__init__()
        uic.loadUi('image_game.ui', self)
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
        self.choice_image.clicked.connect(self.choice_image_btn)
        self.back_btn.clicked.connect(self.close)
        self.user = User()
        self.image_name = self.user.get_name_image()
        self.width, self.height = image(self.image_name)
        self.set_defoult()
        self.restart_count = 0
        self.win_count = 0
        self.game_count = 0
        self.flag_game = False
        self.restart.clicked.connect(self.restart_b)
        self.name.clicked.connect(self.dialog_user_show)
        self.set_name()
        self.zero_button = self.pushButton_16
        self.zero_button_text = ""
        self.arr_button = [[self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4],
                           [self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8],
                           [self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12],
                           [self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16]]
        self.arr_image = []
        self.res_arr_image = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.completion_arr()

    def button(self):
        action = self.sender()
        if not self.flag_game:
            self.game_count += 1
            self.flag_game = True
        if action == self.zero_button:
            pass
        else:
            x, y = self.indexing(action)
            x_zero, y_zero = self.indexing(self.zero_button)
            if (x == x_zero + 1 and y == y_zero) or (x == x_zero - 1 and y == y_zero) \
                    or (y == y_zero - 1 and x == x_zero) or (y == y_zero + 1 and x == x_zero):
                self.arr_image[x * 4 + y], self.arr_image[x_zero * 4 + y_zero] \
                    = self.arr_image[x_zero * 4 + y_zero], self.arr_image[x * 4 + y]
                self.set_icon(self.zero_button, self.arr_image[x_zero * 4 + y_zero])
                self.set_icon(action, self.arr_image[x * 4 + y])
                self.zero_button = action
        if self.res_arr_image == self.arr_image:
            print(
                "--------------------------------------------YOU WIN------------------------------------------------")
            self.win_count += 1
            self.dialog()

    def completion_arr(self):
        self.arr_image = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        random.shuffle(self.arr_image)
        self.arr_image.append(15)
        self.zero_button = self.pushButton_16
        for x in range(4):
            for y in range(4):
                index = self.arr_image[x * 4 + y]
                name_image = 'image' + str(index) + '.png'
                icon = QIcon(name_image)
                self.arr_button[x][y].setText("")
                self.arr_button[x][y].setIcon(icon)
                self.arr_button[x][y].setIconSize(QSize(95, 95))
        self.flag_game = False

    def set_icon(self, button, index):
        name_image = 'image' + str(index) + '.png'
        icon = QIcon(name_image)
        button.setIcon(icon)
        button.setIconSize(QSize(95, 95))

    def set_defoult(self):
        pixmap = QPixmap(self.image_name)
        self.image.setPixmap(pixmap)

    def indexing(self, button):
        for x in range(len(self.arr_button)):
            for y in range(len(self.arr_button[x])):
                if self.arr_button[x][y] == button:
                    return x, y

    def choice_image_btn(self):
        self.game = main()
        self.game.signal.connect(self.reboot)
        self.game.show()
        self.hide()

    def reboot(self):
        self.image_name = self.user.get_name_image()
        self.set_defoult()
        image(self.image_name)
        self.completion_arr()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = image_game()
    ex.show()
    sys.exit(app.exec_())
