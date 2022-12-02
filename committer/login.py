from committer.utils.standardpath import StandardPath
from PySide2.QtWidgets import QWidget, QMessageBox
from requests.exceptions import ConnectionError
from requests.exceptions import MissingSchema
from requests.exceptions import InvalidSchema
from committer.utils.uitools import set_size
from committer.ui.UI_login import Ui_Login
from PySide2.QtCore import Signal, QTimer
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from requests import post
import json
import os


class Login(QWidget, Ui_Login):

    login_success = Signal(str)

    def __init__(self):
        super(Login, self).__init__()
        self.login_file = StandardPath.login_file()
        self.login_info = {}
        self.setupUi(self)
        self.init_ui()
        self.init_connect()
        self.show()

    # 初始化信号槽
    def init_connect(self):
        QTimer.singleShot(2000, self.auto_login)
        self.login_btn.clicked.connect(self.manual_login)

    # 自动登陆
    def auto_login(self):
        if os.path.exists(self.login_file):
            with open(self.login_file, 'r', encoding='utf-8') as f:
                self.login_info = json.load(f)
            self.login()

    # 手动登陆
    def manual_login(self):
        if self.check():
            self.get_data()
            self.login()

    def login(self):
        # 构造请求参数
        params = {
            "username": self.login_info["user_name"],
            "password": self.login_info["password"]
        }
        try:
            req = post(self.login_info["server"] + "/login",
                       params=params,
                       timeout=5)
            status = json.loads(req.text)["status"]
            message = json.loads(req.text)["message"]
            if status == "Success":
                self.success()
            else:
                self.warning("Login Failed", message)
        except ConnectionError as e:
            self.warning("ConnectionError", str(e))
        except TimeoutError as e:
            self.warning("TimeoutError", str(e))
        except MissingSchema as e:
            self.warning("MissingSchema", str(e))
        except InvalidSchema as e:
            self.warning("InvalidSchema", str(e))

    # 登陆成功
    def success(self):
        # 检查配置文件夹是否存在
        StandardPath.check(StandardPath.config_dir())
        with open(self.login_file, 'w', encoding='utf-8') as f:
            json.dump(self.login_info, f)
        # 发射登陆成功信号
        self.login_success.emit(self.login_info["user_name"])
        self.close()

    # 从界面获取输入数据
    def get_data(self):
        self.login_info["server"] = self.server_edit.text()
        self.login_info["user_name"] = self.user_name_edit.text()
        self.login_info["password"] = self.password_edit.text()

    # 检查输入是否为空
    def check(self):
        if len(self.server_edit.text()) == 0:
            self.server_edit.setFocus()
            return False
        if len(self.user_name_edit.text()) == 0:
            self.user_name_edit.setFocus()
            return False
        if len(self.password_edit.text()) == 0:
            self.password_edit.setFocus()
            return False
        return True

    # 显示警告信息
    def warning(self, title, message):
        QMessageBox.warning(self, title, message)

    def init_ui(self):
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon(QPixmap(":/icons/committer.png")))
        set_size(self.user_name_icon)
        set_size(self.server_icon)
        set_size(self.password_icon)
        self.user_name_icon.setPixmap(QPixmap(":/icons/user.svg"))
        self.server_icon.setPixmap(QPixmap(":/icons/browser.svg"))
        self.password_icon.setPixmap(QPixmap(":/icons/password.svg"))
