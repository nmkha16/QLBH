# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_nhansuqyZHQC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Menu_NS(object):
    def setupUi(self, Menu_NS):
        if not Menu_NS.objectName():
            Menu_NS.setObjectName(u"Menu_NS")
        Menu_NS.resize(384, 233)
        self.verticalLayout = QVBoxLayout(Menu_NS)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Menu_NS)
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

        self.view_btn = QPushButton(self.groupBox)
        self.view_btn.setObjectName(u"view_btn")

        self.gridLayout.addWidget(self.view_btn, 1, 0, 1, 1)

        self.signout_btn = QPushButton(self.groupBox)
        self.signout_btn.setObjectName(u"signout_btn")

        self.gridLayout.addWidget(self.signout_btn, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(Menu_NS)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.register_btn = QPushButton(self.frame)
        self.register_btn.setObjectName(u"register_btn")

        self.horizontalLayout.addWidget(self.register_btn, 0, Qt.AlignTop)

        self.pay_btn = QPushButton(self.frame)
        self.pay_btn.setObjectName(u"pay_btn")

        self.horizontalLayout.addWidget(self.pay_btn)

        self.fire_btn = QPushButton(self.frame)
        self.fire_btn.setObjectName(u"fire_btn")

        self.horizontalLayout.addWidget(self.fire_btn)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Menu_NS)

        QMetaObject.connectSlotsByName(Menu_NS)
    # setupUi

    def retranslateUi(self, Menu_NS):
        Menu_NS.setWindowTitle(QCoreApplication.translate("Menu_NS", u"Menu - Nh\u00e2n s\u1ef1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Menu_NS", u"T\u00e0i kho\u1ea3n", None))
        self.label.setText(QCoreApplication.translate("Menu_NS", u"Ch\u00e0o nh\u00e2n s\u1ef1 ", None))
        self.name_label.setText(QCoreApplication.translate("Menu_NS", u"<TenNV>", None))
        self.view_btn.setText(QCoreApplication.translate("Menu_NS", u"Theo d\u00f5i nh\u00e2n vi\u00ean", None))
        self.signout_btn.setText(QCoreApplication.translate("Menu_NS", u"\u0110\u0103ng xu\u1ea5t", None))
        self.register_btn.setText(QCoreApplication.translate("Menu_NS", u"\u0110i\u1ec3m danh", None))
        self.pay_btn.setText(QCoreApplication.translate("Menu_NS", u"Tr\u1ea3 l\u01b0\u01a1ng", None))
        self.fire_btn.setText(QCoreApplication.translate("Menu_NS", u"Sa th\u1ea3i", None))
    # retranslateUi

