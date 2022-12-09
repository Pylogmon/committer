from PySide2.QtCore import QStandardPaths
from os.path import join, exists
from os import makedirs


class StandardPath:

    def __init__(self):
        pass

    # config文件夹
    @staticmethod
    def config_dir() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/')

    # 草稿文件夹
    @staticmethod
    def draft_dir() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/drafts/')

    # 模板文件夹
    @staticmethod
    def template_dir() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/templates/')

    # 登陆信息文件
    @staticmethod
    def login_file() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/login.json')

    @staticmethod
    def check(path):
        if not exists(path):
            makedirs(path)
