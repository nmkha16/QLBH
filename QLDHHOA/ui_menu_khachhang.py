# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_khachhangCzsDWA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Menu_KH(object):
    def setupUi(self, Menu_KH):
        if not Menu_KH.objectName():
            Menu_KH.setObjectName(u"Menu_KH")
        Menu_KH.resize(306, 147)
        self.verticalLayout = QVBoxLayout(Menu_KH)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Menu_KH)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 1, 1, 1)

        self.account_btn = QPushButton(self.groupBox)
        self.account_btn.setObjectName(u"account_btn")

        self.gridLayout.addWidget(self.account_btn, 1, 0, 1, 1)

        self.signout_btn = QPushButton(self.groupBox)
        self.signout_btn.setObjectName(u"signout_btn")

        self.gridLayout.addWidget(self.signout_btn, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(Menu_KH)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.orderhistory_btn = QPushButton(self.frame)
        self.orderhistory_btn.setObjectName(u"orderhistory_btn")

        self.horizontalLayout.addWidget(self.orderhistory_btn, 0, Qt.AlignTop)

        self.product_btn = QPushButton(self.frame)
        self.product_btn.setObjectName(u"product_btn")

        self.horizontalLayout.addWidget(self.product_btn, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Menu_KH)

        QMetaObject.connectSlotsByName(Menu_KH)
    # setupUi

    def retranslateUi(self, Menu_KH):
        Menu_KH.setWindowTitle(QCoreApplication.translate("Menu_KH", u"Menu - Kh\u00e1ch h\u00e0ng", None))
        self.groupBox.setTitle(QCoreApplication.translate("Menu_KH", u"T\u00e0i kho\u1ea3n", None))
        self.label.setText(QCoreApplication.translate("Menu_KH", u"Ch\u00e0o m\u1eebng kh\u00e1ch h\u00e0ng", None))
        self.name_label.setText(QCoreApplication.translate("Menu_KH", u"<TenKhachHang>", None))
        self.account_btn.setText(QCoreApplication.translate("Menu_KH", u"Th\u00f4ng tin t\u00e0i kho\u1ea3n", None))
        self.signout_btn.setText(QCoreApplication.translate("Menu_KH", u"\u0110\u0103ng xu\u1ea5t", None))
        self.orderhistory_btn.setText(QCoreApplication.translate("Menu_KH", u"L\u1ecbch s\u1eed \u0111\u1eb7t h\u00e0ng", None))
        self.product_btn.setText(QCoreApplication.translate("Menu_KH", u"Danh s\u00e1ch s\u1ea3n ph\u1ea9m", None))
    # retranslateUi

