from committer.utils.standardpath import StandardPath
from committer.ui.UI_form import Ui_Form
from PySide2.QtGui import QTextDocument
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QFile
import requests
import json


class Form(QWidget, Ui_Form):

    def __init__(self, commit_list):
        super(Form, self).__init__()
        self.commit_list = commit_list
        self.login_file = StandardPath.login_file()
        self.server = ""
        self.setupUi(self)
        self.init_ui()
        self.init_connect()
        self.show()

    def init_ui(self):
        # 加载qss样式表
        qss_file = QFile(":/qss/form.qss")
        qss_file.open(QFile.ReadOnly)
        qss = qss_file.readAll().data().decode()
        self.setStyleSheet(qss)
        # 加载commit列表
        for i in self.commit_list:
            self.commit_box.addItem(f"{i['commit_id']}: {i['title']}")
        # 获取服务器地址
        with open(self.login_file, 'r', encoding='utf-8') as f:
            info = json.load(f)
            self.server = info["server"]
        # 加载commit详细信息
        self.view_content()

    def init_connect(self):
        self.commit_box.currentTextChanged.connect(self.view_content)

    def view_content(self):
        if len(self.commit_list) == 0:
            return
        commit = self.commit_list[self.commit_box.currentIndex()]
        self.setWindowTitle(f"Commit:{commit['commit_id']}")
        self.creator.setText(self.get_name("user", commit["creator"]))
        self.assigned.setText(self.get_name("user", commit["assigned"]))
        self.product.setText(self.get_name("product", commit["product_id"]))
        self.project.setText(
            self.get_name("project", commit["project_id"],
                          commit["product_id"]))
        self.module.setText(
            self.get_name("module", commit["module_id"], commit["product_id"],
                          commit["project_id"]))
        self.branch.setText(
            self.get_name("branch", commit["branch_id"], commit["product_id"],
                          commit["project_id"], commit["module_id"]))
        self.type.setText(commit["type"])
        self.severity.setText(str(commit["severity"]))
        self.pri.setText(str(commit["pri"]))
        self.os.setText(commit["os"])
        self.browser.setText(commit["browser"])
        content = QTextDocument()
        text = commit["content"]
        # 去除服务器传递导致的多个\\n
        text = eval(repr(text).replace("\\\\", "\\"))
        content.setMarkdown(text)
        self.preview.setDocument(content)

    # 通过ID获取名称
    def get_name(self, name, id, id1=None, id2=None, id3=None):
        try:
            params = {}
            params[f"{name}_id"] = id
            if id1 is not None:
                params["product_id"] = id1
            if id2 is not None:
                params["project_id"] = id2
            if id3 is not None:
                params["module_id"] = id3
            req = requests.get(self.server + f"/get_{name}",
                               params=params,
                               timeout=5)
            status = json.loads(req.text)["status"]
            data = json.loads(req.text)["data"]
            if status == "Success":
                return data[f"{name}_name"]
            else:
                return "None"
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))
