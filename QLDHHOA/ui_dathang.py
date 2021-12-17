# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dathangcZtZQU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DatHang(object):
    def setupUi(self, DatHang):
        if not DatHang.objectName():
            DatHang.setObjectName(u"DatHang")
        DatHang.resize(1090, 793)
        DatHang.setAutoFillBackground(False)
        DatHang.setStyleSheet(u"background-image: url(\"image/background.jpg\");")
        self.frame = QFrame(DatHang)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 1071, 771))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(500, 10, 561, 261))
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background: none;")
        self.table_2 = QTableWidget(self.groupBox)
        if (self.table_2.columnCount() < 2):
            self.table_2.setColumnCount(2)
        if (self.table_2.rowCount() < 3):
            self.table_2.setRowCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_2.setItem(0, 0, __qtablewidgetitem)
        self.table_2.setObjectName(u"table_2")
        self.table_2.setGeometry(QRect(10, 60, 541, 181))
        self.table_2.setStyleSheet(u"background: none;")
        self.table_2.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table_2.setAlternatingRowColors(True)
        self.table_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.table_2.setGridStyle(Qt.SolidLine)
        self.table_2.setCornerButtonEnabled(True)
        self.table_2.setRowCount(3)
        self.table_2.setColumnCount(2)
        self.table_2.horizontalHeader().setVisible(True)
        self.table_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_2.horizontalHeader().setHighlightSections(True)
        self.table_2.horizontalHeader().setStretchLastSection(True)
        self.table_2.verticalHeader().setVisible(False)
        self.table_2.verticalHeader().setStretchLastSection(False)
        self.order_btn = QPushButton(self.groupBox)
        self.order_btn.setObjectName(u"order_btn")
        self.order_btn.setGeometry(QRect(10, 23, 101, 23))
        self.order_btn.setStyleSheet(u"background: none;")
        self.delete_btn = QPushButton(self.groupBox)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(394, 20, 151, 23))
        self.delete_btn.setStyleSheet(u"background: none;")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 270, 1051, 491))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setStyleSheet(u"background: none;")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.next_btn = QToolButton(self.groupBox_2)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setStyleSheet(u"background:white;")
        self.next_btn.setArrowType(Qt.RightArrow)

        self.gridLayout.addWidget(self.next_btn, 0, 3, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: none;")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.table = QTableWidget(self.groupBox_2)
        if (self.table.columnCount() < 2):
            self.table.setColumnCount(2)
        if (self.table.rowCount() < 3):
            self.table.setRowCount(3)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem1)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"background: none;")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
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

        self.gridLayout.addWidget(self.table, 2, 0, 1, 8)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background: none;")

        self.gridLayout.addWidget(self.lineEdit, 0, 4, 1, 1)

        self.search_btn = QPushButton(self.groupBox_2)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setStyleSheet(u"background: none;")

        self.gridLayout.addWidget(self.search_btn, 0, 5, 1, 1)

        self.prev_btn = QToolButton(self.groupBox_2)
        self.prev_btn.setObjectName(u"prev_btn")
        self.prev_btn.setStyleSheet(u"background: white;")
        self.prev_btn.setArrowType(Qt.LeftArrow)

        self.gridLayout.addWidget(self.prev_btn, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 10, 471, 251))
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet(u"background: none;")
        self.category = QComboBox(self.groupBox_3)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(120, 50, 141, 20))
        self.category.setStyleSheet(u"background: none;")
        self.category_smol = QComboBox(self.groupBox_3)
        self.category_smol.setObjectName(u"category_smol")
        self.category_smol.setGeometry(QRect(120, 140, 141, 20))
        self.category_smol.setStyleSheet(u"background: none;")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 61, 16))
        self.label_2.setStyleSheet(u"background: none;")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 71, 21))
        self.label_3.setStyleSheet(u"background: none;")

        self.retranslateUi(DatHang)

        QMetaObject.connectSlotsByName(DatHang)
    # setupUi

    def retranslateUi(self, DatHang):
        DatHang.setWindowTitle(QCoreApplication.translate("DatHang", u"\u0110\u1eb7t h\u00e0ng", None))
        self.groupBox.setTitle(QCoreApplication.translate("DatHang", u"S\u1ea3n ph\u1ea9m \u0111\u00e3 ch\u1ecdn", None))

        __sortingEnabled = self.table_2.isSortingEnabled()
        self.table_2.setSortingEnabled(False)
        self.table_2.setSortingEnabled(__sortingEnabled)

        self.order_btn.setText(QCoreApplication.translate("DatHang", u"\u0110\u1eb7t h\u00e0ng", None))
        self.delete_btn.setText(QCoreApplication.translate("DatHang", u"Xo\u00e1 s\u1ea3n ph\u1ea9m", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DatHang", u"S\u1ea3n ph\u1ea9m", None))
        self.next_btn.setText(QCoreApplication.translate("DatHang", u"...", None))
        self.label.setText(QCoreApplication.translate("DatHang", u"<Pg.Number>", None))

        __sortingEnabled1 = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled1)

        self.search_btn.setText(QCoreApplication.translate("DatHang", u"T\u00ecm ki\u1ebfm", None))
        self.prev_btn.setText(QCoreApplication.translate("DatHang", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("DatHang", u"Danh m\u1ee5c", None))
        self.label_2.setText(QCoreApplication.translate("DatHang", u"Ch\u1ee7 \u0111\u1ec1", None))
        self.label_3.setText(QCoreApplication.translate("DatHang", u"Th\u1ec3 lo\u1ea1i", None))
    # retranslateUi

