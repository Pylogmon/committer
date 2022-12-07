from committer.ui.UI_form import Ui_Form
from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QWidget


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
        self.view_content()

    def init_connect(self):
        self.commit_box.currentTextChanged.connect(self.view_content)

    def view_content(self):
        commit = self.commit_list[self.commit_box.currentIndex()]
        self.setWindowTitle(f"Commit:{commit['commit_id']}")
        self.title.setText(commit["title"])

        content = QTextDocument()
        text = commit["content"]
        text = eval(repr(text).replace("\\\\", "\\"))
        content.setMarkdown(text, QTextDocument.MarkdownDialectGitHub)
        self.preview.setDocument(content)
