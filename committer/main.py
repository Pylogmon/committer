#!/bin/python3
import sys
import os
# 添加path路径，否则有可能会找不到模块
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from committer.mainwindow import MainWindow
from PySide2.QtWidgets import QApplication
from committer.login import Login
from PySide2.QtCore import Slot


class Committer(object):

    def __init__(self):
        self.app = QApplication()
        self.app.setApplicationName("committer")
        self.login_page = None
        self.main_window = None

    def run(self):
        self.login()

    def login(self):
        self.login_page = Login()
        self.login_page.login_success.connect(self.start)

    @Slot(str)
    def start(self, username):
        self.main_window = MainWindow(username)
        self.main_window.show()


if __name__ == "__main__":
    application = Committer()
    application.run()
    sys.exit(application.app.exec_())
