# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ketnoiqAjnMM.ui'
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
        Form.resize(243, 126)
        Form.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tensv_lnedit = QLineEdit(self.frame)
        self.tensv_lnedit.setObjectName(u"tensv_lnedit")
        self.tensv_lnedit.setStyleSheet(u"")
        self.tensv_lnedit.setReadOnly(False)

        self.gridLayout.addWidget(self.tensv_lnedit, 0, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tendb_lnedit = QLineEdit(self.frame)
        self.tendb_lnedit.setObjectName(u"tendb_lnedit")
        self.tendb_lnedit.setStyleSheet(u"")
        self.tendb_lnedit.setReadOnly(False)

        self.gridLayout.addWidget(self.tendb_lnedit, 1, 1, 1, 1)

        self.ok_btn = QPushButton(self.frame)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.ok_btn, 2, 1, 1, 1, Qt.AlignRight|Qt.AlignTop)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"K\u1ebft n\u1ed1i", None))
        self.label.setText(QCoreApplication.translate("Form", u"T\u00ean server", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"T\u00ean database", None))
        self.ok_btn.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi

