from committer.ui.UI_mainwindow import Ui_MainWindow
from committer.utils.standardpath import StandardPath
from committer.utils.uitools import set_size
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
import requests
import json
import os


class MainWindow(QWidget, Ui_MainWindow):

    logout_success = Signal()

    def __init__(self, login_info):
        super(MainWindow, self).__init__()
        self.login_info = login_info
        self.user_list = None
        self.product_list = None
        self.project_list = None
        self.setupUi(self)
        self.init_ui()
        self.init_connect()

    def init_ui(self):
        self.set_icons()
        self.set_other_ui()
        self.set_boxes()

    def init_connect(self):
        self.logout_btn.clicked.connect(self.logout)
        self.product_box.currentIndexChanged.connect(self.set_project_list)

    def set_icons(self):
        self.setWindowIcon(QIcon(QPixmap(":/icons/committer.png")))
        self.my_commit_btn.setIcon(QIcon(QPixmap(":/icons/my.svg")))
        self.assigned_me_btn.setIcon(QIcon(QPixmap(":/icons/assigned.svg")))
        self.save_to_draft_btn.setIcon(QIcon(QPixmap(":/icons/save.svg")))
        self.save_to_template_btn.setIcon(
            QIcon(QPixmap(":/icons/template.svg")))
        self.commit_btn.setIcon(QIcon(QPixmap(":/icons/commit.svg")))

        label_icon_list = [
            self.user_name_icon, self.product_icon, self.project_icon,
            self.module_icon, self.branch_icon, self.type_icon,
            self.severity_icon, self.pri_icon, self.version_icon, self.os_icon,
            self.browser_icon, self.draft_icon, self.template_icon,
            self.title_icon, self.keywords_icon, self.mailto_icon
        ]
        for i in label_icon_list:
            set_size(i)
        self.user_name_icon.setPixmap(QPixmap(":/icons/user.svg"))
        self.product_icon.setPixmap(QPixmap(":/icons/product.svg"))
        self.project_icon.setPixmap(QPixmap(":/icons/project.svg"))
        self.module_icon.setPixmap(QPixmap(":/icons/module.svg"))
        self.branch_icon.setPixmap(QPixmap(":/icons/branch.svg"))
        self.type_icon.setPixmap(QPixmap(":/icons/type.svg"))
        self.severity_icon.setPixmap(QPixmap(":/icons/severity.svg"))
        self.pri_icon.setPixmap(QPixmap(":/icons/pri.svg"))
        self.version_icon.setPixmap(QPixmap(":/icons/version.svg"))
        self.os_icon.setPixmap(QPixmap(":/icons/os.svg"))
        self.browser_icon.setPixmap(QPixmap(":/icons/browser.svg"))
        self.draft_icon.setPixmap(QPixmap(":/icons/draft.svg"))
        self.template_icon.setPixmap(QPixmap(":/icons/template.svg"))
        self.title_icon.setPixmap(QPixmap(":/icons/title.svg"))
        self.keywords_icon.setPixmap(QPixmap(":/icons/keywords.svg"))
        self.mailto_icon.setPixmap(QPixmap(":/icons/mailto.svg"))

    def set_other_ui(self):
        self.user_name_label.setText(self.login_info["user_name"])
        self.setWindowTitle("Committer")
        self.project_box.setEnabled(False)
        self.module_box.setEnabled(False)
        self.branch_box.setEnabled(False)
        self.assigned_box.setEditable(True)

    def set_boxes(self):
        self.set_local_box()
        self.set_remote_box()

    def set_local_box(self):
        type_list = [
            'baselineedition', 'docerror', 'reliable', 'compatible',
            'modifyimport', 'codeerror', 'config', 'install', 'security',
            'performance', 'standard', 'designdefect', 'system', 'app',
            'desktop', 'kernel', 'newfeature', 'page_display', 'experience',
            'function', 'interface', 'operation_prompt', 'not_involve'
        ]
        for item in type_list:
            self.type_box.addItem(item)
        os_list = [
            'ios', 'android', 'deepin', 'uos', 'all', 'windows', 'others'
        ]
        for item in os_list:
            self.os_box.addItem(item)
        browser_list = ['uos', 'all', 'ie', 'chrome', 'firefox', 'other']
        for item in browser_list:
            self.browser_box.addItem(item)
        for i in range(1, 5):
            self.severity_box.addItem(str(i))
        for i in range(5):
            self.pri_box.addItem(str(i))
        self.get_draft_list()
        self.get_template_list()

    def get_draft_list(self):
        draft_dir = StandardPath.draft_dir()
        StandardPath.check(draft_dir)
        self.draft_box.addItem("None")
        for r, dirs, files in os.walk(draft_dir):
            for i in files:
                if i.endswith('json'):
                    self.draft_box.addItem(i.split('.')[0])
        self.draft_box.setCurrentText("None")

    def get_template_list(self):
        template_dir = StandardPath.template_dir()
        StandardPath.check(template_dir)
        self.template_box.addItem("None")
        for r, dirs, files in os.walk(template_dir):
            for i in files:
                if i.endswith('json'):
                    self.template_box.addItem(i.split('.')[0])
        self.template_box.setCurrentText("None")

    def set_remote_box(self):
        self.set_user_list()
        self.set_product_list()
        self.set_project_list()

    def build_json(self):
        data = {'meta': {}, "auth": {}}
        data['meta']['product'] = self.product_box.currentText()

    def logout(self):
        login_file = StandardPath.login_file()
        self.login_info["user_name"] = ""
        self.login_info["password"] = ""
        with open(login_file, 'w', encoding='utf-8') as f:
            json.dump(self.login_info, f)
        self.logout_success.emit()
        self.close()

    def set_user_list(self):
        try:
            req = requests.get(self.login_info["server"] + "/get_user",
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.user_list = json.loads(req.text)["data"]
            if status == "Success":
                for i in self.user_list:
                    self.assigned_box.addItem(i["user_name"])
            else:
                self.warning("Get User Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def set_product_list(self):
        try:
            req = requests.get(self.login_info["server"] + "/get_product",
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.product_list = json.loads(req.text)["data"]
            if status == "Success":
                for i in self.product_list:
                    self.product_box.addItem(i["product_name"])
                self.project_box.setCurrentIndex(0)
            else:
                self.warning("Get Product Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def set_project_list(self):
        try:
            for i in self.product_list:
                if i["product_name"] == self.product_box.currentText():
                    current_product_id = i["product_id"]
                    break
            req = requests.get(self.login_info["server"] + "/get_project",
                               params={"product_id": current_product_id},
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.project_list = json.loads(req.text)["data"]
            if status == "Success":
                self.project_box.clear()
                for i in self.project_list:
                    self.project_box.addItem(i["project_name"])
                self.project_box.setEnabled(True)
            else:
                self.warning("Get Product Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))
