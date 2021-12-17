# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_quanliaejinL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QL(object):
    def setupUi(self, QL):
        if not QL.objectName():
            QL.setObjectName(u"QL")
        QL.resize(621, 442)
        self.horizontalLayout_2 = QHBoxLayout(QL)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(QL)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(self.groupBox)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(0)
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table, 1, 0, 1, 4)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 0, 2, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.doanhthu = QLabel(self.groupBox)
        self.doanhthu.setObjectName(u"doanhthu")

        self.gridLayout.addWidget(self.doanhthu, 0, 3, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(QL)

        QMetaObject.connectSlotsByName(QL)
    # setupUi

    def retranslateUi(self, QL):
        QL.setWindowTitle(QCoreApplication.translate("QL", u"Menu - Qu\u1ea3n l\u00ed", None))
        self.groupBox.setTitle(QCoreApplication.translate("QL", u"Menu qu\u1ea3n l\u00ed", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("QL", u"Th\u1ed1ng k\u00ea doanh thu", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("QL", u"Top 10 Nh\u00e2n vi\u00ean t\u1ed1t", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("QL", u"S\u1ea3n ph\u1ea9m b\u00e1n ch\u1ea1y", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("QL", u"Doanh thu t\u1ed5ng", None))

        self.dateEdit.setDisplayFormat(QCoreApplication.translate("QL", u"yyyy/MM/dd", None))
        self.label.setText(QCoreApplication.translate("QL", u"M\u1ee5c", None))
        self.doanhthu.setText(QCoreApplication.translate("QL", u"<doanh thu t\u1ed5ng>", None))
    # retranslateUi

