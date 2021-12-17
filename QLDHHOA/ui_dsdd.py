# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dsddOiLsVY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DSDD(object):
    def setupUi(self, DSDD):
        if not DSDD.objectName():
            DSDD.setObjectName(u"DSDD")
        DSDD.resize(505, 477)
        self.horizontalLayout_2 = QHBoxLayout(DSDD)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(DSDD)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setWrapping(True)
        self.dateEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.ok_btn = QPushButton(self.groupBox)
        self.ok_btn.setObjectName(u"ok_btn")

        self.gridLayout.addWidget(self.ok_btn, 0, 2, 1, 1)

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

        self.gridLayout.addWidget(self.table, 1, 0, 1, 3)


        self.horizontalLayout.addWidget(self.groupBox)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(DSDD)

        QMetaObject.connectSlotsByName(DSDD)
    # setupUi

    def retranslateUi(self, DSDD):
        DSDD.setWindowTitle(QCoreApplication.translate("DSDD", u"Danh s\u00e1ch nh\u00e2n vi\u00ean \u0111\u00e3 \u0111i\u1ec3m danh trong ng\u00e0y", None))
        self.groupBox.setTitle(QCoreApplication.translate("DSDD", u"Nh\u00e2n vi\u00ean l\u00e0m vi\u1ec7c trong ng\u00e0y", None))
        self.label.setText(QCoreApplication.translate("DSDD", u"L\u1ef1a ch\u1ecdn ng\u00e0y", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("DSDD", u"yyyy/MM/dd", None))
        self.ok_btn.setText(QCoreApplication.translate("DSDD", u"OK", None))

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

    # retranslateUi

