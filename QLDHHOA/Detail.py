import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_detail import Ui_Detail

class ImgWidget(QLabel):
    def __init__(self,imagePath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagePath)
       
        self.setPixmap(pic)
        self.setAlignment(Qt.AlignCenter)
        #self.setScaledContents(True)

class Detail(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Detail()
        self.ui.setupUi(self)

    def populateTableByWare(self,productList):
        self.ui.table.setColumnCount(4)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã SP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Số lượng tồn"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Minh hoạ"))

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

    def populateTableByIm_Export(self,productList):
        self.ui.table.setColumnCount(7)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã Kho"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Số lượng"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Loại"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("Ngày thực hiện"))
        self.ui.table.setHorizontalHeaderItem(5,QTableWidgetItem("Mã nhân viên phụ trách"))
        self.ui.table.setHorizontalHeaderItem(6,QTableWidgetItem("Địa chỉ nhập/xuất"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):                    
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

    def populateTableByEmployeeWork(self,productList):
        self.ui.table.blockSignals(True)
        self.ui.table.setColumnCount(4)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã NV"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên NV"))

        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Tình trạng"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Xác nhận"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        # now populate the table with data

        lists = {"Nghỉ việc","Nghỉ phép","Đang làm","Chưa làm"}
        
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                if (j == 2):
                    comboBox = QComboBox()
                    for x in lists:
                        comboBox.addItem(x)
                    comboBox.setCurrentText(productList[i][j])
                    self.ui.table.setCellWidget(i,j,comboBox)
                    #add checkbox to fourth column
                    item1= QTableWidgetItem()
                    item1.setCheckState(Qt.Unchecked)
                    self.ui.table.setItem(i,j+1,item1)

                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()
        self.ui.table.blockSignals(False)


    def populateTableByEmployeeRegister(self,productList):
        self.ui.table.blockSignals(True)
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã NV"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên NV"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Xác nhận"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                if (j == 1):
                    #add checkbox to third column
                    item1= QTableWidgetItem()
                    item1.setCheckState(Qt.Unchecked)
                    item1.setTextAlignment(Qt.AlignCenter)
                    self.ui.table.setItem(i,j+1,item1)

                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)

        self.ui.table.resizeRowsToContents()
        self.ui.table.blockSignals(False)

    def populateTableByPay(self,productList):
        self.ui.table.blockSignals(True)
        self.ui.table.setColumnCount(4)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã NV"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên NV"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Lương trả"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Xác nhận"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                if (j == 1):
                    
                    item = QTableWidgetItem()
                    item.setTextAlignment(Qt.AlignCenter)
                    self.ui.table.setItem(i,j+1,item)
                    #add checkbox to fourth column
                    item1= QTableWidgetItem()
                    item1.setCheckState(Qt.Unchecked)
                    item1.setTextAlignment(Qt.AlignCenter)
                    self.ui.table.setItem(i,j+2,item1)

                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)

        self.ui.table.resizeRowsToContents()
        self.ui.table.blockSignals(False)