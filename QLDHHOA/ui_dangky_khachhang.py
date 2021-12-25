# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dangky_khachhangdDaEgu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DKKH(object):
    def setupUi(self, DKKH):
        if not DKKH.objectName():
            DKKH.setObjectName(u"DKKH")
        DKKH.resize(379, 226)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DKKH.sizePolicy().hasHeightForWidth())
        DKKH.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(DKKH)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DKKH)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pass_lnedit = QLineEdit(self.frame)
        self.pass_lnedit.setObjectName(u"pass_lnedit")
        self.pass_lnedit.setEchoMode(QLineEdit.Password)
        self.pass_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.pass_lnedit, 6, 1, 1, 2)

        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cancel_btn, 7, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.phone_lnedit = QLineEdit(self.frame)
        self.phone_lnedit.setObjectName(u"phone_lnedit")
        self.phone_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.phone_lnedit, 3, 1, 1, 2)

        self.email_lnedit = QLineEdit(self.frame)
        self.email_lnedit.setObjectName(u"email_lnedit")
        self.email_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.email_lnedit, 5, 1, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.address_lnedit = QLineEdit(self.frame)
        self.address_lnedit.setObjectName(u"address_lnedit")
        self.address_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.address_lnedit, 4, 1, 1, 2)

        self.signup_btn = QPushButton(self.frame)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.signup_btn, 7, 2, 1, 1)

        self.name_lnedit = QLineEdit(self.frame)
        self.name_lnedit.setObjectName(u"name_lnedit")
        self.name_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.name_lnedit, 2, 1, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DKKH)

        QMetaObject.connectSlotsByName(DKKH)
    # setupUi

    def retranslateUi(self, DKKH):
        DKKH.setWindowTitle(QCoreApplication.translate("DKKH", u"\u0110\u0103ng k\u00fd kh\u00e1ch h\u00e0ng", None))
        self.cancel_btn.setText(QCoreApplication.translate("DKKH", u"Hu\u1ef7", None))
        self.label_4.setText(QCoreApplication.translate("DKKH", u"\u0110\u1ecba ch\u1ec9", None))
        self.label_6.setText(QCoreApplication.translate("DKKH", u"M\u1eadt kh\u1ea9u", None))
        self.label_3.setText(QCoreApplication.translate("DKKH", u"\u0110i\u1ec7n tho\u1ea1i", None))
        self.label_5.setText(QCoreApplication.translate("DKKH", u"Email", None))
        self.label.setText(QCoreApplication.translate("DKKH", u"H\u1ecd t\u00ean", None))
        self.signup_btn.setText(QCoreApplication.translate("DKKH", u"\u0110\u0103ng k\u00fd", None))
        self.label_2.setText(QCoreApplication.translate("DKKH", u"\u0110\u0103ng k\u00fd", None))
    # retranslateUi

