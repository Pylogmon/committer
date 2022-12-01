from committer.ui.UI_mainwindow import Ui_MainWindow
from PySide2.QtGui import QIcon, QPixmap
from committer.resource import rc_icons
from PySide2.QtWidgets import QWidget


class MainWindow(QWidget, Ui_MainWindow):

    def __init__(self, username):
        super(MainWindow, self).__init__()
        self.user_name = username
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.set_icons()
        self.set_boxes()
        self.set_other_ui()

    def set_icons(self):
        self.setWindowIcon(QIcon(QPixmap(":/icons/committer.png")))
        self.my_commit_btn.setIcon(QIcon(QPixmap(":/icons/my.svg")))
        self.assigned_me_btn.setIcon(QIcon(QPixmap(":/icons/assigned.svg")))
        self.save_to_draft_btn.setIcon(QIcon(QPixmap(":/icons/save.svg")))
        self.save_to_template_btn.setIcon(
            QIcon(QPixmap(":/icons/template.svg")))
        self.commit_btn.setIcon(QIcon(QPixmap(":/icons/commit.svg")))

        size = self.user_name_icon.height()
        self.user_name_icon.setPixmap(
            QPixmap(":/icons/user.svg").scaled(size, size))
        self.product_icon.setPixmap(
            QPixmap(":/icons/product.svg").scaled(size, size))
        self.project_icon.setPixmap(
            QPixmap(":/icons/project.svg").scaled(size, size))
        self.module_icon.setPixmap(
            QPixmap(":/icons/module.svg").scaled(size, size))
        self.branch_icon.setPixmap(
            QPixmap(":/icons/branch.svg").scaled(size, size))
        self.type_icon.setPixmap(
            QPixmap(":/icons/type.svg").scaled(size, size))
        self.severity_icon.setPixmap(
            QPixmap(":/icons/severity.svg").scaled(size, size))
        self.pri_icon.setPixmap(QPixmap(":/icons/pri.svg").scaled(size, size))
        self.version_icon.setPixmap(
            QPixmap(":/icons/version.svg").scaled(size, size))
        self.os_icon.setPixmap(QPixmap(":/icons/os.svg").scaled(size, size))
        self.browser_icon.setPixmap(
            QPixmap(":/icons/browser.svg").scaled(size, size))
        self.draft_icon.setPixmap(
            QPixmap(":/icons/draft.svg").scaled(size, size))
        self.template_icon.setPixmap(
            QPixmap(":/icons/template.svg").scaled(size, size))
        self.title_icon.setPixmap(
            QPixmap(":/icons/title.svg").scaled(size, size))
        self.keywords_icon.setPixmap(
            QPixmap(":/icons/keywords.svg").scaled(size, size))
        self.mailto_icon.setPixmap(
            QPixmap(":/icons/mailto.svg").scaled(size, size))

    def set_boxes(self):
        pass

    def set_other_ui(self):
        self.user_name_label.setText(self.user_name)
        self.setWindowTitle("Committer")
