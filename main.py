from PyQt5.QtWidgets import *
from AuthWin import Authorization, CreateTable
from settings import STYLE


if __name__ == '__main__':
    import sys
    table = CreateTable()
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    win = Authorization()
    win.setupUI()
    win.show()

    sys.exit(app.exec_())