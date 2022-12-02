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
        MainWindow.resize(1105, 680)
        self.gridLayout_5 = QGridLayout(MainWindow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.my_commit_btn = QPushButton(MainWindow)
        self.my_commit_btn.setObjectName(u"my_commit_btn")

        self.gridLayout_2.addWidget(self.my_commit_btn, 0, 0, 1, 1)

        self.assigned_me_btn = QPushButton(MainWindow)
        self.assigned_me_btn.setObjectName(u"assigned_me_btn")

        self.gridLayout_2.addWidget(self.assigned_me_btn, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding,
                                            QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.user_name_icon = QLabel(MainWindow)
        self.user_name_icon.setObjectName(u"user_name_icon")

        self.gridLayout_2.addWidget(self.user_name_icon, 0, 3, 1, 1)

        self.user_name_label = QLabel(MainWindow)
        self.user_name_label.setObjectName(u"user_name_label")

        self.gridLayout_2.addWidget(self.user_name_label, 0, 4, 1, 1)

        self.logout_btn = QPushButton(MainWindow)
        self.logout_btn.setObjectName(u"logout_btn")

        self.gridLayout_2.addWidget(self.logout_btn, 0, 5, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.product_icon = QLabel(MainWindow)
        self.product_icon.setObjectName(u"product_icon")

        self.gridLayout.addWidget(self.product_icon, 0, 0, 1, 1)

        self.product_label = QLabel(MainWindow)
        self.product_label.setObjectName(u"product_label")

        self.gridLayout.addWidget(self.product_label, 0, 1, 1, 1)

        self.product_box = QComboBox(MainWindow)
        self.product_box.setObjectName(u"product_box")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.product_box.sizePolicy().hasHeightForWidth())
        self.product_box.setSizePolicy(sizePolicy)
        self.product_box.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.product_box, 0, 2, 1, 1)

        self.project_icon = QLabel(MainWindow)
        self.project_icon.setObjectName(u"project_icon")

        self.gridLayout.addWidget(self.project_icon, 0, 3, 1, 1)

        self.project_label = QLabel(MainWindow)
        self.project_label.setObjectName(u"project_label")

        self.gridLayout.addWidget(self.project_label, 0, 4, 1, 1)

        self.project_box = QComboBox(MainWindow)
        self.project_box.setObjectName(u"project_box")
        sizePolicy.setHeightForWidth(
            self.project_box.sizePolicy().hasHeightForWidth())
        self.project_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.project_box, 0, 5, 1, 1)

        self.module_icon = QLabel(MainWindow)
        self.module_icon.setObjectName(u"module_icon")

        self.gridLayout.addWidget(self.module_icon, 0, 6, 1, 1)

        self.module_label = QLabel(MainWindow)
        self.module_label.setObjectName(u"module_label")

        self.gridLayout.addWidget(self.module_label, 0, 7, 1, 1)

        self.module_box = QComboBox(MainWindow)
        self.module_box.setObjectName(u"module_box")
        sizePolicy.setHeightForWidth(
            self.module_box.sizePolicy().hasHeightForWidth())
        self.module_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.module_box, 0, 8, 1, 1)

        self.branch_icon = QLabel(MainWindow)
        self.branch_icon.setObjectName(u"branch_icon")

        self.gridLayout.addWidget(self.branch_icon, 0, 9, 1, 1)

        self.branch_label = QLabel(MainWindow)
        self.branch_label.setObjectName(u"branch_label")

        self.gridLayout.addWidget(self.branch_label, 0, 10, 1, 1)

        self.branch_box = QComboBox(MainWindow)
        self.branch_box.setObjectName(u"branch_box")
        sizePolicy.setHeightForWidth(
            self.branch_box.sizePolicy().hasHeightForWidth())
        self.branch_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.branch_box, 0, 11, 1, 1)

        self.type_icon = QLabel(MainWindow)
        self.type_icon.setObjectName(u"type_icon")

        self.gridLayout.addWidget(self.type_icon, 1, 0, 1, 1)

        self.type_label = QLabel(MainWindow)
        self.type_label.setObjectName(u"type_label")

        self.gridLayout.addWidget(self.type_label, 1, 1, 1, 1)

        self.type_box = QComboBox(MainWindow)
        self.type_box.setObjectName(u"type_box")
        sizePolicy.setHeightForWidth(
            self.type_box.sizePolicy().hasHeightForWidth())
        self.type_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.type_box, 1, 2, 1, 1)

        self.severity_icon = QLabel(MainWindow)
        self.severity_icon.setObjectName(u"severity_icon")

        self.gridLayout.addWidget(self.severity_icon, 1, 3, 1, 1)

        self.severity_label = QLabel(MainWindow)
        self.severity_label.setObjectName(u"severity_label")

        self.gridLayout.addWidget(self.severity_label, 1, 4, 1, 1)

        self.severity_box = QComboBox(MainWindow)
        self.severity_box.setObjectName(u"severity_box")
        sizePolicy.setHeightForWidth(
            self.severity_box.sizePolicy().hasHeightForWidth())
        self.severity_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.severity_box, 1, 5, 1, 1)

        self.pri_icon = QLabel(MainWindow)
        self.pri_icon.setObjectName(u"pri_icon")

        self.gridLayout.addWidget(self.pri_icon, 1, 6, 1, 1)

        self.pri_label = QLabel(MainWindow)
        self.pri_label.setObjectName(u"pri_label")

        self.gridLayout.addWidget(self.pri_label, 1, 7, 1, 1)

        self.pri_box = QComboBox(MainWindow)
        self.pri_box.setObjectName(u"pri_box")
        sizePolicy.setHeightForWidth(
            self.pri_box.sizePolicy().hasHeightForWidth())
        self.pri_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.pri_box, 1, 8, 1, 1)

        self.version_icon = QLabel(MainWindow)
        self.version_icon.setObjectName(u"version_icon")

        self.gridLayout.addWidget(self.version_icon, 1, 9, 1, 1)

        self.assigned_label = QLabel(MainWindow)
        self.assigned_label.setObjectName(u"assigned_label")

        self.gridLayout.addWidget(self.assigned_label, 1, 10, 1, 1)

        self.assigned_box = QComboBox(MainWindow)
        self.assigned_box.setObjectName(u"assigned_box")

        self.gridLayout.addWidget(self.assigned_box, 1, 11, 1, 1)

        self.os_icon = QLabel(MainWindow)
        self.os_icon.setObjectName(u"os_icon")

        self.gridLayout.addWidget(self.os_icon, 2, 0, 1, 1)

        self.os_label = QLabel(MainWindow)
        self.os_label.setObjectName(u"os_label")

        self.gridLayout.addWidget(self.os_label, 2, 1, 1, 1)

        self.os_box = QComboBox(MainWindow)
        self.os_box.setObjectName(u"os_box")
        sizePolicy.setHeightForWidth(
            self.os_box.sizePolicy().hasHeightForWidth())
        self.os_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.os_box, 2, 2, 1, 1)

        self.browser_icon = QLabel(MainWindow)
        self.browser_icon.setObjectName(u"browser_icon")

        self.gridLayout.addWidget(self.browser_icon, 2, 3, 1, 1)

        self.browser_label = QLabel(MainWindow)
        self.browser_label.setObjectName(u"browser_label")

        self.gridLayout.addWidget(self.browser_label, 2, 4, 1, 1)

        self.browser_box = QComboBox(MainWindow)
        self.browser_box.setObjectName(u"browser_box")
        sizePolicy.setHeightForWidth(
            self.browser_box.sizePolicy().hasHeightForWidth())
        self.browser_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.browser_box, 2, 5, 1, 1)

        self.draft_icon = QLabel(MainWindow)
        self.draft_icon.setObjectName(u"draft_icon")

        self.gridLayout.addWidget(self.draft_icon, 2, 6, 1, 1)

        self.draft_label = QLabel(MainWindow)
        self.draft_label.setObjectName(u"draft_label")

        self.gridLayout.addWidget(self.draft_label, 2, 7, 1, 1)

        self.draft_box = QComboBox(MainWindow)
        self.draft_box.setObjectName(u"draft_box")
        sizePolicy.setHeightForWidth(
            self.draft_box.sizePolicy().hasHeightForWidth())
        self.draft_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.draft_box, 2, 8, 1, 1)

        self.template_icon = QLabel(MainWindow)
        self.template_icon.setObjectName(u"template_icon")

        self.gridLayout.addWidget(self.template_icon, 2, 9, 1, 1)

        self.template_label = QLabel(MainWindow)
        self.template_label.setObjectName(u"template_label")

        self.gridLayout.addWidget(self.template_label, 2, 10, 1, 1)

        self.template_box = QComboBox(MainWindow)
        self.template_box.setObjectName(u"template_box")
        sizePolicy.setHeightForWidth(
            self.template_box.sizePolicy().hasHeightForWidth())
        self.template_box.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.template_box, 2, 11, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.title_icon = QLabel(MainWindow)
        self.title_icon.setObjectName(u"title_icon")

        self.gridLayout_3.addWidget(self.title_icon, 0, 0, 1, 1)

        self.title_label = QLabel(MainWindow)
        self.title_label.setObjectName(u"title_label")

        self.gridLayout_3.addWidget(self.title_label, 0, 1, 1, 1)

        self.title_edit = QLineEdit(MainWindow)
        self.title_edit.setObjectName(u"title_edit")

        self.gridLayout_3.addWidget(self.title_edit, 0, 2, 1, 1)

        self.keywords_icon = QLabel(MainWindow)
        self.keywords_icon.setObjectName(u"keywords_icon")

        self.gridLayout_3.addWidget(self.keywords_icon, 1, 0, 1, 1)

        self.keywords_label = QLabel(MainWindow)
        self.keywords_label.setObjectName(u"keywords_label")

        self.gridLayout_3.addWidget(self.keywords_label, 1, 1, 1, 1)

        self.keywords_edit = QLineEdit(MainWindow)
        self.keywords_edit.setObjectName(u"keywords_edit")

        self.gridLayout_3.addWidget(self.keywords_edit, 1, 2, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.main_edit = QPlainTextEdit(MainWindow)
        self.main_edit.setObjectName(u"main_edit")

        self.gridLayout_5.addWidget(self.main_edit, 3, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mailto_icon = QLabel(MainWindow)
        self.mailto_icon.setObjectName(u"mailto_icon")

        self.gridLayout_4.addWidget(self.mailto_icon, 0, 0, 1, 1)

        self.mailto_edit = QLineEdit(MainWindow)
        self.mailto_edit.setObjectName(u"mailto_edit")

        self.gridLayout_4.addWidget(self.mailto_edit, 0, 1, 1, 1)

        self.save_to_draft_btn = QPushButton(MainWindow)
        self.save_to_draft_btn.setObjectName(u"save_to_draft_btn")

        self.gridLayout_4.addWidget(self.save_to_draft_btn, 0, 2, 1, 1)

        self.save_to_template_btn = QPushButton(MainWindow)
        self.save_to_template_btn.setObjectName(u"save_to_template_btn")

        self.gridLayout_4.addWidget(self.save_to_template_btn, 0, 3, 1, 1)

        self.commit_btn = QPushButton(MainWindow)
        self.commit_btn.setObjectName(u"commit_btn")

        self.gridLayout_4.addWidget(self.commit_btn, 0, 4, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 4, 0, 1, 1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"Form", None))
        #if QT_CONFIG(tooltip)
        self.my_commit_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u6211\u7684\u63d0\u4ea4 \u67e5\u770b\u6211\u63d0\u4ea4\u7684\u5de5\u5355",
                None))
        #endif // QT_CONFIG(tooltip)
        self.my_commit_btn.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u6211\u7684\u63d0\u4ea4", None))
        #if QT_CONFIG(tooltip)
        self.assigned_me_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u5f85\u5904\u7406 \u67e5\u770b\u6307\u6d3e\u7ed9\u6211\u7684\u5de5\u5355",
                None))
        #endif // QT_CONFIG(tooltip)
        self.assigned_me_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u5f85\u5904\u7406",
                                       None))
        self.user_name_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.user_name_label.setText(
            QCoreApplication.translate("MainWindow", u"Username", None))
        self.logout_btn.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u9000\u51fa\u767b\u5f55", None))
        self.product_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.product_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u6240\u5c5e\u4ea7\u54c1", None))
        #if QT_CONFIG(tooltip)
        self.product_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u6240\u5c5e\u4ea7\u54c1 <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.product_box.setPlaceholderText("")
        self.project_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.project_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u6240\u5c5e\u9879\u76ee", None))
        #if QT_CONFIG(tooltip)
        self.project_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u6240\u5c5e\u9879\u76ee <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.module_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.module_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u6240\u5c5e\u6a21\u5757", None))
        #if QT_CONFIG(tooltip)
        self.module_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"\u6240\u5c5e\u6a21\u5757 \u9009\u586b", None))
        #endif // QT_CONFIG(tooltip)
        self.branch_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.branch_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u6240\u5c5e\u5206\u652f", None))
        #if QT_CONFIG(tooltip)
        self.branch_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"\u6240\u5c5e\u5206\u652f \u9009\u586b", None))
        #endif // QT_CONFIG(tooltip)
        self.type_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.type_label.setText(
            QCoreApplication.translate("MainWindow", u"Bug\u7c7b\u578b", None))
        #if QT_CONFIG(tooltip)
        self.type_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>Bug\u7c7b\u578b <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.severity_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.severity_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u4e25\u91cd\u7a0b\u5ea6", None))
        #if QT_CONFIG(tooltip)
        self.severity_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u4e25\u91cd\u7a0b\u5ea6 <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.pri_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.pri_label.setText(
            QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u7ea7",
                                       None))
        #if QT_CONFIG(tooltip)
        self.pri_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u4f18\u5148\u7ea7 <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.version_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.assigned_label.setText(
            QCoreApplication.translate("MainWindow", u"\u6307\u6d3e\u7ed9",
                                       None))
        #if QT_CONFIG(tooltip)
        self.assigned_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u6307\u6d3e\u7ed9 <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.os_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.os_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u64cd\u4f5c\u7cfb\u7edf", None))
        #if QT_CONFIG(tooltip)
        self.os_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow", u"\u64cd\u4f5c\u7cfb\u7edf \u9009\u586b", None))
        #endif // QT_CONFIG(tooltip)
        self.browser_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.browser_label.setText(
            QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8\u5668",
                                       None))
        #if QT_CONFIG(tooltip)
        self.browser_box.setToolTip(
            QCoreApplication.translate("MainWindow",
                                       u"\u6d4f\u89c8\u5668 \u9009\u586b",
                                       None))
        #endif // QT_CONFIG(tooltip)
        self.draft_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.draft_label.setText(
            QCoreApplication.translate("MainWindow", u"\u8349\u7a3f\u7bb1",
                                       None))
        #if QT_CONFIG(tooltip)
        self.draft_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u8349\u7a3f\u7bb1 \u9009\u62e9\u4fdd\u5b58\u7684\u8349\u7a3f\u7ee7\u7eed\u7f16\u8f91",
                None))
        #endif // QT_CONFIG(tooltip)
        self.template_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.template_label.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u9009\u62e9\u6a21\u677f", None))
        #if QT_CONFIG(tooltip)
        self.template_box.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u9009\u62e9\u6a21\u677f \u590d\u7528\u6a21\u677f\u5feb\u901f\u7f16\u8f91",
                None))
        #endif // QT_CONFIG(tooltip)
        self.title_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.title_label.setText(
            QCoreApplication.translate("MainWindow", u"\u6807\u9898", None))
        #if QT_CONFIG(tooltip)
        self.title_edit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u6807\u9898 <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.title_edit.setText("")
        self.title_edit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow", u"\u6807\u9898\u4e0d\u80fd\u4e3a\u7a7a", None))
        self.keywords_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        self.keywords_label.setText(
            QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd",
                                       None))
        #if QT_CONFIG(tooltip)
        self.keywords_edit.setToolTip(
            QCoreApplication.translate("MainWindow",
                                       u"\u5173\u952e\u8bcd \u9009\u586b",
                                       None))
        #endif // QT_CONFIG(tooltip)
        self.keywords_edit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u591a\u4e2a\u5173\u952e\u8bcd\u7528;\u9694\u5f00", None))
        #if QT_CONFIG(tooltip)
        self.main_edit.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"<html><head/><body><p>\u4e3b\u8981\u5185\u5bb9 \u63cf\u8ff0\u590d\u73b0\u6b65\u9aa4 \u5b9a\u4f4d\u601d\u8def <span style=\" font-weight:600; color:#ff0000;\">\u5fc5\u586b</span></p></body></html>",
                None))
        #endif // QT_CONFIG(tooltip)
        self.mailto_icon.setText(
            QCoreApplication.translate("MainWindow", u"A", None))
        #if QT_CONFIG(tooltip)
        self.mailto_edit.setToolTip(
            QCoreApplication.translate("MainWindow",
                                       u"\u6284\u9001 \u9009\u586b", None))
        #endif // QT_CONFIG(tooltip)
        self.mailto_edit.setPlaceholderText(
            QCoreApplication.translate(
                "MainWindow",
                u"\u6284\u9001,\u591a\u4e2a\u90ae\u7bb1\u7528;\u9694\u5f00",
                None))
        #if QT_CONFIG(tooltip)
        self.save_to_draft_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u5c06\u5f53\u524d\u7f16\u8f91\u5185\u5bb9\u4fdd\u5b58\u4e3a\u8349\u7a3f",
                None))
        #endif // QT_CONFIG(tooltip)
        self.save_to_draft_btn.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u4fdd\u5b58\u4e3a\u8349\u7a3f",
                                       None))
        #if QT_CONFIG(tooltip)
        self.save_to_template_btn.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                u"\u5c06\u5f53\u524d\u5185\u5bb9\u4f5c\u4e3a\u6a21\u677f\u4fdd\u5b58",
                None))
        #endif // QT_CONFIG(tooltip)
        self.save_to_template_btn.setText(
            QCoreApplication.translate("MainWindow",
                                       u"\u4fdd\u5b58\u4e3a\u6a21\u677f",
                                       None))
        self.commit_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4", None))

    # retranslateUi
