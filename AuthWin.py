import sqlite3 as sql
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import *
from GameWin import GameWindow
from settings import authCrit_msg, authCrit_msg_2, authInfo_msg


class CreateTable:
    def __init__(self):
        with sql.connect('db.sqlite3') as con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE IF NOT EXISTS "users" (
                "id"	    INTEGER,
                "login"	    TEXT UNIQUE,
                "password"	TEXT DEFAULT 0000,
                PRIMARY KEY("id"))"""
            )
            con.commit()


class Authorization(QWidget):
    def __init__(self):
        super().__init__()
        self.gameWin = GameWindow()
    
    def setupUI(self):
        self.setWindowTitle('Authorization')
        self.setMinimumSize(QSize(200, 130))
        self.setMaximumSize(QSize(200, 130))

        self.centralWidget = QWidget(self)
        self.centralWidget.setGeometry(QRect(0, 0, 200, 130))
        self.centralWidget.setObjectName('MainWindow')

        self.lbl_by = QLabel(self.centralWidget)
        self.lbl_by.setGeometry(QRect(2, 113, 200, 15))
        self.lbl_by.setText('by WoollySensed Software')
        self.lbl_by.setObjectName('MainLbl_by')

        self.led_login = QLineEdit(self.centralWidget)
        self.led_login.setGeometry(QRect(10, 5, 180, 30))
        self.led_login.setPlaceholderText('Enter your login')
        self.led_login.setMaxLength(16)
        self.led_login.setObjectName('MainLed_login')

        self.led_password = QLineEdit(self.centralWidget)
        self.led_password.setGeometry(QRect(10, 45, 180, 30))
        self.led_password.setPlaceholderText('Enter your password')
        self.led_password.setEchoMode(QLineEdit.Password)
        self.led_password.setMaxLength(16)
        self.led_password.setObjectName('MainLed_password')

        self.btn_signUP = QPushButton(self.centralWidget)
        self.btn_signUP.setGeometry(QRect(10, 85, 85, 25))
        self.btn_signUP.setText('Sign up')
        self.btn_signUP.setObjectName('MainBtn_signUP')
        self.btn_signUP.clicked.connect(self.signUP_clicked)

        self.btn_logIN = QPushButton(self.centralWidget)
        self.btn_logIN.setGeometry(QRect(105, 85, 85, 25))
        self.btn_logIN.setText('Log in')
        self.btn_logIN.setObjectName('MainBtn_logIN')
        self.btn_logIN.clicked.connect(self.logIN_clicked)

    # Create new user in DB
    def signUP_clicked(self):
        login = self.led_login.text()
        password = self.led_password.text()
        self.led_login.clear()
        self.led_password.clear()

        if all((login, password)):
            with sql.connect('db.sqlite3') as con:
                cur = con.cursor()
                cur.execute("""SELECT login, password FROM users""")
                all_users = cur.fetchall()
            logins_list = [lg[0] for lg in all_users]
            
            if login not in logins_list:
                with sql.connect('db.sqlite3') as con:
                    cur = con.cursor()
                    cur.execute("""INSERT INTO users (login, password)
                        VALUES (?, ?)""", (login, password,)
                    )
                    con.commit()
                
                self.gameWin.setupUI()
                self.gameWin.show()
                self.hide()
            
            else: QMessageBox.critical(self, 'ERROR', authCrit_msg)
        else: QMessageBox.information(self, 'Attention!', authInfo_msg)
    
    # Checks if the user exists in the DB
    def logIN_clicked(self):
        login = self.led_login.text()
        password = self.led_password.text()
        self.led_login.clear()
        self.led_password.clear()

        if all((login, password)):
            with sql.connect('db.sqlite3') as con:
                cur = con.cursor()
                cur.execute("""SELECT login, password FROM users
                    WHERE (login=? AND password=?)""", (login, password,)
                )
            all_users = cur.fetchone()
            
            if all_users is not None:
                self.gameWin.setupUI()
                self.gameWin.show()
                self.hide()
            
            else: QMessageBox.critical(self, 'ERROR', authCrit_msg_2)
        
        else: QMessageBox.information(self, 'Attention!', authInfo_msg)
