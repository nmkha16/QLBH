# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailEhpqHn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Detail(object):
    def setupUi(self, Detail):
        if not Detail.objectName():
            Detail.setObjectName(u"Detail")
        Detail.resize(851, 575)
        self.horizontalLayout_2 = QHBoxLayout(Detail)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Detail)
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
        if (self.table.rowCount() < 3):
            self.table.setRowCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(3)
        self.table.setColumnCount(2)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Detail)

        QMetaObject.connectSlotsByName(Detail)
    # setupUi

    def retranslateUi(self, Detail):
        Detail.setWindowTitle(QCoreApplication.translate("Detail", u"Chi ti\u1ebft", None))
        self.groupBox.setTitle(QCoreApplication.translate("Detail", u"Label", None))

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("Detail", u"Label", None))
    # retranslateUi

