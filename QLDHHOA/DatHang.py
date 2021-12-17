
import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_dathang import Ui_DatHang


class ImgWidget(QLabel):
    def __init__(self,imagePath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagePath)
       
        self.setPixmap(pic)
        self.setAlignment(Qt.AlignCenter)
        #self.setScaledContents(True)


class DatHang(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_DatHang()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())

        self.ui.table_2.setRowCount(0)
        self.setHeaderForShoppingCart()
        #event for table




    def setHeaderForShoppingCart(self):
        self.ui.table_2.setColumnCount(5)
        # set column headers name for table
        self.ui.table_2.setHorizontalHeaderItem(0,QTableWidgetItem("Mã SP"))
        self.ui.table_2.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table_2.setHorizontalHeaderItem(2,QTableWidgetItem("Giá bán"))
        self.ui.table_2.setHorizontalHeaderItem(3,QTableWidgetItem("Số lượng"))
        self.ui.table_2.setHorizontalHeaderItem(4,QTableWidgetItem("Tổng tiền"))



    def populateTable(self,productList):
        self.ui.table.setColumnCount(5)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã SP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Giá bán"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Loại SP"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("Minh hoạ"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.table.rowHeight(24)
        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                if (j == len(productList[i])-1):
                    imgPath = "image\\" + productList[i][1]
                    if (os.path.isfile(imgPath+".jpg")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".jpg"))
                    elif(os.path.isfile(imgPath+".png")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".png"))
                    
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

    def populateCart(self,productList):
        self.ui.table_2.setRowCount(len(productList))

        for i in range(len(productList)):
            for j in range(len(productList[i])):                   
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                if (j != 3):
                    item.setFlags(Qt.ItemIsEditable)
                self.ui.table_2.setItem(i,j,item)


 


