import os
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_lsdh_khachhang import Ui_LSDH


class ImgWidget(QLabel):
    def __init__(self,imagePath, parent=None):
        super(ImgWidget, self).__init__(parent)

        pic = QPixmap(imagePath)
       
        self.setPixmap(pic)
        self.setAlignment(Qt.AlignCenter)
        #self.setScaledContents(True)

class LSDH(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_LSDH()
        self.ui.setupUi(self)

    def populateTable(self,orderList):
        ###### SET HEADER
        self.ui.table.setColumnCount(5)
        self.ui.table.setRowCount(len(orderList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã DH"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Ngày mua"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Địa chỉ giao hàng"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Tình Trạng"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("Tổng tiền"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.ui.table.rowHeight(24)

        # now populate the table with data
        for i in range(len(orderList)):
            for j in range(len(orderList[i])):                    
                item = QTableWidgetItem(str(orderList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)

class CTDH(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_LSDH()
        self.ui.setupUi(self)
        self.ui.label.setText("Chi tiết đơn hàng hiện tại")
        self.ui.name_label.setText("")
    def populateTable(self,orderDetail):
        ###### SET HEADER
        self.ui.table.setColumnCount(6)
        self.ui.table.setRowCount(len(orderDetail))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Tên SP"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Giá SP"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Số lượng"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Giá giảm"))
        self.ui.table.setHorizontalHeaderItem(4,QTableWidgetItem("Thành tiền"))
        self.ui.table.setHorizontalHeaderItem(5,QTableWidgetItem("Minh hoạ"))
        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)

        self.ui.table.rowHeight(24)

        # now populate the table with data
        for i in range(len(orderDetail)):
            for j in range(len(orderDetail[i])):
                if (j == len(orderDetail[i])-1):
                    imgPath = "image\\" + orderDetail[i][0]
                    if (os.path.isfile(imgPath+".jpg")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".jpg"))
                    elif(os.path.isfile(imgPath+".png")):
                        self.ui.table.setCellWidget(i,j+1, ImgWidget(imgPath+".png"))
                    
                item = QTableWidgetItem(str(orderDetail[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()