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
        qss_file = QFile(":/qss/form.qss")
        qss_file.open(QFile.ReadOnly)
        qss = qss_file.readAll().data().decode()
        self.setStyleSheet(qss)

        for i in self.commit_list:
            self.commit_box.addItem(f"{i['commit_id']}: {i['title']}")
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
