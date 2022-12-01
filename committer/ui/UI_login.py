# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(400, 250)
        self.gridLayout_2 = QGridLayout(Login)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.up = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.up, 0, 1, 1, 1)

        self.left = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.left, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.server_label = QLabel(Login)
        self.server_label.setObjectName(u"server_label")

        self.gridLayout.addWidget(self.server_label, 0, 0, 1, 1)

        self.server_edit = QLineEdit(Login)
        self.server_edit.setObjectName(u"server_edit")
        self.server_edit.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.server_edit, 0, 1, 1, 1)

        self.user_name_label = QLabel(Login)
        self.user_name_label.setObjectName(u"user_name_label")

        self.gridLayout.addWidget(self.user_name_label, 1, 0, 1, 1)

        self.user_name_edit = QLineEdit(Login)
        self.user_name_edit.setObjectName(u"user_name_edit")
        self.user_name_edit.setMinimumSize(QSize(250, 0))

        self.gridLayout.addWidget(self.user_name_edit, 1, 1, 1, 1)

        self.password_label = QLabel(Login)
        self.password_label.setObjectName(u"password_label")

        self.gridLayout.addWidget(self.password_label, 2, 0, 1, 1)

        self.password_edit = QLineEdit(Login)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setMinimumSize(QSize(250, 0))
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.password_edit, 2, 1, 1, 1)

        self.login_btn = QPushButton(Login)
        self.login_btn.setObjectName(u"login_btn")

        self.gridLayout.addWidget(self.login_btn, 3, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.right = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.right, 1, 2, 1, 1)

        self.down = QSpacerItem(20, 46, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.down, 2, 1, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.server_label.setText(QCoreApplication.translate("Login", u"Server:", None))
        self.server_edit.setText(QCoreApplication.translate("Login", u"http://127.0.0.1:9000", None))
        self.user_name_label.setText(QCoreApplication.translate("Login", u"UserName:", None))
        self.user_name_edit.setText(QCoreApplication.translate("Login", u"LiMin", None))
        self.password_label.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.password_edit.setText(QCoreApplication.translate("Login", u"666666", None))
        self.login_btn.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi

