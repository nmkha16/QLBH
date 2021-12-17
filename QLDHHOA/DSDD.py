
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtWidgets import *
from ui_dsdd import Ui_DSDD

class DSDD(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_DSDD()
        self.ui.setupUi(self)

    def populateTable(self,productList):
        self.ui.table.setColumnCount(3)
        self.ui.table.setRowCount(len(productList))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Mã NV"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Tên NV"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Ngày điểm danh"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        # now populate the table with data
        for i in range(len(productList)):
            for j in range(len(productList[i])):
                    
                item = QTableWidgetItem(str(productList[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                #item.setFlags(Qt.ItemIsEditable)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()