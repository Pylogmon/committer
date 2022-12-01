# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 680)
        self.gridLayout_5 = QGridLayout(MainWindow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.top_line = QGridLayout()
        self.top_line.setObjectName(u"top_line")
        self.my_commit_btn = QPushButton(MainWindow)
        self.my_commit_btn.setObjectName(u"my_commit_btn")

        self.top_line.addWidget(self.my_commit_btn, 0, 0, 1, 1)

        self.assigned_me_btn = QPushButton(MainWindow)
        self.assigned_me_btn.setObjectName(u"assigned_me_btn")

        self.top_line.addWidget(self.assigned_me_btn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.top_line.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.user_name_label = QLabel(MainWindow)
        self.user_name_label.setObjectName(u"user_name_label")

        self.top_line.addWidget(self.user_name_label, 0, 3, 1, 1)


        self.gridLayout_5.addLayout(self.top_line, 0, 0, 1, 1)

        self.meta_line = QGridLayout()
        self.meta_line.setObjectName(u"meta_line")
        self.product_label = QLabel(MainWindow)
        self.product_label.setObjectName(u"product_label")

        self.meta_line.addWidget(self.product_label, 0, 0, 1, 1)

        self.product_box = QComboBox(MainWindow)
        self.product_box.setObjectName(u"product_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.product_box.sizePolicy().hasHeightForWidth())
        self.product_box.setSizePolicy(sizePolicy)
        self.product_box.setLayoutDirection(Qt.LeftToRight)

        self.meta_line.addWidget(self.product_box, 0, 1, 1, 1)

        self.project_label = QLabel(MainWindow)
        self.project_label.setObjectName(u"project_label")

        self.meta_line.addWidget(self.project_label, 0, 2, 1, 1)

        self.project_box = QComboBox(MainWindow)
        self.project_box.setObjectName(u"project_box")
        sizePolicy.setHeightForWidth(self.project_box.sizePolicy().hasHeightForWidth())
        self.project_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.project_box, 0, 3, 1, 1)

        self.module_label = QLabel(MainWindow)
        self.module_label.setObjectName(u"module_label")

        self.meta_line.addWidget(self.module_label, 0, 4, 1, 1)

        self.module_box = QComboBox(MainWindow)
        self.module_box.setObjectName(u"module_box")
        sizePolicy.setHeightForWidth(self.module_box.sizePolicy().hasHeightForWidth())
        self.module_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.module_box, 0, 5, 1, 1)

        self.branch_label = QLabel(MainWindow)
        self.branch_label.setObjectName(u"branch_label")

        self.meta_line.addWidget(self.branch_label, 0, 6, 1, 1)

        self.branch_box = QComboBox(MainWindow)
        self.branch_box.setObjectName(u"branch_box")
        sizePolicy.setHeightForWidth(self.branch_box.sizePolicy().hasHeightForWidth())
        self.branch_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.branch_box, 0, 7, 1, 1)

        self.type_label = QLabel(MainWindow)
        self.type_label.setObjectName(u"type_label")

        self.meta_line.addWidget(self.type_label, 1, 0, 1, 1)

        self.type_box = QComboBox(MainWindow)
        self.type_box.setObjectName(u"type_box")
        sizePolicy.setHeightForWidth(self.type_box.sizePolicy().hasHeightForWidth())
        self.type_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.type_box, 1, 1, 1, 1)

        self.severity_label = QLabel(MainWindow)
        self.severity_label.setObjectName(u"severity_label")

        self.meta_line.addWidget(self.severity_label, 1, 2, 1, 1)

        self.severity_box = QComboBox(MainWindow)
        self.severity_box.setObjectName(u"severity_box")
        sizePolicy.setHeightForWidth(self.severity_box.sizePolicy().hasHeightForWidth())
        self.severity_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.severity_box, 1, 3, 1, 1)

        self.pri_label = QLabel(MainWindow)
        self.pri_label.setObjectName(u"pri_label")

        self.meta_line.addWidget(self.pri_label, 1, 4, 1, 1)

        self.pri_box = QComboBox(MainWindow)
        self.pri_box.setObjectName(u"pri_box")
        sizePolicy.setHeightForWidth(self.pri_box.sizePolicy().hasHeightForWidth())
        self.pri_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.pri_box, 1, 5, 1, 1)

        self.version_label = QLabel(MainWindow)
        self.version_label.setObjectName(u"version_label")

        self.meta_line.addWidget(self.version_label, 1, 6, 1, 1)

        self.version_edit = QLineEdit(MainWindow)
        self.version_edit.setObjectName(u"version_edit")

        self.meta_line.addWidget(self.version_edit, 1, 7, 1, 1)

        self.os_label = QLabel(MainWindow)
        self.os_label.setObjectName(u"os_label")

        self.meta_line.addWidget(self.os_label, 2, 0, 1, 1)

        self.os_box = QComboBox(MainWindow)
        self.os_box.setObjectName(u"os_box")
        sizePolicy.setHeightForWidth(self.os_box.sizePolicy().hasHeightForWidth())
        self.os_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.os_box, 2, 1, 1, 1)

        self.browser_label = QLabel(MainWindow)
        self.browser_label.setObjectName(u"browser_label")

        self.meta_line.addWidget(self.browser_label, 2, 2, 1, 1)

        self.browser_box = QComboBox(MainWindow)
        self.browser_box.setObjectName(u"browser_box")
        sizePolicy.setHeightForWidth(self.browser_box.sizePolicy().hasHeightForWidth())
        self.browser_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.browser_box, 2, 3, 1, 1)

        self.draft_box = QComboBox(MainWindow)
        self.draft_box.setObjectName(u"draft_box")
        sizePolicy.setHeightForWidth(self.draft_box.sizePolicy().hasHeightForWidth())
        self.draft_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.draft_box, 2, 5, 1, 1)

        self.draft_label = QLabel(MainWindow)
        self.draft_label.setObjectName(u"draft_label")

        self.meta_line.addWidget(self.draft_label, 2, 4, 1, 1)

        self.template_label = QLabel(MainWindow)
        self.template_label.setObjectName(u"template_label")

        self.meta_line.addWidget(self.template_label, 2, 6, 1, 1)

        self.template_box = QComboBox(MainWindow)
        self.template_box.setObjectName(u"template_box")
        sizePolicy.setHeightForWidth(self.template_box.sizePolicy().hasHeightForWidth())
        self.template_box.setSizePolicy(sizePolicy)

        self.meta_line.addWidget(self.template_box, 2, 7, 1, 1)


        self.gridLayout_5.addLayout(self.meta_line, 1, 0, 1, 1)

        self.meta_line_2 = QGridLayout()
        self.meta_line_2.setObjectName(u"meta_line_2")
        self.title_label = QLabel(MainWindow)
        self.title_label.setObjectName(u"title_label")

        self.meta_line_2.addWidget(self.title_label, 0, 0, 1, 1)

        self.title_edit = QLineEdit(MainWindow)
        self.title_edit.setObjectName(u"title_edit")

        self.meta_line_2.addWidget(self.title_edit, 0, 1, 1, 1)

        self.keywords_label = QLabel(MainWindow)
        self.keywords_label.setObjectName(u"keywords_label")

        self.meta_line_2.addWidget(self.keywords_label, 1, 0, 1, 1)

        self.keywords_edit = QLineEdit(MainWindow)
        self.keywords_edit.setObjectName(u"keywords_edit")

        self.meta_line_2.addWidget(self.keywords_edit, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.meta_line_2, 2, 0, 1, 1)

        self.main_edit = QPlainTextEdit(MainWindow)
        self.main_edit.setObjectName(u"main_edit")

        self.gridLayout_5.addWidget(self.main_edit, 3, 0, 1, 1)

        self.bottom_line = QGridLayout()
        self.bottom_line.setObjectName(u"bottom_line")
        self.mailto_label = QLabel(MainWindow)
        self.mailto_label.setObjectName(u"mailto_label")

        self.bottom_line.addWidget(self.mailto_label, 0, 0, 1, 1)

        self.mailto_edit = QLineEdit(MainWindow)
        self.mailto_edit.setObjectName(u"mailto_edit")

        self.bottom_line.addWidget(self.mailto_edit, 0, 1, 1, 1)

        self.save_to_draft_btn = QPushButton(MainWindow)
        self.save_to_draft_btn.setObjectName(u"save_to_draft_btn")

        self.bottom_line.addWidget(self.save_to_draft_btn, 0, 2, 1, 1)

        self.save_to_template_btn = QPushButton(MainWindow)
        self.save_to_template_btn.setObjectName(u"save_to_template_btn")

        self.bottom_line.addWidget(self.save_to_template_btn, 0, 3, 1, 1)

        self.commit_btn = QPushButton(MainWindow)
        self.commit_btn.setObjectName(u"commit_btn")

        self.bottom_line.addWidget(self.commit_btn, 0, 4, 1, 1)


        self.gridLayout_5.addLayout(self.bottom_line, 4, 0, 1, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.my_commit_btn.setText(QCoreApplication.translate("MainWindow", u"My Commit", None))
        self.assigned_me_btn.setText(QCoreApplication.translate("MainWindow", u"Assigned Me", None))
        self.user_name_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.product_label.setText(QCoreApplication.translate("MainWindow", u"Product:", None))
        self.project_label.setText(QCoreApplication.translate("MainWindow", u"Project:", None))
        self.module_label.setText(QCoreApplication.translate("MainWindow", u"Module:", None))
        self.branch_label.setText(QCoreApplication.translate("MainWindow", u"Branch:", None))
        self.type_label.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.severity_label.setText(QCoreApplication.translate("MainWindow", u"Severity:", None))
        self.pri_label.setText(QCoreApplication.translate("MainWindow", u"Pri:", None))
        self.version_label.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.os_label.setText(QCoreApplication.translate("MainWindow", u"OS:", None))
        self.browser_label.setText(QCoreApplication.translate("MainWindow", u"Browser:", None))
        self.draft_label.setText(QCoreApplication.translate("MainWindow", u"Draft:", None))
        self.template_label.setText(QCoreApplication.translate("MainWindow", u"Template:", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title:", None))
        self.keywords_label.setText(QCoreApplication.translate("MainWindow", u"Keywords:", None))
        self.mailto_label.setText(QCoreApplication.translate("MainWindow", u"Mailto:", None))
        self.save_to_draft_btn.setText(QCoreApplication.translate("MainWindow", u"Save to Draft", None))
        self.save_to_template_btn.setText(QCoreApplication.translate("MainWindow", u"Save to Template", None))
        self.commit_btn.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
    # retranslateUi

