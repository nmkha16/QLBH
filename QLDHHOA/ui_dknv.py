# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dknvtfIySn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DKNV(object):
    def setupUi(self, DKNV):
        if not DKNV.objectName():
            DKNV.setObjectName(u"DKNV")
        DKNV.resize(347, 242)
        self.horizontalLayout = QHBoxLayout(DKNV)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(DKNV)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.signup_btn = QPushButton(self.frame)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.signup_btn, 9, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.address_lnedit = QLineEdit(self.frame)
        self.address_lnedit.setObjectName(u"address_lnedit")
        self.address_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.address_lnedit, 4, 1, 1, 2)

        self.phone_lnedit = QLineEdit(self.frame)
        self.phone_lnedit.setObjectName(u"phone_lnedit")
        self.phone_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.phone_lnedit, 3, 1, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1, Qt.AlignHCenter)

        self.id_lnedit = QLineEdit(self.frame)
        self.id_lnedit.setObjectName(u"id_lnedit")
        self.id_lnedit.setEchoMode(QLineEdit.Normal)
        self.id_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.id_lnedit, 6, 1, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.name_lnedit = QLineEdit(self.frame)
        self.name_lnedit.setObjectName(u"name_lnedit")
        self.name_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.name_lnedit, 2, 1, 1, 2)

        self.email_lnedit = QLineEdit(self.frame)
        self.email_lnedit.setObjectName(u"email_lnedit")
        self.email_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.email_lnedit, 5, 1, 1, 2)

        self.cancel_btn = QPushButton(self.frame)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cancel_btn, 9, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.birth_lnedit = QLineEdit(self.frame)
        self.birth_lnedit.setObjectName(u"birth_lnedit")
        self.birth_lnedit.setInputMethodHints(Qt.ImhDate)
        self.birth_lnedit.setEchoMode(QLineEdit.Normal)
        self.birth_lnedit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.birth_lnedit, 7, 1, 1, 2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(DKNV)

        QMetaObject.connectSlotsByName(DKNV)
    # setupUi

    def retranslateUi(self, DKNV):
        DKNV.setWindowTitle(QCoreApplication.translate("DKNV", u"Form \u0111\u0103ng k\u00fd nh\u00e2n vi\u00ean", None))
        self.label_3.setText(QCoreApplication.translate("DKNV", u"\u0110i\u1ec7n tho\u1ea1i", None))
        self.signup_btn.setText(QCoreApplication.translate("DKNV", u"\u0110\u0103ng k\u00fd", None))
        self.label_4.setText(QCoreApplication.translate("DKNV", u"\u0110\u1ecba ch\u1ec9", None))
        self.label.setText(QCoreApplication.translate("DKNV", u"H\u1ecd t\u00ean", None))
        self.label_2.setText(QCoreApplication.translate("DKNV", u"\u0110\u0103ng k\u00fd", None))
        self.label_5.setText(QCoreApplication.translate("DKNV", u"Email", None))
        self.cancel_btn.setText(QCoreApplication.translate("DKNV", u"Hu\u1ef7", None))
        self.label_6.setText(QCoreApplication.translate("DKNV", u"CMND", None))
        self.label_7.setText(QCoreApplication.translate("DKNV", u"Ng\u00e0y sinh", None))
    # retranslateUi

