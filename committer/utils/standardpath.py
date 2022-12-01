from PySide2.QtCore import QStandardPaths
from os.path import join, exists
from os import makedirs


class StandardPath:

    def __init__(self):
        pass

    @staticmethod
    def config_dir() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/')

    @staticmethod
    def login_file() -> str:
        config = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        return join(config, 'committer/login.json')

    @staticmethod
    def check(path):
        if not exists(path):
            makedirs(path)
