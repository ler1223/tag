import os
import sys
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from user import User


class QCustomQWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QCustomQWidget, self).__init__(parent)

        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.name_image = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.name_image)

        self.allQHBoxLayout = QtWidgets.QHBoxLayout()
        self.iconQLabel = QtWidgets.QLabel()

        self.iconQLabel.setMinimumSize(80, 80)  # +++
        self.iconQLabel.setMaximumSize(80, 80)  # +++

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQHBoxLayout)

    def setNameImage(self, text):
        self.name_image.setText(text)

    def setIcon(self, imagePath):
        self.iconQLabel.setPixmap(QtGui.QPixmap(imagePath).scaled(120, 120))

    def getNameImage(self):
        return self.name_image.text()


class listWidgets(QtWidgets.QListWidget):
    def __init__(self):
        super(listWidgets, self).__init__()

        # +++
        self.resize(420, 300)
        self.setFrameShape(self.NoFrame)  # Нет границы
        # self.setFlow(self.LeftToRight)  # Слева направо
        self.setWrapping(True)  # Эти 3 комбинации могут достичь того же эффекта, что и FlowLayout
        self.setResizeMode(self.Adjust)
        arr = self.arr()
        self.arr_widget = []
        self.arr_name_image = []

        for index, name_image, icon in arr:
            myQCustomQWidget = QCustomQWidget()
            myQCustomQWidget.setNameImage(name_image)
            myQCustomQWidget.setIcon(icon)
            myQListWidgetItem = QtWidgets.QListWidgetItem(self)
            myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())
            self.arr_widget.append(myQListWidgetItem)
            self.arr_name_image.append(icon)
            self.addItem(myQListWidgetItem)
            self.setItemWidget(myQListWidgetItem, myQCustomQWidget)

        self.itemClicked.connect(self.onClicked)

    def onClicked(self, item):
        user = User()
        name_image = self.arr_name_image[self.arr_widget.index(item)]
        user.set_name_image(name_image)

    def arr(self):
        arr = []
        for root, dirs, files in os.walk("default_image", topdown=False):
            index = 1
            for name in files:
                arr.append((str(index), name, os.path.join(root, name)))
                index += 1
        return arr


class main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('choice_window.ui', self)
        list = listWidgets()
        self.name_image = ""
        self.listLayout.addWidget(list)
        self.setWindowTitle('choice_window')
        self.pushButton.clicked.connect(self.btn_choice)
        self.pushButton_2.clicked.connect(self.ready_btn)
        self.game = None

    signal = QtCore.pyqtSignal(str)

    def btn_choice(self):
        fname = \
            QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                        'Картинка (*.png);;Картинка (*.png);;Все файлы (*)')[0]
        if fname != "":
            user = User()
            user.set_name_image(fname)
        self.close()

    def sendSignal(self):
        self.signal.emit('1')

    def closeEvent(self, event):
        self.sendSignal()

    def ready_btn(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = main()
    ex.show()
    sys.exit(app.exec_())
