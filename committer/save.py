from PySide2.QtWidgets import QWidget, QLineEdit


class Save(QWidget):

    def __init__(self, type):
        super(Save, self).__init__()
        self.setWindowTitle(f"Save to {type}")
        self.init_ui()
        self.init_connect()
        self.show()

    def init_ui(self):
        self.name_edit = QLineEdit(self)
        self.name_edit.setPlaceholderText("输入保存名称")

    def init_connect(self):
        pass
