import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_menu_quanli import Ui_QL

class ImgWidget(QLabel):
    def __init__(self,imagePath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagePath)
       
        self.setPixmap(pic)
        self.setAlignment(Qt.AlignCenter)
        #self.setScaledContents(True)

class QL(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_QL()
        self.ui.setupUi(self)

    def populateTableByProfit(self,productList):
        self.ui.table.setColumnCount(2)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Month"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Profit"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):                    
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                #item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

    def populateTableByBestProduct(self,productList):
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Số lượng bán"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Minh hoạ"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
  
        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                if (j == len(productList[i])-1):
                    imgPath = "image\\" + productList[i][0]
                    if (os.path.isfile(imgPath+".jpg")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".jpg"))
                    elif(os.path.isfile(imgPath+".png")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".png"))
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                #item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

    def bestEmployeeByMonthYear(self,productList):
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã NV"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên NV"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Số ngày làm việc trong tháng"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)

        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):                    
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                #item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()