import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_qlsp_quantri import Ui_QLSP
import random, string

class ImgWidget(QLabel):
    def __init__(self,imagePath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagePath)
       
        self.setPixmap(pic)
        self.setAlignment(Qt.AlignCenter)

class QLSP(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_QLSP()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        #set header for table2
        self.ui.table2.setColumnCount(5)
        self.ui.table2.setRowCount(0)
        # set column headers name for table2
        self.ui.table2.setHorizontalHeaderItem(0,QTableWidgetItem("Mã SP"))
        self.ui.table2.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table2.setHorizontalHeaderItem(2,QTableWidgetItem("Giá bán"))
        self.ui.table2.setHorizontalHeaderItem(3,QTableWidgetItem("Loại SP"))
        self.ui.table2.setHorizontalHeaderItem(4,QTableWidgetItem("Mã kho"))

        #event for table and list double click
        self.ui.addrow_btn.clicked.connect(self.addRow)
        self.ui.remove_btn.clicked.connect(self.removeItem)

    def removeItem(self):
        curRow = self.ui.table2.currentRow()
        self.ui.table2.removeRow(curRow)

    def addRow(self):
        self.ui.table2.insertRow(self.ui.table2.rowCount())
        # auto generate id
        item = QTableWidgetItem(randomword(10))
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.table2.setItem(self.ui.table2.rowCount()-1,0,item)

        item = QTableWidgetItem("9PKRJU")
        item.setTextAlignment(Qt.AlignCenter)
        self.ui.table2.setItem(self.ui.table2.rowCount()-1,4,item)

    def populateTableByProducts(self,List):
        self.ui.table.clearContents()
        self.ui.table.setColumnCount(7)
        self.ui.table.setRowCount(len(List))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã SP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Giá bán"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Loại SP"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("Mã kho"))
        self.ui.table.setHorizontalHeaderItem(5,QTableWidgetItem("Mã danh mục"))
        self.ui.table.setHorizontalHeaderItem(6,QTableWidgetItem("Minh hoạ"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.ui.table.rowHeight(24)
        # now populate the table with data
        for i in range(len(List)):
            for j in range(len(List[i])):
                if (j == len(List[i])-1):
                    imgPath = "image\\" + List[i][1]
                    if (os.path.isfile(imgPath+".jpg")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".jpg"))
                    elif(os.path.isfile(imgPath+".png")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".png"))
                item = QTableWidgetItem(str(List[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                if (j == 0):
                    item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

    def populateTableByWarehouse(self,List):
        self.ui.table.clearContents()
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(len(List))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã Kho"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Địa chỉ"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Mã nhân viên phụ trách"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        # now populate the table with data
        for i in range(len(List)):
            for j in range(len(List[i])):
                item = QTableWidgetItem(str(List[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()
    
    def populateTable(self,List):
        if (self.ui.CBox.itemText(self.ui.CBox.currentIndex()) == "Sản phẩm"):
            self.populateTableByProducts(List)
        else:
            self.populateTableByWarehouse(List)



#generate random word
def randomword(length):
   letters = string.ascii_uppercase+string.digits
   return ''.join(random.choice(letters) for i in range(length))