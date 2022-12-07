from committer.ui.UI_mainwindow import Ui_MainWindow
from committer.utils.standardpath import StandardPath
from PySide2.QtWidgets import QWidget, QMessageBox, QPlainTextEdit
from committer.utils.uitools import set_size
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from PySide2.QtCore import Signal
import requests
import json
import os


class MainWindow(QWidget, Ui_MainWindow):

    logout_success = Signal()

    def __init__(self, login_info):
        super(MainWindow, self).__init__()
        self.login_info = login_info
        self.draft_dir = StandardPath.draft_dir()
        self.template_dir = StandardPath.template_dir()
        self.user_list = None
        self.product_list = None
        self.project_list = None
        self.module_list = None
        self.branch_list = None
        self.setupUi(self)  # 初始化ui
        self.init_ui()  # 设置ui界面
        self.init_connect()  # 初始化信号槽

    def init_ui(self):
        self.set_icons()  # 设置图标
        self.set_other_ui()  # 设置其他ui选项
        self.set_boxes()  # 设置下拉菜单

    def init_connect(self):
        self.logout_btn.clicked.connect(self.logout)
        self.product_box.currentIndexChanged.connect(self.set_project_list)
        self.project_box.currentIndexChanged.connect(self.set_module_list)
        self.module_box.currentIndexChanged.connect(self.set_branch_list)
        self.save_to_draft_btn.clicked.connect(self.save_to_draft)
        self.save_to_template_btn.clicked.connect(self.save_to_template)
        self.commit_btn.clicked.connect(self.commit)
        self.draft_box.currentTextChanged.connect(self.load_draft)
        self.template_box.currentTextChanged.connect(self.load_template)

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
        self.set_draft_list()
        self.set_template_list()

    def set_draft_list(self):
        StandardPath.check(self.draft_dir)
        self.draft_box.clear()
        self.draft_box.addItem("None")
        for r, dirs, files in os.walk(self.draft_dir):
            for i in files:
                if i.endswith('json'):
                    self.draft_box.addItem(i.split('.')[0])
        self.draft_box.setCurrentText("None")

    def set_template_list(self):
        StandardPath.check(self.template_dir)
        self.template_box.clear()
        self.template_box.addItem("None")
        for r, dirs, files in os.walk(self.template_dir):
            for i in files:
                if i.endswith('json'):
                    self.template_box.addItem(i.split('.')[0])
        self.template_box.setCurrentText("None")

    def set_remote_box(self):
        self.set_user_list()
        self.set_product_list()
        self.set_project_list()
        self.set_module_list()
        self.set_branch_list()

    def build_json(self):
        if not self.check_data():
            return False
        data = {}
        data["user_name"] = self.login_info["user_name"]
        data["password"] = self.login_info["password"]
        data["title"] = self.title_edit.text()
        if len(self.keywords_edit.text()) > 0:
            data["keywords"] = self.keywords_edit.text()
        data["product_id"] = self.get_id(self.product_list)
        data["project_id"] = self.get_id(self.project_list)
        if self.module_box.isEnabled():
            data["module_id"] = self.get_id(self.module_list)
        if self.branch_box.isEnabled():
            data["branch_id"] = self.get_id(self.branch_list)
        data["type"] = self.type_box.currentText()
        data["severity"] = int(self.severity_box.currentText())
        data["pri"] = int(self.pri_box.currentText())
        data["assigned"] = self.get_id(self.user_list)
        data["os"] = self.os_box.currentText()
        data["browser"] = self.browser_box.currentText()
        data["content"] = self.main_edit.toPlainText()
        data["creator"] = self.get_my_id()
        return data

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
            else:
                self.warning("Get Product Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def set_project_list(self):
        if not self.product_box.isEnabled():
            return
        current_product_id = self.get_id(self.product_list)
        try:
            req = requests.get(self.login_info["server"] + "/get_project",
                               params={"product_id": current_product_id},
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.project_list = json.loads(req.text)["data"]
            if status == "Success":
                self.project_box.setEnabled(True)
                self.project_box.clear()
                for i in self.project_list:
                    self.project_box.addItem(i["project_name"])
            else:
                self.project_box.setEnabled(False)
                self.project_box.clear()
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def set_module_list(self):
        if not self.project_box.isEnabled():
            self.module_box.clear()
            self.module_box.setEnabled(False)
            return
        current_product_id = self.get_id(self.product_list)
        current_project_id = self.get_id(self.project_list)
        try:
            req = requests.get(self.login_info["server"] + "/get_module",
                               params={
                                   "product_id": current_product_id,
                                   "project_id": current_project_id
                               },
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.module_list = json.loads(req.text)["data"]
            if status == "Success":
                self.module_box.setEnabled(True)
                self.module_box.clear()
                for i in self.module_list:
                    self.module_box.addItem(i["module_name"])
            else:
                self.module_box.setEnabled(False)
                self.module_box.clear()
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def set_branch_list(self):
        if not self.module_box.isEnabled():
            self.branch_box.clear()
            self.branch_box.setEnabled(False)
            return
        current_product_id = self.get_id(self.product_list)
        current_project_id = self.get_id(self.project_list)
        current_module_id = self.get_id(self.module_list)

        try:
            req = requests.get(self.login_info["server"] + "/get_branch",
                               params={
                                   "product_id": current_product_id,
                                   "project_id": current_project_id,
                                   "module_id": current_module_id
                               },
                               timeout=5)
            status = json.loads(req.text)["status"]
            self.branch_list = json.loads(req.text)["data"]
            if status == "Success":
                self.branch_box.clear()
                for i in self.branch_list:
                    self.branch_box.addItem(i["branch_name"])
                self.branch_box.setEnabled(True)
            else:
                self.branch_box.clear()
                self.branch_box.setEnabled(False)
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    def save_to_draft(self):
        data = self.build_json()
        if data is False:
            return
        data["product_name"] = self.product_box.currentText()
        data["project_name"] = self.project_box.currentText()
        data["module_name"] = self.module_box.currentText()
        data["branch_name"] = self.branch_box.currentText()
        data["assigned_name"] = self.assigned_box.currentText()
        draft_file = os.path.join(self.draft_dir, data["title"] + ".json")
        if os.path.exists(draft_file):
            result = QMessageBox.warning(
                self, "文件已存在", f"{data['title']+'.json'}已存在，确定要覆盖吗？",
                QMessageBox.Yes, QMessageBox.Cancel)
            if result == 4194304:
                return
        with open(draft_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        self.info("保存成功", f"{data['title']}已保存为草稿")
        self.set_draft_list()

    def save_to_template(self):
        data = self.build_json()
        if data is False:
            return
        data["product_name"] = self.product_box.currentText()
        data["project_name"] = self.project_box.currentText()
        data["module_name"] = self.module_box.currentText()
        data["branch_name"] = self.branch_box.currentText()
        data["assigned_name"] = self.assigned_box.currentText()
        template_file = os.path.join(self.template_dir,
                                     data["title"] + ".json")
        if os.path.exists(template_file):
            result = QMessageBox.warning(
                self, "文件已存在", f"{data['title']+'.json'}已存在，确定要覆盖吗？",
                QMessageBox.Yes, QMessageBox.Cancel)
            if result == 4194304:
                return
        with open(template_file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        self.info("保存成功", f"{data['title']}已保存为模板")
        self.set_template_list()

    # 提交表单
    def commit(self):
        data = self.build_json()
        if data is False:
            return
        try:
            req = requests.post(self.login_info["server"] + "/commit",
                                data=data,
                                timeout=5)
            status = json.loads(req.text)["status"]
            res = json.loads(req.text)["data"]
            if status == "Success":
                self.info("提交成功", f"提交成功,CommitID:{res['commit_id']}")
            else:
                self.warning("提交失败", f"{res['message']}")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 将名称转换为ID
    def get_id(self, list):
        if len(list) > 0:
            if "product_name" in list[0].keys():
                type = "product"
                box = self.product_box
            if "project_name" in list[0].keys():
                type = "project"
                box = self.project_box
            if "module_name" in list[0].keys():
                type = "module"
                box = self.module_box
            if "branch_name" in list[0].keys():
                type = "branch"
                box = self.branch_box
            if "user_name" in list[0].keys():
                type = "user"
                box = self.assigned_box
            for i in list:
                if i[f"{type}_name"] == box.currentText():
                    return i[f"{type}_id"]

    # 获取我的ID
    def get_my_id(self):
        for i in self.user_list:
            if i["user_name"] == self.login_info["user_name"]:
                return i["user_id"]

    # 检查数据是否非空
    def check_data(self):
        if len(self.title_edit.text()) == 0:
            self.title_edit.setFocus()
            return False
        return True

    def load_draft(self):
        draft_file = self.draft_box.currentText()
        if draft_file == "None":
            return
        draft_file = os.path.join(self.draft_dir, draft_file + ".json")
        self.load_json(draft_file)

    def load_template(self):
        template_file = self.template_box.currentText()
        if template_file == "None":
            return
        template_file = os.path.join(self.template_dir,
                                     template_file + ".json")
        self.load_json(template_file)

    def load_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.product_box.setCurrentText(data["product_name"])
        self.project_box.setCurrentText(data["project_name"])
        if len(data["module_name"]) > 0:
            self.module_box.setCurrentText(data["module_name"])
        if len(data["branch_name"]) > 0:
            self.branch_box.setCurrentText(data["branch_name"])
        self.assigned_box.setCurrentText(data["assigned_name"])
        self.type_box.setCurrentText(data["type"])
        self.severity_box.setCurrentText(str(data["severity"]))
        self.pri_box.setCurrentText(str(data["pri"]))
        self.os_box.setCurrentText(data["os"])
        self.browser_box.setCurrentText(data["browser"])
        self.title_edit.setText(data["title"])
        if "keywords" in data.keys():
            self.keywords_edit.setText(data["keywords"])
        else:
            self.keywords_edit.clear()
        self.main_edit.setPlainText(data["content"])

    def warning(self, title, message):
        QMessageBox.warning(self, title, message)

    def info(self, title, message):
        QMessageBox.information(self, title, message)
