# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lsdh_khachhangofcakh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LSDH(object):
    def setupUi(self, LSDH):
        if not LSDH.objectName():
            LSDH.setObjectName(u"LSDH")
        LSDH.resize(1029, 697)
        self.horizontalLayout = QHBoxLayout(LSDH)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(LSDH)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(self.groupBox)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setCornerButtonEnabled(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.table, 2, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name_label = QLabel(self.groupBox)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(LSDH)

        QMetaObject.connectSlotsByName(LSDH)
    # setupUi

    def retranslateUi(self, LSDH):
        LSDH.setWindowTitle(QCoreApplication.translate("LSDH", u"L\u1ecbch s\u1eed \u0111\u01a1n h\u00e0ng", None))
        self.groupBox.setTitle(QCoreApplication.translate("LSDH", u"\u0110\u01a1n h\u00e0ng", None))
        self.label.setText(QCoreApplication.translate("LSDH", u"L\u1ecbch s\u1eed mua h\u00e0ng c\u1ee7a", None))
        self.name_label.setText(QCoreApplication.translate("LSDH", u"<insert name>", None))
    # retranslateUi

