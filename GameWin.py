import random as r
from PyQt5.QtCore import QRect, QSize, Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowMinMaxButtonsHint)
        self.randomNum = r.randint(1, 30)
        self.tryCount = 6
    
    def setupUI(self):
        self.setWindowTitle('Guess Number')
        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(400, 200))
        self.setObjectName('GameWindow')

        self.centralWidget = QWidget(self)
        self.centralWidget.setGeometry(QRect(0, 0, 400, 200))
        self.centralWidget.setObjectName('GameWindow')

        self.lbl_tryCount = QLabel(self.centralWidget)
        self.lbl_tryCount.setGeometry(QRect(5, 165, 80, 30))
        self.lbl_tryCount.setText('Try Count: 6')
        self.lbl_tryCount.setObjectName('GameLbl_tryCount')

        self.lbl_title = QLabel(self.centralWidget)
        self.lbl_title.setGeometry(QRect(0, 20, 400, 30))
        self.lbl_title.setText('Guess my number (1-30)')
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setObjectName('GameLbl_title')

        self.led_userNum = QLineEdit(self.centralWidget)
        self.led_userNum.setGeometry(QRect(75, 60, 250, 30))
        self.led_userNum.setPlaceholderText(
            'What number could this be?'
        )
        self.led_userNum.setObjectName('GameLed_userNum')

        self.intValidator = QIntValidator(self)
        self.intValidator.setRange(1, 30)

        self.led_userNum.setValidator(self.intValidator)

        self.btn_tryGuess = QPushButton(self.centralWidget)
        self.btn_tryGuess.setGeometry(QRect(75, 100, 250, 25))
        self.btn_tryGuess.setText('TRY TO GUESS')
        self.btn_tryGuess.clicked.connect(self.tryGuess_clicked)
        self.btn_tryGuess.setObjectName('GameBtn_tryGuess')

        self.btn_restart = QPushButton(self.centralWidget)
        self.btn_restart.setGeometry(QRect(75, 100, 250, 25))
        self.btn_restart.setText('RESTART GAME')
        self.btn_restart.clicked.connect(self.restart_clicked)
        self.btn_restart.setObjectName('GameBtn_restart')
        self.btn_restart.hide()

        self.btn_exit = QPushButton(self.centralWidget)
        self.btn_exit.setGeometry(QRect(385, 0, 20, 20))
        self.btn_exit.setText('x')
        self.btn_exit.clicked.connect(self.exit_clicked)
        self.btn_exit.setObjectName('GameBtn_exit')
    
    def tryGuess_clicked(self):
        if self.led_userNum.text() != '':
            self.tryCount -= 1
            if self.tryCount >= 0:
                userNum = int(self.led_userNum.text())
                self.led_userNum.clear()

                if userNum < self.randomNum:
                    self.lbl_title.setText(f'{userNum} less than my')
                    self.lbl_tryCount.setText(f'Try Count: {self.tryCount}')
                
                elif userNum > self.randomNum:
                    self.lbl_title.setText(f'{userNum} more than my')
                    self.lbl_tryCount.setText(f'Try Count: {self.tryCount}')
                
                elif userNum == self.randomNum:
                    self.lbl_title.setText(
                        f'Great! You guessed my number, it\'s really {self.randomNum}'
                    )
                    self.led_userNum.setPlaceholderText(
                        'You win! Maybe play again?'
                    )
                    self.lbl_tryCount.setText(f'Try Count: {self.tryCount}')
                    self.btn_tryGuess.destroy()
                    self.btn_restart.show()
        
            else:
                self.lbl_title.setText(
                    f'You lose! My number it\'s {self.randomNum}'
                )
                self.lbl_tryCount.setText(f'Try Count: {self.tryCount}')
                self.btn_tryGuess.destroy()
                self.btn_restart.show()

    def restart_clicked(self):
        self.gameWin = GameWindow()
        self.gameWin.setupUI()
        self.gameWin.show()
        self.destroy()
    
    def exit_clicked(self):
        import sys
        sys.exit()
