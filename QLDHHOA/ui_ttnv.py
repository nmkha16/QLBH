# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ttnvhyvEjb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TTNV(object):
    def setupUi(self, TTNV):
        if not TTNV.objectName():
            TTNV.setObjectName(u"TTNV")
        TTNV.resize(712, 416)
        self.horizontalLayout = QHBoxLayout(TTNV)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(TTNV)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.type = QLabel(self.frame)
        self.type.setObjectName(u"type")

        self.gridLayout.addWidget(self.type, 4, 6, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 3, 6, 1, 1)

        self.date = QLabel(self.frame)
        self.date.setObjectName(u"date")

        self.gridLayout.addWidget(self.date, 4, 2, 1, 2, Qt.AlignHCenter)

        self.Phone = QLabel(self.frame)
        self.Phone.setObjectName(u"Phone")

        self.gridLayout.addWidget(self.Phone, 1, 3, 1, 2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 2)

        self.addr = QLabel(self.frame)
        self.addr.setObjectName(u"addr")

        self.gridLayout.addWidget(self.addr, 2, 1, 1, 6)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.WorkMonth = QLabel(self.frame)
        self.WorkMonth.setObjectName(u"WorkMonth")

        self.gridLayout.addWidget(self.WorkMonth, 1, 5, 1, 2)

        self.income = QLabel(self.frame)
        self.income.setObjectName(u"income")

        self.gridLayout.addWidget(self.income, 4, 4, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 5, 1, 2)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.cmnd = QLabel(self.frame)
        self.cmnd.setObjectName(u"cmnd")

        self.gridLayout.addWidget(self.cmnd, 4, 0, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 4, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.MaNV = QLabel(self.frame)
        self.MaNV.setObjectName(u"MaNV")

        self.gridLayout.addWidget(self.MaNV, 1, 0, 1, 1)

        self.table = QTableWidget(self.frame)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setCornerButtonEnabled(False)
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)

        self.gridLayout.addWidget(self.table, 5, 0, 1, 7)

        self.email = QLabel(self.frame)
        self.email.setObjectName(u"email")

        self.gridLayout.addWidget(self.email, 4, 1, 1, 1)

        self.TenNV = QLabel(self.frame)
        self.TenNV.setObjectName(u"TenNV")

        self.gridLayout.addWidget(self.TenNV, 1, 1, 1, 2)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 2, 1, 2, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(TTNV)

        QMetaObject.connectSlotsByName(TTNV)
    # setupUi

    def retranslateUi(self, TTNV):
        TTNV.setWindowTitle(QCoreApplication.translate("TTNV", u"Th\u00f4ng tin nh\u00e2n vi\u00ean", None))
        self.type.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("TTNV", u"Lo\u1ea1i NV", None))
        self.date.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.Phone.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("TTNV", u"\u0110i\u1ec7n tho\u1ea1i", None))
        self.addr.setText(QCoreApplication.translate("TTNV", u"<ADDR>", None))
        self.label_10.setText(QCoreApplication.translate("TTNV", u"\u0110\u1ecba ch\u1ec9", None))
        self.label.setText(QCoreApplication.translate("TTNV", u"M\u00e3 NV", None))
        self.WorkMonth.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.income.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("TTNV", u"S\u1ed1 th\u00e1ng l\u00e0m vi\u1ec7c", None))
        self.label_5.setText(QCoreApplication.translate("TTNV", u"CMND", None))
        self.label_2.setText(QCoreApplication.translate("TTNV", u"T\u00ean NV", None))
        self.cmnd.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("TTNV", u"L\u01b0\u01a1ng", None))
        self.label_6.setText(QCoreApplication.translate("TTNV", u"Email", None))
        self.MaNV.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.email.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.TenNV.setText(QCoreApplication.translate("TTNV", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("TTNV", u"Ng\u00e0y sinh", None))
    # retranslateUi

