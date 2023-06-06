STYLE = """
    QWidget#MainWindow{
        background: #C04000;
        font-family: Courier;
    }
    QLineEdit#MainLed_login{
        background: #FAF9F6;
        color: #000000;
        font-size: 16px;
        padding: 1px;
        border: 2px solid #000000;
        border-radius: 8px;
    }
    QLineEdit#MainLed_password{
        background: #FAF9F6;
        color: #000000;
        font-size: 16px;
        padding: 1px;
        border: 2px solid #000000;
        border-radius: 8px;
    }
    QPushButton#MainBtn_signUP{
        background: #000000;
        padding: 1px;
        color: #FAF9F6;
        border-radius: 10px;
        font: bold;
    }
    QPushButton#MainBtn_signUP:hover{
        background: #353935;
        color: #FAF9F6;
    }
    QPushButton#MainBtn_logIN{
        background: #000000;
        padding: 1px;
        color: #FAF9F6;
        border-radius: 10px;
        font: bold;
    }
    QPushButton#MainBtn_logIN:hover{
        background: #353935;
        color: #FAF9F6;
    }
    QLabel#MainLbl_by{
        color: #FAF9F6;
    }

    QWidget#GameWindow{
        background: #C04000;
        font-family: Courier;
    }
    QLineEdit#GameLed_userNum{
        background: #FAF9F6;
        color: #000000;
        font-size: 16px;
        padding: 1px;
        border: 2px solid #000000;
        border-radius: 8px;
    }
    QLabel#GameLbl_title{
        background: #C04000;
        color: #FAF9F6;
        font-size: 16px;
    }
    QLabel#GameLbl_tryCount{
        background: #C04000;
        color: #FAF9F6;
        font-size: 14px;
    }
    QPushButton#GameBtn_tryGuess{
        background: #000000;
        padding: 1px;
        color: #FAF9F6;
        border-radius: 10px;
        font: bold;
    }
    QPushButton#GameBtn_tryGuess:hover{
        background: #353935;
        color: #FAF9F6;
    }
    QPushButton#GameBtn_restart{
        background: #000000;
        padding: 1px;
        color: #FAF9F6;
        border-radius: 10px;
        font: bold;
    }
    QPushButton#GameBtn_restart:hover{
        background: #353935;
        color: #FAF9F6;
    }
    QPushButton#GameBtn_exit{
        background: #C04000;
        padding: 1px;
        color: #FAF9F6;
        border-radius: 5px;
    }
    QPushButton#GameBtn_exit:hover{
        background: #FAF9F6;
        color: #C04000;
    }
"""

authCrit_msg = """You cannot use this login because it
is already taken by another user.
"""

authCrit_msg_2 = """You have entered incorrect login 
information, please double-check it.
"""

authInfo_msg = """You did not provide all the required 
information, please double-check it.
"""
