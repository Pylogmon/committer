# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1000, 666)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.commit_box = QComboBox(Form)
        self.commit_box.setObjectName(u"commit_box")

        self.gridLayout_5.addWidget(self.commit_box, 0, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.creator = QLabel(Form)
        self.creator.setObjectName(u"creator")

        self.gridLayout_2.addWidget(self.creator, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.assigned_l = QLabel(Form)
        self.assigned_l.setObjectName(u"assigned_l")

        self.gridLayout_2.addWidget(self.assigned_l, 0, 2, 1, 1)

        self.assigned = QLabel(Form)
        self.assigned.setObjectName(u"assigned")

        self.gridLayout_2.addWidget(self.assigned, 0, 3, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.project = QLabel(Form)
        self.project.setObjectName(u"project")

        self.gridLayout_4.addWidget(self.project, 0, 2, 1, 1)

        self.connect_1 = QLabel(Form)
        self.connect_1.setObjectName(u"connect_1")

        self.gridLayout_4.addWidget(self.connect_1, 0, 1, 1, 1)

        self.connect_2 = QLabel(Form)
        self.connect_2.setObjectName(u"connect_2")

        self.gridLayout_4.addWidget(self.connect_2, 0, 3, 1, 1)

        self.product = QLabel(Form)
        self.product.setObjectName(u"product")

        self.gridLayout_4.addWidget(self.product, 0, 0, 1, 1)

        self.connect_3 = QLabel(Form)
        self.connect_3.setObjectName(u"connect_3")

        self.gridLayout_4.addWidget(self.connect_3, 0, 5, 1, 1)

        self.branch = QLabel(Form)
        self.branch.setObjectName(u"branch")

        self.gridLayout_4.addWidget(self.branch, 0, 6, 1, 1)

        self.module = QLabel(Form)
        self.module.setObjectName(u"module")

        self.gridLayout_4.addWidget(self.module, 0, 4, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.type = QLabel(Form)
        self.type.setObjectName(u"type")

        self.gridLayout_3.addWidget(self.type, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.severity_l = QLabel(Form)
        self.severity_l.setObjectName(u"severity_l")

        self.horizontalLayout_4.addWidget(self.severity_l)

        self.severity = QLabel(Form)
        self.severity.setObjectName(u"severity")

        self.horizontalLayout_4.addWidget(self.severity)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pri_l = QLabel(Form)
        self.pri_l.setObjectName(u"pri_l")

        self.horizontalLayout_3.addWidget(self.pri_l)

        self.pri = QLabel(Form)
        self.pri.setObjectName(u"pri")

        self.horizontalLayout_3.addWidget(self.pri)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.os_l = QLabel(Form)
        self.os_l.setObjectName(u"os_l")

        self.horizontalLayout_2.addWidget(self.os_l)

        self.os = QLabel(Form)
        self.os.setObjectName(u"os")

        self.horizontalLayout_2.addWidget(self.os)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.browser_l = QLabel(Form)
        self.browser_l.setObjectName(u"browser_l")

        self.horizontalLayout.addWidget(self.browser_l)

        self.browser = QLabel(Form)
        self.browser.setObjectName(u"browser")

        self.horizontalLayout.addWidget(self.browser)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 4, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.preview = QTextEdit(Form)
        self.preview.setObjectName(u"preview")
        self.preview.setReadOnly(True)

        self.gridLayout_5.addWidget(self.preview, 3, 0, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.creator.setText(QCoreApplication.translate("Form", u"creator", None))
        self.assigned_l.setText(QCoreApplication.translate("Form", u"\u6307\u6d3e\u7ed9", None))
        self.assigned.setText(QCoreApplication.translate("Form", u"assigned", None))
        self.project.setText(QCoreApplication.translate("Form", u"project", None))
        self.connect_1.setText(QCoreApplication.translate("Form", u"-", None))
        self.connect_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.product.setText(QCoreApplication.translate("Form", u"product", None))
        self.connect_3.setText(QCoreApplication.translate("Form", u"-", None))
        self.branch.setText(QCoreApplication.translate("Form", u"branch", None))
        self.module.setText(QCoreApplication.translate("Form", u"module", None))
        self.type.setText(QCoreApplication.translate("Form", u"type", None))
        self.severity_l.setText(QCoreApplication.translate("Form", u"\u4e25\u91cd\u7a0b\u5ea6\uff1a", None))
        self.severity.setText(QCoreApplication.translate("Form", u"severity", None))
        self.pri_l.setText(QCoreApplication.translate("Form", u"\u4f18\u5148\u7ea7\uff1a", None))
        self.pri.setText(QCoreApplication.translate("Form", u"pri", None))
        self.os_l.setText(QCoreApplication.translate("Form", u"\u64cd\u4f5c\u7cfb\u7edf\uff1a", None))
        self.os.setText(QCoreApplication.translate("Form", u"os", None))
        self.browser_l.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8\u5668\uff1a", None))
        self.browser.setText(QCoreApplication.translate("Form", u"browser", None))
        self.preview.setMarkdown("")
    # retranslateUi

