# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowhucwhv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(251, 148)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.connect_btn = QPushButton(self.centralwidget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.connect_btn, 0, 2, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 2)

        self.signup_btn = QPushButton(self.centralwidget)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.signup_btn, 3, 1, 1, 1)

        self.ok_btn = QPushButton(self.centralwidget)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setStyleSheet(u"")

        self.gridLayout.addWidget(self.ok_btn, 3, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Main", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Kh\u00e1ch h\u00e0ng", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Qu\u1ea3n tr\u1ecb", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Qu\u1ea3n l\u00ed", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Nh\u00e2n s\u1ef1", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Nh\u00e2n vi\u00ean", None))

        self.connect_btn.setText(QCoreApplication.translate("MainWindow", u"K\u1ebft n\u1ed1i", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0110i\u1ec7n tho\u1ea1i", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u1eadt kh\u1ea9u", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng k\u00fd", None))
        self.ok_btn.setText(QCoreApplication.translate("MainWindow", u"\u0110\u0103ng nh\u1eadp", None))
    # retranslateUi

