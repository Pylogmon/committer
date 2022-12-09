from committer.ui.UI_mainwindow import Ui_MainWindow
from committer.utils.standardpath import StandardPath
from PySide2.QtWidgets import QWidget, QMessageBox
from committer.utils.uitools import set_size
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCore import Signal, QFile
from committer.resource import resource
from committer.form import Form
from time import sleep
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
        self.user_list = {}
        self.product_list = {}
        self.project_list = {}
        self.module_list = {}
        self.branch_list = {}
        self.my_commit_list = []
        self.assigned_me_list = []
        self.view_page = None
        self.setupUi(self)  # 初始化ui
        self.init_ui()  # 设置ui界面
        self.init_connect()  # 初始化信号槽

    def init_ui(self):
        self.set_icons()  # 设置图标
        self.set_other_ui()  # 设置其他ui选项
        self.set_boxes()  # 设置下拉菜单

    def init_connect(self):
        # 退出登陆
        self.logout_btn.clicked.connect(self.logout)
        # 更新project列表
        self.product_box.currentIndexChanged.connect(self.set_project_box)
        # 更新module列表
        self.project_box.currentIndexChanged.connect(self.set_module_box)
        # 更新branch列表
        self.module_box.currentIndexChanged.connect(self.set_branch_box)
        # 保存为草稿
        self.save_to_draft_btn.clicked.connect(self.save_to_draft)
        # 保存为模板
        self.save_to_template_btn.clicked.connect(self.save_to_template)
        # 提交表单
        self.commit_btn.clicked.connect(self.commit)
        # 加载草稿
        self.draft_box.currentTextChanged.connect(self.load_draft)
        # 加载模板
        self.template_box.currentTextChanged.connect(self.load_template)
        # 查看我的提交
        self.my_commit_btn.clicked.connect(self.view_my_commit)
        # 查看待处理
        self.assigned_me_btn.clicked.connect(self.view_assigned_me)

    # 退出登陆
    def logout(self):
        login_file = StandardPath.login_file()
        self.login_info["user_name"] = ""
        self.login_info["password"] = ""
        with open(login_file, 'w', encoding='utf-8') as f:
            json.dump(self.login_info, f)
        self.logout_success.emit()
        self.close()

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
        qss_file = QFile(":/qss/mainwindow.qss")
        qss_file.open(QFile.ReadOnly)
        qss = qss_file.readAll().data().decode()
        self.setStyleSheet(qss)

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

    # 设置草稿下拉选项
    def set_draft_list(self):
        StandardPath.check(self.draft_dir)
        self.draft_box.clear()
        self.draft_box.addItem("None")
        for r, dirs, files in os.walk(self.draft_dir):
            for i in files:
                if i.endswith('json'):
                    self.draft_box.addItem(i.split('.')[0])
        self.draft_box.setCurrentText("None")

    # 设置模板下拉选项
    def set_template_list(self):
        StandardPath.check(self.template_dir)
        self.template_box.clear()
        self.template_box.addItem("None")
        for r, dirs, files in os.walk(self.template_dir):
            for i in files:
                if i.endswith('json'):
                    self.template_box.addItem(i.split('.')[0])
        self.template_box.setCurrentText("None")

    # 设置需要远程获取的下拉选项
    def set_remote_box(self):
        self.set_assigned_box()
        self.set_product_box()
        self.set_project_box()
        self.set_module_box()
        self.set_branch_box()
        self.set_my_commit_btn()
        self.set_assigned_me_btn()

    # 设置指派下拉菜单 /get_user
    def set_assigned_box(self):
        try:
            req = requests.get(self.login_info["server"] + "/get_user",
                               timeout=5)
            status = json.loads(req.text)["status"]
            if status == "Success":
                data = json.loads(req.text)["data"]
                for i in data:
                    self.user_list[i["user_name"]] = i["user_id"]
                    self.assigned_box.addItem(i["user_name"])
            else:
                self.warning("Get User Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 获取产品列表 /get_product
    def set_product_box(self):
        try:
            req = requests.get(self.login_info["server"] + "/get_product",
                               timeout=5)
            status = json.loads(req.text)["status"]
            if status == "Success":
                data = json.loads(req.text)["data"]
                for i in data:
                    self.product_list[i["product_name"]] = i["product_id"]
                    self.product_box.addItem(i["product_name"])
            else:
                self.warning("Get Product Fail", "")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 获取项目列表 /get_project
    def set_project_box(self):
        if not self.product_box.count():
            return
        current_product_id = self.product_list[self.product_box.currentText()]
        try:
            req = requests.get(self.login_info["server"] + "/get_project",
                               params={"product_id": current_product_id},
                               timeout=5)
            status = json.loads(req.text)["status"]
            if status == "Success":
                data = json.loads(req.text)["data"]
                self.project_box.setEnabled(True)
                self.project_box.clear()
                for i in data:
                    self.project_list[i["project_name"]] = i["project_id"]
                    self.project_box.addItem(i["project_name"])
            else:
                self.project_box.setEnabled(False)
                self.project_box.clear()
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 获取模块列表 /get_module
    def set_module_box(self):
        if not self.project_box.count():
            self.module_box.clear()
            self.module_box.setEnabled(False)
            return
        current_product_id = self.product_list[self.product_box.currentText()]
        current_project_id = self.project_list[self.project_box.currentText()]
        try:
            req = requests.get(self.login_info["server"] + "/get_module",
                               params={
                                   "product_id": current_product_id,
                                   "project_id": current_project_id
                               },
                               timeout=5)
            status = json.loads(req.text)["status"]
            if status == "Success":
                data = json.loads(req.text)["data"]
                self.module_box.setEnabled(True)
                self.module_box.clear()
                for i in data:
                    self.module_list[i["module_name"]] = i["module_id"]
                    self.module_box.addItem(i["module_name"])
            else:
                self.module_box.setEnabled(False)
                self.module_box.clear()
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 获取分支列表 /get_branch
    def set_branch_box(self):
        if not self.module_box.count():
            self.branch_box.clear()
            self.branch_box.setEnabled(False)
            return
        current_product_id = self.product_list[self.product_box.currentText()]
        current_project_id = self.project_list[self.project_box.currentText()]
        current_module_id = self.module_list[self.module_box.currentText()]
        try:
            req = requests.get(self.login_info["server"] + "/get_branch",
                               params={
                                   "product_id": current_product_id,
                                   "project_id": current_project_id,
                                   "module_id": current_module_id
                               },
                               timeout=5)
            status = json.loads(req.text)["status"]
            if status == "Success":
                data = json.loads(req.text)["data"]
                self.branch_box.setEnabled(True)
                self.branch_box.clear()
                for i in data:
                    self.branch_list[i["branch_name"]] = i["branch_id"]
                    self.branch_box.addItem(i["branch_name"])
            else:
                self.branch_box.clear()
                self.branch_box.setEnabled(False)
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 设置我的提交角标
    def set_my_commit_btn(self):
        try:
            req = requests.get(
                self.login_info["server"] + "/get_commit",
                params={
                    "creator": self.user_list[self.login_info["user_name"]],
                },
                timeout=5)
            self.my_commit_list = json.loads(req.text)
            num = len(self.my_commit_list)
            if num > 0:
                self.my_commit_btn.setText(f"我的提交({num})")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 设置待处理角标
    def set_assigned_me_btn(self):
        try:
            req = requests.get(
                self.login_info["server"] + "/get_commit",
                params={
                    "assigned": self.user_list[self.login_info["user_name"]],
                },
                timeout=5)
            self.assigned_me_list = json.loads(req.text)
            num = len(self.assigned_me_list)
            if num > 0:
                self.assigned_me_btn.setText(f"待处理({num})")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 保存到草稿
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

    # 保存到模板
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

    # 从界面数据构造json
    def build_json(self):
        if not self.check_data():
            return False
        data = {}
        data["user_name"] = self.login_info["user_name"]
        data["password"] = self.login_info["password"]
        data["title"] = self.title_edit.text()
        data["keywords"] = self.keywords_edit.text()
        data["product_id"] = self.product_list[self.product_box.currentText()]
        data["project_id"] = self.project_list[self.project_box.currentText()]
        if self.module_box.isEnabled():
            data["module_id"] = self.module_list[self.module_box.currentText()]
        if self.branch_box.isEnabled():
            data["branch_id"] = self.branch_list[self.branch_box.currentText()]
        data["type"] = self.type_box.currentText()
        data["severity"] = int(self.severity_box.currentText())
        data["pri"] = int(self.pri_box.currentText())
        data["assigned"] = self.user_list[self.assigned_box.currentText()]
        data["os"] = self.os_box.currentText()
        data["browser"] = self.browser_box.currentText()
        data["content"] = self.main_edit.toPlainText()
        data["creator"] = self.user_list[data["user_name"]]
        data["mailto"] = self.mailto_edit.text()
        return data

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
                self.set_my_commit_btn()
                self.info("提交成功", f"提交成功,CommitID:{res['commit_id']}")
            else:
                self.warning("提交失败", f"{res['message']}")
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))

    # 检查数据是否非空
    def check_data(self):
        if len(self.title_edit.text()) == 0:
            self.title_edit.setFocus()
            return False
        return True

    # 加载草稿到界面
    def load_draft(self):
        draft_file = self.draft_box.currentText()
        if draft_file == "None" or draft_file == "":
            return
        draft_file = os.path.join(self.draft_dir, draft_file + ".json")
        self.load_json(draft_file)

    # 加载模板到界面
    def load_template(self):
        template_file = self.template_box.currentText()
        if template_file == "None" or template_file == "":
            return
        template_file = os.path.join(self.template_dir,
                                     template_file + ".json")
        self.load_json(template_file)

    # 加载草稿/模板json文件
    def load_json(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        index = self.product_box.findText(data["product_name"])
        if index >= 0:
            self.product_box.setCurrentIndex(index)
        else:
            self.warning("错误", "草稿/模板错误，找不到对应的产品名称")
            return
        # 尝试两秒，超时认为出错
        for i in range(20):
            index = self.project_box.findText(data["project_name"])
            if index >= 0:
                self.project_box.setCurrentIndex(index)
                break
            else:
                sleep(0.1)
        else:
            self.warning("错误", "草稿/模板错误，找不到对应的项目名称")
            return
        if len(data["module_name"]) > 0:
            for i in range(20):
                index = self.module_box.findText(data["module_name"])
                if index >= 0:
                    self.module_box.setCurrentIndex(index)
                    break
                else:
                    sleep(0.1)
            else:
                self.warning("错误", "草稿/模板错误，找不到对应的模块名称")
                return
        if len(data["branch_name"]) > 0:
            for i in range(20):
                index = self.branch_box.findText(data["branch_name"])
                if index >= 0:
                    self.branch_box.setCurrentIndex(index)
                    break
                else:
                    sleep(0.1)
            else:
                self.warning("错误", "草稿/模板错误，找不到对应的分支名称")
                return
        index = self.assigned_box.findText(data["assigned_name"])
        if index >= 0:
            self.assigned_box.setCurrentIndex(index)
        else:
            self.warning("错误", "草稿/模板错误，找不到对应的用户名称")
            return
        self.type_box.setCurrentText(data["type"])
        self.severity_box.setCurrentText(str(data["severity"]))
        self.pri_box.setCurrentText(str(data["pri"]))
        self.os_box.setCurrentText(data["os"])
        self.browser_box.setCurrentText(data["browser"])
        self.title_edit.setText(data["title"])
        self.keywords_edit.setText(data["keywords"])
        self.main_edit.setPlainText(data["content"])
        self.info("成功", "草稿/模板加载成功")

    # 查看我的提交
    def view_my_commit(self):
        self.view_page = Form(self.my_commit_list)

    # 查看待处理
    def view_assigned_me(self):
        self.view_page = Form(self.assigned_me_list)

    def warning(self, title, message):
        QMessageBox.warning(self, title, message)

    def info(self, title, message):
        QMessageBox.information(self, title, message)
