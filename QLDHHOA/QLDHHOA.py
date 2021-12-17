
from os import curdir
import pyodbc
from PySide2.QtCore import (QAbstractItemModel, QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from QLSP import QLSP
from ui_ketnoi import Ui_Form
from ui_mainwindow import Ui_MainWindow
from ui_dangky_khachhang import Ui_DKKH
from ui_menu_khachhang import Ui_Menu_KH
from DatHang import DatHang
from LSDH import LSDH,CTDH
from Detail import Detail
from ui_dknv import Ui_DKNV
from ui_ttnv import Ui_TTNV
from ui_menu_nhansu import Ui_Menu_NS
from DSDD import DSDD
from Menu_QL import QL
from qt_material import apply_stylesheet
from datetime import date
import random, string

#global cursor, allow easier calling sql query from any where in class
global cursor
#global status, check if app is connected to db
status = False
#global id, store current user id
id = ""

class gui(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)    
        
        self.pageNumber =1 #Track page number of table for QLSP_QuanTri 
        self.isPage = False
        ###### button event
        self.ui.connect_btn.clicked.connect(self.ketNoiWidget)
        self.ui.signup_btn.clicked.connect(self.DKKHWidget)
        self.ui.ok_btn.clicked.connect(self.signInVerification)
        

    #Mở window kết nối
    def ketNoiWidget(self):
        self.ketNoi = KetNoi()
        self.ketNoi.show()

    #Mở window đăng ký khách hàng
    def DKKHWidget(self):
        if (status):
            loginType = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
            if (loginType == "Khách hàng"):
                self.dkkh = DKKH()
                self.dkkh.show()
            elif(loginType == "Nhân viên"):
                self.dknv= DKNV()
                self.dknv.show()
    #Mở window menu khách hàng sau khi đăng nhập thành công
    def menuKH(self):
        if (status):
            self.menukh = Menu_KH()
            self.menukh.show()

    def signInVerification(self):
        global id
        global cursor
        role = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        phone = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        try:
            if (role == "Khách hàng"):
                ### 
                phone = "0865462805"
                password = "Corpus Christi8"
                cursor.execute("Select makh from khachhang where dienthoaikh=? and matkhau =?",phone,password)
                id = cursor.fetchone()[0]
                self.menuKH()

            elif(role == "Quản trị"):
                ### 
                phone = "092832141"
                password = "123456"
                cursor.execute("Select manv from nhanvien where dienthoainv=? and matkhau =? and loainv = N'Quản trị'",phone,password)
                id = cursor.fetchone()[0]
                
                self.initialQLSPWidget()
            elif(role=="Nhân viên"):
                ### 
                phone = "0855903412     "
                password = "Colorado8      "
                cursor.execute("Select manv from nhanvien where dienthoainv=? and matkhau =? and loainv = N'Thường'",phone,password)
                id = cursor.fetchone()[0]
                self.ttnv = TTNV()
                self.ttnv.show()
            elif(role=="Nhân sự"):
                ### fast debug hack
                phone = "092841231      "
                password = "123456         "
                cursor.execute("Select manv from nhanvien where dienthoainv=? and matkhau =? and loainv = N'Nhân sự'",phone,password)
                id = cursor.fetchone()[0]
                self.ttns = Menu_NS()
                self.ttns.show()
            elif(role=="Quản lí"):
                ### fast debug hack
                phone = "094535241      "
                password = "123456         "
                cursor.execute("Select manv from nhanvien where dienthoainv=? and matkhau =? and loainv = N'Quản lí'",phone,password)
                id = cursor.fetchone()[0]
                self.initialManagerWidget()
        except:
            self.ui.messBox = QMessageBox()
            self.ui.messBox.setWindowTitle("Thông báo")
            self.ui.messBox.setText("Đăng nhập thất bại")
            self.ui.messBox.show()
      
    def initialManagerWidget(self):
        self.ql = QL()
        self.ql.show()

        # block date signal
        #self.ql.ui.dateEdit.blockSignals(False)
        #set event 
        self.ql.ui.comboBox.currentIndexChanged.connect(self.do_event)
        self.ql.ui.dateEdit.dateChanged.connect(self.calculateEvent)

    def calculateEvent(self,newDate):
        event= self.ql.ui.comboBox.itemText(self.ql.ui.comboBox.currentIndex())
        if (event == "Nhân viên tốt"):
            curDate = str(self.ql.ui.dateEdit.date().toPython())
            year = curDate.split('-')[0]
            month = curDate.split('-')[1]
            cursor.execute("select top 10 d1.manv,n.tennv, count(d1.ngayDiemDanh) 'SoDiemDanh' from diemdanh d1 join nhanvien n on n.manv = d1.manv where month(d1.ngaydiemdanh)=? and year(d1.ngaydiemdanh)=? group by d1.manv, n.TenNV",month,year)
            row = queryToList(cursor.fetchall())
            self.ql.bestEmployeeByMonthYear(row)
        elif (event == "Thống kê doanh thu"):
            year = str(newDate.toPython()).split('-')[0]

            cursor.execute("select month(ngaylapdh), sum(tongtien) from donhang where year(ngayLapDH) = ? group by month(ngayLapDH)",year)
            row = cursor.fetchall()
            row = queryToList(row)

            self.ql.populateTableByProfit(row)

    def do_event(self):
        event= self.ql.ui.comboBox.itemText(self.ql.ui.comboBox.currentIndex())

        if (event == "Thông kê doanh thu"):
            self.ql.ui.dateEdit.blockSignals(False)

        elif(event =="Sản phẩm bán chạy"):
            self.ql.ui.dateEdit.blockSignals(True)
            cursor.execute("select s.tenSP,sum(c.soLuong)'SoLuongBan' from sanpham s join CTDH c on c.MaSP = s.MaSP group by s.tenSP")
            row = cursor.fetchall()
            row = queryToList(row)
            self.ql.populateTableByBestProduct(row)

        elif(event == "Doanh thu tổng"):
            self.ql.ui.dateEdit.blockSignals(True)
            cursor.execute("select sum(cast (tongtien as bigint)) from donhang")
            self.ql.ui.doanhthu.setText(str(cursor.fetchone()[0]) + "VND")

        elif(event == "Nhân viên tốt"):
            self.ql.ui.dateEdit.blockSignals(False)
            

    def initialQLSPWidget(self):
        global cursor
        self.qlsp = QLSP()
        self.qlsp.show()
        #set event button for filter button
        self.qlsp.ui.filter_btn.clicked.connect(self.ListByCategory)
        #set event button for button
        self.qlsp.ui.add_btn.clicked.connect(self.addNewItemToDB)
        #set event for delete button
        self.qlsp.ui.delete_btn.clicked.connect(self.removeEntry)
        #set event for update button
        self.qlsp.ui.update_btn.clicked.connect(self.updateEntry)
        # dectect change everytime user change a category
        self.qlsp.ui.category.currentIndexChanged.connect(self.populateSmolCategory)
        #detect next page button clicked
        self.qlsp.ui.next_btn.clicked.connect(self.nextPage)
        # detect prev page button clicked
        self.qlsp.ui.prev_btn.clicked.connect(self.prevPage)
        # button event for searching
        self.qlsp.ui.search_btn.clicked.connect(self.searchItem)

        #detect cell clicked to view information
        self.qlsp.ui.table.cellClicked.connect(self.viewDetail)

        # set page number
        self.qlsp.ui.label.setText(str(self.pageNumber))
        #populate list of category QComboBox
        # create query to get category
        cursor.execute("select tenDM from danhmuc where (dmcha is null)")
        row = cursor.fetchall()
        self.category = queryToList(row)
        self.qlsp.ui.category.clear()
        for x in self.category:
            self.qlsp.ui.category.addItem(x[0])

    #xem thông tin chi tiết
    def viewDetail(self,row,col):
        global cusor
        self.qlsp.detail = Detail()
        if (self.qlsp.ui.CBox.itemText(self.qlsp.ui.CBox.currentIndex()) == "Kho"): 
            if (col == 0):
                self.qlsp.detail.show()
                self.qlsp.detail.ui.groupBox.setTitle("Chi tiết kho")
                self.qlsp.detail.ui.label.setText("Các sản phẩm trong kho")
                #print(self.qlsp.ui.table.item(row,0).text())
                cursor.execute("select masp,tensp,soluongton from ctkho where makho =?",self.qlsp.ui.table.item(row,0).text())
                row=cursor.fetchall()
                row = queryToList(row)
                self.qlsp.detail.populateTableByWare(row)
        else:
            if (col == 6):
                self.qlsp.detail.show()
                self.qlsp.detail.ui.groupBox.setTitle("Chi tiết sản phẩm")
                self.qlsp.detail.ui.label.setText("Lịch sử nhập xuất của sản phẩm")
                cursor.execute("select l.makho, c.tensp,c.soluong, l.loai, l.ngayThucHien, l.nhanVienPhuTrach, l.diaChiNhapXuat from ctnx c,LICHSUNHAPXUAT l where c.MaPhieu = l.MaPhieu and c.masp =?",self.qlsp.ui.table.item(row,0).text())
                row=cursor.fetchall()
                row = queryToList(row)
                self.qlsp.detail.populateTableByIm_Export(row)
                #self.qlsp.detail.populateTableByWare(row)

    #cập nhật sản phẩm
    def updateEntry(self):
        global cursor
        curRow = self.qlsp.ui.table.currentRow()
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        # perform delete product on database
        productID = self.qlsp.ui.table.item(curRow,0).text()
        productName = self.qlsp.ui.table.item(curRow,1).text()
        productPrice = self.qlsp.ui.table.item(curRow,2).text()
        productType = self.qlsp.ui.table.item(curRow,3).text()
        productWareID = self.qlsp.ui.table.item(curRow,4).text()
        productTypeID = self.qlsp.ui.table.item(curRow,5).text()
        cursor.execute("update sanpham set tensp=?,giaban=?,loaisp=?,makho=?,madm=? where masp = ?",productName,productPrice,productType,productWareID,productTypeID,productID)
        cursor.commit()
        try:
            #cursor.execute("delete from sanpham where masp = ?",self.ui.table.item(curRow,0).text())
            #cursor.commit()
            self.ui.messBox.setText("Cập nhật sản phẩm mới " +self.qlsp.ui.table.item(curRow,1).text() +" thành công")
        except:
            self.ui.messBox.setText("Mã kho không tồn tại hoặc trùng mã sản phẩm")
        self.ui.messBox.show()
    #xoá sản phẩm
    def removeEntry(self):
        global cursor
        curRow = self.qlsp.ui.table.currentRow()
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        # perform delete product on database
        try:
            cursor.execute("delete from sanpham where masp = ?",self.ui.table.item(curRow,0).text())
            cursor.commit()
            self.ui.messBox.setText("Xoá sản phẩm " +self.qlsp.ui.table.item(curRow,1).text() +" thành công")
        except:
            self.ui.messBox.setText("Xoá thất bại")
        self.ui.messBox.show()
            
    
    #thêm sản phẩm
    def addNewItemToDB(self):
        global cursor
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        self.ui.messBox.setText("Thêm "+str(self.qlsp.ui.table2.rowCount()) +" sản phẩm thành công")
        for i in range(self.qlsp.ui.table2.rowCount()):
            try:
                productID = self.qlsp.ui.table2.item(i,0).text()
                productName = self.qlsp.ui.table2.item(i,1).text()
                productPrice = self.qlsp.ui.table2.item(i,2).text()
                productType = self.qlsp.ui.table2.item(i,3).text()
                productWareID = self.qlsp.ui.table2.item(i,4).text()
                #get product ID base on MaDM
                cursor.execute("select madm from danhmuc where tendm = ?",productType)
                row = cursor.fetchone()[0]
            except:
                row = None
            try:                
                cursor.execute("insert into sanpham values (?,?,?,?,?,?)",productID,productName,productPrice,productType,productWareID,row)
                cursor.commit()
            except:
                self.ui.messBox.setText("Thêm sản phẩm thất bại")
        self.ui.messBox.show()
                
    def populateSmolCategory(self):
        global cursor
        #get ID of father category
        # create query to get id
        q = "select madm from danhmuc where tendm = N'"+ self.qlsp.ui.category.itemText(self.qlsp.ui.category.currentIndex())+"'"
        cursor.execute(q)
        id = cursor.fetchone()
        ### populate smol category
        q ="select tendm from danhmuc where dmcha ='"+id[0]+"'"
        cursor.execute(q)
        row = cursor.fetchall()
        self.smolcategory = queryToList(row)
        self.qlsp.ui.category_smol.clear()

        for x in self.smolcategory:
            self.qlsp.ui.category_smol.addItem(x[0])

    def ListByCategory(self):
        global cursor
        #user search for item

        if (self.isPage == False):
            self.pageNumber = 1
            self.qlsp.ui.table.clearContents()
        else:
            self.isPage = False
        if (self.qlsp.ui.CBox.itemText(self.qlsp.ui.CBox.currentIndex()) == "Sản phẩm"):
            #self.populateTableByProducts(List)
            # create query to get list of product
            q = "Select masp, tensp, giaban, loaisp,makho,madm from sanpham where loaisp = N'" +self.qlsp.ui.category_smol.itemText(self.qlsp.ui.category_smol.currentIndex())+"'"
            q+="order by tensp desc offset("+ str(self.pageNumber*10) +") rows fetch next(10) rows only"
            #print(q)
            cursor.execute(q)
            row = cursor.fetchall()

            self.List = queryToList(row)

        else:
           # self.populateTableByWarehouse(List)
            cursor.execute("Select MaKho,diachikho, nhanvienphutrach from kho")
            row = cursor.fetchall()
            self.List = queryToList(row)


        #if query return empty, revert pagenumber
        if (len(self.List)<1):
            self.pageNumber-=1
        else:            
            self.qlsp.populateTable(self.List)

        self.qlsp.ui.label.setText(str(self.pageNumber))

    def nextPage(self):
        self.isPage = True
        self.pageNumber+=1
        self.qlsp.ui.label.setText(str(self.pageNumber))
        self.ListByCategory()

    def prevPage(self):
        if (self.pageNumber >1):
            self.isPage = True
            self.pageNumber-=1 
            self.qlsp.ui.label.setText(str(self.pageNumber))
            self.ListByCategory()

    def searchItem(self):
        self.pageNumber =1
        self.qlsp.ui.label.setText(str(self.pageNumber))
        if (self.qlsp.ui.CBox.itemText(self.qlsp.ui.CBox.currentIndex()) == "Sản phẩm"):
            # create query to get list of product
            q = "Select masp, tensp, giaban, loaisp from sanpham where tensp like N'"+self.qlsp.ui.lineEdit.text()+"%'"
            #print(q)
            cursor.execute(q)
        else:
            cursor.execute("Select MaKho,diachikho, nhanvienphutrach from kho where MaKho like N'"+self.qlsp.ui.lineEdit.text()+"%'")
            
        row = cursor.fetchall()
        row = queryToList(row)
        self.qlsp.populateTable(row)

class KetNoi(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #fast debug hack
        self.ui.tensv_lnedit.setText("NMKHA")
        self.ui.tendb_lnedit.setText("DB_LAB2")
        # button event
        self.ui.ok_btn.clicked.connect(self.connect)

    def connect(self):
        global cursor
        global status
        #self.sv = "NMKHA"
        #self.db = "DA1"

        self.sv = str(self.ui.tensv_lnedit.text())
        self.db = str(self.ui.tendb_lnedit.text())
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        self.ui.messBox.show()
        _str = (('Driver={0};'
                                'Server={1};'
                                'Database={2};'
                                'Trusted_Connection=yes;').format("SQL SERVER",self.sv,self.db))
        try:
            if (self.sv == "" or self.db == ""):
                raise ValueError("Nothing in databased input entered")
            conn = pyodbc.connect(_str)
            status = True
            cursor = conn.cursor()
            
        except:
            self.ui.messBox.setText("Kết nối không thành công")            
            return

        self.ui.messBox.setText("Kết nối thành công")
        self.hide()

class DKKH(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_DKKH()
        self.ui.setupUi(self)

        #button event
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.signup_btn.clicked.connect(self.createAccount)

    def createAccount(self):
        global cursor
        # get variable from text input
        name = self.ui.name_lnedit.text()
        phone = self.ui.phone_lnedit.text()
        address =self.ui.address_lnedit.text()
        email =self.ui.email_lnedit.text()
        password = self.ui.pass_lnedit.text()

        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        try:
            cursor.execute("insert into khachhang values (?,?,?,?,?,?)",randomword(10),name,phone,address,email,password)
            cursor.commit()
            self.ui.messBox.setText("Thêm khách hàng " + name+" thành công")
        except:
            self.ui.messBox.setText("Thêm khách hàng " + name+" thất bại")

        self.ui.messBox.show()

class Menu_KH(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Menu_KH()
        self.ui.setupUi(self)  

        #create variable for page number
        self.pageNumber = 1
        #boolean variable for user clicking next page and prev page while chosing another category without affecting pageNumber
        self.isPage = False       
        #set name label
        global cursor
        global id
        cursor.execute("select tenkh from khachhang where makh = ?",id)
        self.ui.name_label.setText(cursor.fetchone()[0])

        #### button event
        self.ui.product_btn.clicked.connect(self.Products)
        self.ui.orderhistory_btn.clicked.connect(self.Lsdh)
        self.ui.account_btn.clicked.connect(self.accountInfo)
        self.ui.signout_btn.clicked.connect(self.close)
        

    #Mờ window cập nhật thông tin tài khoản khách hàng
    def accountInfo(self):
        global cursor
        global id
        #resue DKKH widget
        self.info = DKKH();
        #set label to "Cập nhật thông tin tài khoản"
        self.info.ui.label_2.setText("Cập nhật thông tin tài khoản")
        self.info.ui.signup_btn.setText("Cập nhật")

        cursor.execute("Select tenkh, dienthoaikh, diachikh, email, matkhau from khachhang where makh = '" +id+"'")
        row = cursor.fetchall()
        info = queryToList(row)
        #print(info)
        # set text to box
        self.info.ui.name_lnedit.setText(info[0][0])
        self.info.ui.phone_lnedit.setText(info[0][1])
        self.info.ui.address_lnedit.setText(info[0][2])
        self.info.ui.email_lnedit.setText(info[0][3])
        self.info.ui.pass_lnedit.setText(info[0][4])

        #button event
        self.info.ui.signup_btn.clicked.connect(self.updateInfo)
        self.info.ui.cancel_btn.clicked.connect(self.close)

        self.info.show()
    
    def updateInfo():
        global cursor
        # get variable from text input
        name = self.info.ui.name_lnedit.text()
        phone = self.info.ui.phone_lnedit.text()
        address =self.info.ui.address_lnedit.text()
        email =self.info.ui.email_lnedit.text()
        password = self.info.ui.pass_lnedit.text()
        
        #create query
        cursor.execute("update khachhang set tenkh=?, dienthoaikh=?, email=?, matkhau=? where makh = '"+self.id+"'",name,phone,address,email,password)
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        self.ui.messBox.setText("Cập nhật khách hàng " + name+" thành công")
        self.ui.messBox.show()
        self.info.close()


    #Mở window xem lịch sử đơn hàng
    def Lsdh(self):
        global cursor
        global id
        self.lsdh = LSDH()
        self.lsdh.show()
        #set name label
        #set name label
        cursor.execute("select tenkh from khachhang where makh = ?",id)
        self.lsdh.ui.name_label.setText(cursor.fetchone()[0])


        # query statement to get list of orders
        cursor.execute("select madh, ngaylapdh, diachidh,tinhtrang,tongtien from donhang where makh = '"+id+"'")
        row = cursor.fetchall()
        orderList = queryToList(row)
        
        self.lsdh.populateTable(orderList)

        ## set event for
        self.lsdh.ui.table.cellDoubleClicked.connect(self.showOrderDetail)


    def showOrderDetail(self):
        global cursor
        row = self.lsdh.ui.table.currentRow()
        orderID = (self.lsdh.ui.table.item(int(row),0).text())

        self.orderDetail = CTDH()
        self.orderDetail.show()

        #create query
        q = "select tensp, giasanpham, soluong, giagiam, thanhtien from ctdh where madh = '"+orderID+"'"
        #print(q)
        cursor.execute(q)
        row = cursor.fetchall()
        orderDetail = queryToList(row)

        self.orderDetail.populateTable(orderDetail)

    #Mở window sản phẩm để đặt hàng
    def Products(self):
        global cursor
        self.products = DatHang()
        self.products.show()
        # retrieve older shoping item
        self.getCart()
        # set page number
        self.products.ui.label.setText(str(self.pageNumber))
        #populate list of category QComboBox
        # create query to get category
        cursor.execute("select tenDM from danhmuc where (dmcha is null)")
        row = cursor.fetchall()
        self.category = queryToList(row)
        self.products.ui.category.clear()
        for x in self.category:
            self.products.ui.category.addItem(x[0])

        # dectect change everytime user change a category
        self.products.ui.category.currentIndexChanged.connect(self.populateSmolCategory)
        # dectect change verytime user change a smol category, auto populate table
        self.products.ui.category_smol.currentIndexChanged.connect(self.ProductListByCategory)
        #detect next page button clicked
        self.products.ui.next_btn.clicked.connect(self.nextPage)
        # detect prev page button clicked
        self.products.ui.prev_btn.clicked.connect(self.prevPage)
        # button event for searching
        self.products.ui.search_btn.clicked.connect(self.searchItem)
        # button event for order
        self.products.ui.order_btn.clicked.connect(self.createOrder)
    
        self.products.ui.table.cellDoubleClicked.connect(self.chooseItem) #double click item to chose
        self.products.ui.delete_btn.clicked.connect(self.removeItem)
        self.products.ui.table_2.cellChanged.connect(self.recalculatePrice) 

    #lấy danh sách giỏ hàng của khách hàng
    def getCart(self):
        global id
        global cursor
        cursor.execute("Select masp, tensp,giasanpham,soluong,tongtien from ctgiohang where makh =?",id)
        row= cursor.fetchall()
        cart = queryToList(row)
        self.products.populateCart(cart)
    
    #chọn sản phẩm thêm vào giỏ hàng
    def chooseItem(self):
        global id
        global cursor
        self.products.ui.table_2.insertRow(self.products.ui.table_2.rowCount())

        # curRow index of products table
        curRow = self.products.ui.table.currentRow()
        #curRowCart is current row index of cart table
        curRowCart = self.products.ui.table_2.rowCount()-1
        #print(curRowCart)
        # create item
        for i in range(5):
            if i == 3:
                item = QTableWidgetItem(str(1))
                
            elif i == 4:
                item = QTableWidgetItem(str(int(self.products.ui.table_2.item(curRowCart,2).text())))
                item.setFlags(Qt.ItemIsEditable)
            else:
                text = self.products.ui.table.item(curRow,i).text()
                item = QTableWidgetItem(text)
                item.setFlags(Qt.ItemIsEditable)
                
            item.setTextAlignment(Qt.AlignCenter)
            self.products.ui.table_2.setItem(curRowCart,i,item)
        # add item to database of shoping cart
        productID = self.products.ui.table.item(curRow,0).text()
        productName = self.products.ui.table.item(curRow,1).text()
        productPrice= self.products.ui.table.item(curRow,2).text()
        productQuantity= self.products.ui.table_2.item(curRowCart,3).text()
        cursor.execute("exec proc_themCTGIOHANG ?,?,?,?,?",id,productID,productName,productPrice,productQuantity)
        cursor.commit()

    def recalculatePrice(self,row,col):
        if col == 3:
            price = QTableWidgetItem(str(int(self.products.ui.table_2.item(row,2).text()) * int(self.products.ui.table_2.item(row,col).text())))
            item = QTableWidgetItem(price)
            item.setFlags(Qt.ItemIsEditable)
            item.setTextAlignment(Qt.AlignCenter)
            self.products.ui.table_2.setItem(row,4,item)

    def removeItem(self):
        global id
        global cursor
        curRow = self.products.ui.table_2.currentRow()

        cursor.execute("exec proc_xoa1dongCTGH ?,?",id,self.products.ui.table_2.item(curRow,0).text())
        cursor.commit()
        self.products.ui.table_2.removeRow(curRow)

    # tạo đơn hàng
    def createOrder(self):
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        if (self.products.ui.table_2.rowCount() < 1):
            self.ui.messBox.setText("Giỏ hàng trống")
            self.ui.messBox.show()
            return
        global cursor
        global id
        cursor.execute("select diachikh from khachhang where makh = ?",id)
        address = cursor.fetchone()[0]
        #create order
        orderID = randomword(10)
        cursor.execute("exec proc_themdonhang ?,?,?,?,?", orderID, address, "Chưa giao",id,None)
        try:
            # create order detail
            productsNum = self.products.ui.table_2.rowCount()
            for i in range(productsNum):
                productID = self.products.ui.table_2.item(i,0).text()
                quantity = int(self.products.ui.table_2.item(i,3).text())
                #price = int(self.products.ui.table_2.itemText(4))
                cursor.execute("exec proc_themCTDH ?,?,?,?", orderID, productID, quantity, random.randrange(5000,300000))
            cursor.commit()
            
            self.ui.messBox.setText("Đặt hàng thành công\nMã đơn hàng là: "+orderID)
        except:
            self.ui.messBox.setText("Đặt hàng thất bại")
        self.ui.messBox.show()

    def populateSmolCategory(self):
        global cursor
        #get ID of father category
        # create query to get id
        q = "select madm from danhmuc where tendm = N'"+ self.products.ui.category.itemText(self.products.ui.category.currentIndex())+"'"
        cursor.execute(q)
        id = cursor.fetchone()
        ### populate smol category
        q ="select tendm from danhmuc where dmcha ='"+id[0]+"'"
        cursor.execute(q)
        row = cursor.fetchall()
        self.smolcategory = queryToList(row)
        self.products.ui.category_smol.clear()

        for x in self.smolcategory:
            self.products.ui.category_smol.addItem(x[0])

    def ProductListByCategory(self):
        global cursor
        #user search for item

        if (self.isPage == False):
            self.pageNumber = 1
            self.products.ui.table.clearContents()
        else:
            self.isPage = False


        # create query to get list of product
        q = "Select masp, tensp, giaban, loaisp from sanpham where loaisp = N'" +self.products.ui.category_smol.itemText(self.products.ui.category_smol.currentIndex())+"'"
        q+="order by tensp desc offset("+ str(self.pageNumber*10) +") rows fetch next(10) rows only"
        #print(q)
        cursor.execute(q)
        row = cursor.fetchall()

        self.productList = queryToList(row)

        #if query return empty, revert pagenumber
        if (len(self.productList)<1):
            self.pageNumber-=1
        else:            
            self.products.populateTable(self.productList)

        self.products.ui.label.setText(str(self.pageNumber))

    def nextPage(self):
        self.isPage = True
        self.pageNumber+=1
        self.products.ui.label.setText(str(self.pageNumber))
        self.ProductListByCategory()

    def prevPage(self):
        if (self.pageNumber >1):
            self.isPage = True
            self.pageNumber-=1 
            self.products.ui.label.setText(str(self.pageNumber))
            self.ProductListByCategory()

    def searchItem(self):
        self.pageNumber =1
        self.products.ui.label.setText(str(self.pageNumber))
        # create query to get list of product
        q = "Select masp, tensp, giaban, loaisp from sanpham where tensp like N'"+self.products.ui.lineEdit.text()+"%'"
        #print(q)
        cursor.execute(q)
        row = cursor.fetchall()

        self.productList = queryToList(row)
        self.products.populateTable(self.productList)

class DKNV(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_DKNV()
        self.ui.setupUi(self)
        self.ui.birth_lnedit.setPlaceholderText("Enter format YYYY-MM-DD")
        self.ui.cancel_btn.clicked.connect(self.close)
        self.ui.signup_btn.clicked.connect(self.addEmployee)

    def addEmployee(self):
        global cursor
        # get variable from text input
        name = self.ui.name_lnedit.text()
        phone = self.ui.phone_lnedit.text()
        address =self.ui.address_lnedit.text()
        email =self.ui.email_lnedit.text()
        cID = self.ui.id_lnedit.text()
        birth = self.ui.birth_lnedit.text()
        self.ui.messBox = QMessageBox()
        self.ui.messBox.setWindowTitle("Thông báo")
        cursor.execute("insert into nhanvien values (?,?,?,?,?,?,?,?,?,?,?,?)",randomword(10),name,address,phone,0,cID,email,birth,0,"Chưa làm","Thường",randomword(10))
        cursor.commit()
        try:
            
       
            self.ui.messBox.setText("Đăng ký nhân viên thành công!\nVài ngày nữa nhân sự sẽ liên lạc bạn")
        except:
            self.ui.messBox.setText("Đăng ký thất bại")

        self.ui.messBox.show()

class TTNV(QWidget):
    def __init__(self):
        global id 
        global cursor
        QWidget.__init__(self)
        self.ui = Ui_TTNV()
        self.ui.setupUi(self)
        #initialize information on gui
        cursor.execute("Select * from nhanvien where manv=?",id)
        row = cursor.fetchall()
        row = queryToList(row)

        # set label
        self.ui.MaNV.setText(row[0][0])
        self.ui.TenNV.setText(row[0][1])
        self.ui.addr.setText(row[0][2])
        self.ui.Phone.setText(row[0][3])
        self.ui.WorkMonth.setText(str(row[0][4]))
        self.ui.cmnd.setText(row[0][5])
        self.ui.email.setText(row[0][6])
        self.ui.date.setText(row[0][7])
        self.ui.income.setText(str(row[0][8]))
        self.ui.type.setText(row[0][10])

        #populate table to view income history
        cursor.execute("select ngaynhanluong,luongcung,luongthuong,tongluong from lichsuluong where manv=?",id)
        row = cursor.fetchall()
        row = queryToList(row)
        
        self.ui.table.setColumnCount(4)
        self.ui.table.setRowCount(len(row))

        # set column headers name for table
        self.ui.table.setHorizontalHeaderItem(0,QTableWidgetItem("Ngày nhận lương"))
        self.ui.table.setHorizontalHeaderItem(1,QTableWidgetItem("Lương cứng"))
        self.ui.table.setHorizontalHeaderItem(2,QTableWidgetItem("Lương thưởng"))
        self.ui.table.setHorizontalHeaderItem(3,QTableWidgetItem("Tổng lương"))

        # set column width
        header = self.ui.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # now populate the table with data
        for i in range(len(row)):
            for j in range(len(row[i])):                   
                item = QTableWidgetItem(str(row[i][j]))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(i,j,item)
        self.ui.table.resizeRowsToContents()

class Menu_NS(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Menu_NS()
        self.ui.setupUi(self)  
        self.nv = Detail()  # set work status of each employee
        self.nv1= Detail()  # register work today for employee
        self.view = DSDD()
        self.pay = Detail()
        self.pay.ui.table.setEditTriggers(QAbstractItemView.DoubleClicked)

        #set welcome name
        global cursor
        global id
        cursor.execute("select tennv from nhanvien where manv =?",id)
        self.ui.name_label.setText(cursor.fetchone()[0])

        #button event
        self.ui.signout_btn.clicked.connect(self.close)
        self.ui.fire_btn.clicked.connect(self.fire)
        self.ui.register_btn.clicked.connect(self.registerToday)
        self.ui.pay_btn.clicked.connect(self.payIncome)

        self.nv.ui.table.cellChanged.connect(self.updateEmployeeWork)
        self.nv1.ui.table.cellChanged.connect(self.updateRegister)
        self.ui.view_btn.clicked.connect(self.viewNV)
        self.view.ui.ok_btn.clicked.connect(self.viewNV)
        self.view.ui.table.cellClicked.connect(self.viewNVIncome)
        self.pay.ui.table.cellChanged.connect(self.updatePayIncome)
    
    def updatePayIncome(self,row,col):
        if (col == 3):
            global cursor
            employeeID = self.pay.ui.table.item(row,0).text()
            money = self.pay.ui.table.item(row,2).text()
            #print(employeeID)
           # print(money)
            
            try:
                cursor.execute("exec proc_traluong ?, ?",employeeID,money)
                cursor.commit()
            except:
                self.messBox = QMessageBox()
                self.messBox.setWindowTitle("Thông báo")
                self.messBox.setText("Cập nhật vào database thất bại")
                self.messBox.show()
    
    def payIncome(self):
        global cursor
        self.pay.ui.groupBox.setTitle("Khen thưởng")
        self.pay.ui.label.setText("Khen thưởng nhân viên")
        cursor.execute("select manv,tennv from nhanvien")
        row = cursor.fetchall()
        row = queryToList(row)
        self.pay.populateTableByPay(row)
        self.pay.show()

    def viewNVIncome(self,row,col):
        global id
        id = self.view.ui.table.item(row,0).text()
        self.incomeHistory = TTNV()
        self.incomeHistory.show()

    def viewNV(self):
        global cursor
        date = str(self.view.ui.dateEdit.date().toPython())
        cursor.execute("select nv.manv,tennv,ngaydiemdanh from diemdanh join nhanvien nv on nv.manv = diemdanh.manv where diemdanh.ngaydiemdanh =?",date)
        row = cursor.fetchall()
        row = queryToList(row)
        

        self.view.populateTable(row)
        self.view.show()
    
    def updateRegister(self,row,col):
        global cursor
        employeeID = self.nv1.ui.table.item(row,0).text()
        today = date.today().isoformat()
        try:
            cursor.execute("insert into DIEMDANH values (?,?)",employeeID,today)
            cursor.commit()
        except:
            self.messBox = QMessageBox()
            self.messBox.setWindowTitle("Thông báo")
            self.messBox.setText("Điểm danh thất bại hoặc nhân viên đã điểm danh trong hôm nay rồi")
            self.messBox.show()

    def registerToday(self):
        global cursor
        self.nv1.ui.groupBox.setTitle("Danh sách")
        self.nv1.ui.label.setText("Danh sách nhân viên")
        ## query to populate table
        cursor.execute("select manv,tennv from nhanvien where loainv = N'Thường'")
        row= cursor.fetchall()
        row = queryToList(row)
        
        self.nv1.populateTableByEmployeeRegister(row)
        self.nv1.show()

    def updateEmployeeWork(self,row,col):
        global cursor
        employeeID = self.nv.ui.table.item(row,0).text()
        combobox = self.nv.ui.table.cellWidget(row,2)
        if isinstance(combobox,QComboBox):
            employeeStatus = combobox.currentText()
        #update in db
        cursor.execute("update nhanvien set tinhtrang=? where manv =?",employeeStatus,employeeID)
        cursor.commit()

    def fire(self):
        global cursor
        #reuse deatail widget here
        
        self.nv.ui.groupBox.setTitle("Danh sách")
        self.nv.ui.label.setText("Danh sách nhân viên")
        
        ## query to populate table
        cursor.execute("select manv,tennv,tinhtrang from nhanvien where loainv = N'Thường'")
        row= cursor.fetchall()
        row = queryToList(row)
        #
        self.nv.populateTableByEmployeeWork(row)
        self.nv.show()


# convert result query to list
def queryToList(row):
    strg = []
    for i in row:
        tmp = []
        for j in i:
            tmp.append(j)
        strg.append(tmp) 
    return strg

#generate random word
def randomword(length):
   letters = string.ascii_uppercase+string.digits
   return ''.join(random.choice(letters) for i in range(length))

if __name__=="__main__":
    app = QApplication()
    
    apply_stylesheet(app, theme='light_pink.xml',invert_secondary = True)
    window = gui()
    window.show()
    exit(app.exec_())