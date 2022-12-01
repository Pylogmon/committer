from committer.ui.UI_mainwindow import Ui_MainWindow
from PySide2.QtWidgets import QWidget


class MainWindow(QWidget, Ui_MainWindow):

    def __init__(self, username):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.user_name_label.setText(username)
