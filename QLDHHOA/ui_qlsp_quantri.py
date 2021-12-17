# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qlsp_quantriCiqzUU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_QLSP(object):
    def setupUi(self, QLSP):
        if not QLSP.objectName():
            QLSP.setObjectName(u"QLSP")
        QLSP.resize(1091, 789)
        QLSP.setStyleSheet(u"background-image: url(\"image/background.jpg\");")
        self.frame = QFrame(QLSP)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1071, 771))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(500, 10, 561, 251))
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(8)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background: none;")
        self.addrow_btn = QPushButton(self.groupBox)
        self.addrow_btn.setObjectName(u"addrow_btn")
        self.addrow_btn.setGeometry(QRect(10, 23, 81, 21))
        self.addrow_btn.setStyleSheet(u"background: none;")
        self.table2 = QTableWidget(self.groupBox)
        if (self.table2.columnCount() < 2):
            self.table2.setColumnCount(2)
        self.table2.setObjectName(u"table2")
        self.table2.setGeometry(QRect(10, 60, 541, 181))
        self.table2.setStyleSheet(u"background: none;")
        self.table2.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.table2.setAlternatingRowColors(True)
        self.table2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table2.setGridStyle(Qt.SolidLine)
        self.table2.setCornerButtonEnabled(True)
        self.table2.setRowCount(0)
        self.table2.setColumnCount(2)
        self.table2.horizontalHeader().setVisible(True)
        self.table2.horizontalHeader().setCascadingSectionResizes(False)
        self.table2.horizontalHeader().setHighlightSections(True)
        self.table2.horizontalHeader().setStretchLastSection(True)
        self.table2.verticalHeader().setVisible(False)
        self.table2.verticalHeader().setStretchLastSection(False)
        self.remove_btn = QPushButton(self.groupBox)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setGeometry(QRect(460, 20, 81, 23))
        self.remove_btn.setStyleSheet(u"background: none;")
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
        self.next_btn.setStyleSheet(u"background: white;")
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
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setItem(0, 0, __qtablewidgetitem)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"")
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
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
        self.category.setGeometry(QRect(130, 50, 131, 20))
        self.category.setStyleSheet(u"background: none;")
        self.category_smol = QComboBox(self.groupBox_3)
        self.category_smol.setObjectName(u"category_smol")
        self.category_smol.setGeometry(QRect(130, 100, 131, 20))
        self.category_smol.setStyleSheet(u"background: none;")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 61, 16))
        self.label_2.setStyleSheet(u"background: none;")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 71, 21))
        self.label_3.setStyleSheet(u"background-image: none;")
        self.update_btn = QPushButton(self.groupBox_3)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setGeometry(QRect(280, 50, 171, 23))
        self.update_btn.setStyleSheet(u"background: none;")
        self.delete_btn = QPushButton(self.groupBox_3)
        self.delete_btn.setObjectName(u"delete_btn")
        self.delete_btn.setGeometry(QRect(280, 150, 171, 23))
        self.delete_btn.setStyleSheet(u"background: none;")
        self.add_btn = QPushButton(self.groupBox_3)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(280, 100, 171, 23))
        self.add_btn.setStyleSheet(u"background: none;")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 81, 21))
        self.label_4.setStyleSheet(u"background: none;")
        self.CBox = QComboBox(self.groupBox_3)
        self.CBox.addItem("")
        self.CBox.addItem("")
        self.CBox.setObjectName(u"CBox")
        self.CBox.setGeometry(QRect(130, 150, 131, 20))
        self.CBox.setStyleSheet(u"background: none;")
        self.filter_btn = QPushButton(self.groupBox_3)
        self.filter_btn.setObjectName(u"filter_btn")
        self.filter_btn.setGeometry(QRect(170, 190, 91, 23))
        self.filter_btn.setStyleSheet(u"background: none;")

        self.retranslateUi(QLSP)

        QMetaObject.connectSlotsByName(QLSP)
    # setupUi

    def retranslateUi(self, QLSP):
        QLSP.setWindowTitle(QCoreApplication.translate("QLSP", u"Qu\u1ea3n l\u00ed s\u1ea3n ph\u1ea9m", None))
        self.groupBox.setTitle(QCoreApplication.translate("QLSP", u"Th\u00eam s\u1ea3n ph\u1ea9m", None))
        self.addrow_btn.setText(QCoreApplication.translate("QLSP", u"Th\u00eam", None))
        self.remove_btn.setText(QCoreApplication.translate("QLSP", u"Xo\u00e1", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("QLSP", u"S\u1ea3n ph\u1ea9m", None))
        self.next_btn.setText(QCoreApplication.translate("QLSP", u"...", None))
        self.label.setText(QCoreApplication.translate("QLSP", u"<Pg.Number>", None))

        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)

        self.search_btn.setText(QCoreApplication.translate("QLSP", u"T\u00ecm ki\u1ebfm", None))
        self.prev_btn.setText(QCoreApplication.translate("QLSP", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("QLSP", u"Danh m\u1ee5c", None))
        self.label_2.setText(QCoreApplication.translate("QLSP", u"Ch\u1ee7 \u0111\u1ec1", None))
        self.label_3.setText(QCoreApplication.translate("QLSP", u"Th\u1ec3 lo\u1ea1i", None))
        self.update_btn.setText(QCoreApplication.translate("QLSP", u"C\u1eadp nh\u1eadt", None))
        self.delete_btn.setText(QCoreApplication.translate("QLSP", u"Xo\u00e1", None))
        self.add_btn.setText(QCoreApplication.translate("QLSP", u"Th\u00eam s\u1ea3n ph\u1ea9m", None))
        self.label_4.setText(QCoreApplication.translate("QLSP", u"Kho/S\u1ea3n ph\u1ea9m", None))
        self.CBox.setItemText(0, QCoreApplication.translate("QLSP", u"S\u1ea3n ph\u1ea9m", None))
        self.CBox.setItemText(1, QCoreApplication.translate("QLSP", u"Kho", None))

        self.filter_btn.setText(QCoreApplication.translate("QLSP", u"L\u1ecdc", None))
    # retranslateUi

