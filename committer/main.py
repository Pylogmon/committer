#!/bin/python3
import sys
import os
# 添加path路径，否则有可能会找不到模块
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from committer.mainwindow import MainWindow
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from committer.login import Login
from PySide2.QtCore import Slot


class Committer(object):

    def __init__(self):
        self.app = QApplication()
        self.app.setApplicationName("committer")
        self.app.setWindowIcon(QIcon(QPixmap(":/icons/committer.png")))
        self.login_page = None
        self.main_window = None

    def run(self):
        self.login()

    @Slot()
    def login(self):
        self.login_page = Login()
        self.login_page.login_success.connect(self.start)

    @Slot(dict)
    def start(self, login_info):
        self.main_window = MainWindow(login_info)
        self.main_window.show()
        self.main_window.logout_success.connect(self.login)


if __name__ == "__main__":
    application = Committer()
    application.run()
    sys.exit(application.app.exec_())
