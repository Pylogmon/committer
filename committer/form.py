from committer.ui.UI_form import Ui_Form
from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QFile


class Form(QWidget, Ui_Form):

    def __init__(self, commit_list):
        super(Form, self).__init__()
        self.commit_list = commit_list
        self.setupUi(self)
        self.init_ui()
        self.init_connect()
        self.show()

    def init_ui(self):
        for i in self.commit_list:
            self.commit_box.addItem(f"{i['commit_id']}: {i['title']}")
        qss_file = QFile(":/qss/mainwindow.qss")
        qss_file.open(QFile.ReadOnly)
        qss = str(qss_file.readAll(), encoding="utf-8")
        self.setStyleSheet(qss)
        self.view_content()

    def init_connect(self):
        self.commit_box.currentTextChanged.connect(self.view_content)

    def view_content(self):
        if len(self.commit_list) == 0:
            return
        commit = self.commit_list[self.commit_box.currentIndex()]
        self.setWindowTitle(f"Commit:{commit['commit_id']}")

        content = QTextDocument()
        text = commit["content"]
        text = eval(repr(text).replace("\\\\", "\\"))
        content.setMarkdown(text, QTextDocument.MarkdownDialectGitHub)
        self.preview.setDocument(content)
