USE DB_LAB2
GO

--procedure DONHANG va CTDH
/*1) thêm đơn hàng (proc_themdonhang)
	-Tham số: @MaDH, @diachiDH, @tinhtrang, @makh, @manv
	-Lưu ý: ngày thêm đơn hàng được tạo tự động trong proc,
		không cần tạo tự động ở app
*/
CREATE PROCEDURE proc_themdonhang
@madh CHAR(15), @diachiDH nvarchar(150), @tinhtrang nvarchar(15),@makh CHAR(15), @manv CHAR(15)
AS BEGIN
	BEGIN TRAN
		IF EXISTS(SELECT MaDH FROM dbo.DONHANG WHERE MaDH = @madh) ROLLBACK TRAN
		--IF NOT EXISTS(SELECT MaKh FROM dbo.KHACHHANG WHERE @maKH = MaKH) ROLLBACK TRAN
		DECLARE @date DATE
		SET @date = CONVERT(NVARCHAR,YEAR(GETDATE())) + '-'+ CONVERT(NVARCHAR,MONTH(GETDATE())) +'-'+ CONVERT(NVARCHAR,DAY(GETDATE()))
		IF @manv = NULL OR @manv = ''
			INSERT DONHANG VALUES(@madh,@date,@diachiDH,@tinhtrang,0,@makh,NULL)
		ELSE
			INSERT DONHANG VALUES(@madh,@date,@diachiDH,@tinhtrang,0,@makh,@manv)
		COMMIT TRAN
END

--them 1 CTDH
/*2) thêm 1 CTDH cho 1 đơn hàng(proc_themCTDH)
	-Tham số: @madh, @masp, @soluong, @giagiam
	-Lưu ý: tenSP,giasanpham được lấy từ trong database ra
		không cần nhập tenSP,giaban vào
		thành tiền được tính tự động
		bên đơn hàng cũng được cập nhật lại tongtien khi thêm 1 CTDH
*/
CREATE PROCEDURE proc_themCTDH
@madh CHAR(15),@masp CHAR(15), @soluong int, @giagiam int
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT madh FROM dbo.DONHANG WHERE @madh = MaDH) ROLLBACK TRAN
		IF NOT EXISTS(SELECT masp FROM dbo.SANPHAM WHERE @masp = MaSP) ROLLBACK TRAN
		IF EXISTS(SELECT masp,madh FROM ctdh WHERE @madh = MaDH AND @masp = MaSP) ROLLBACK TRAN
		DECLARE @giasanpham INT, @thanhtien INT, @tensp nvarchar(30)
		SET @tensp = (SELECT tensp FROM dbo.SANPHAM WHERE @masp = masp)
		SET @giasanpham = (SELECT giaban FROM dbo.SANPHAM WHERE @masp = masp)
		SET @thanhtien = (@giasanpham * @soluong) - @giagiam
		INSERT CTDH VALUES(@madh,@masp,@tensp,@giasanpham,@soluong,@giagiam,@thanhtien)
		UPDATE dbo.DONHANG
		SET tongtien = tongtien + @thanhtien
		WHERE MaDH = @madh
		COMMIT TRAN
end
--procedure CTGIOHANG
--Them 1 san pham vao gio hang
/*
	3) thêm 1 sản phẩm vào giỏ hàng (proc_themCTGIOHANG)
	-Tham số: @MaKH, @MaSP, @tenSP, @giaSP, @soluong
	-Lưu ý: không cần nhập tổng tiền do được tính tự động ở proc
*/
CREATE PROCEDURE proc_themCTGIOHANG
@MaKH CHAR(15), @MaSP CHAR(15),@tenSP NVARCHAR(30), @giaSP INT, @soluong INT
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT makh FROM dbo.KHACHHANG WHERE @makh = MaKH) ROLLBACK TRAN
		IF NOT EXISTS(SELECT masp FROM dbo.SANPHAM WHERE @masp = masp) ROLLBACK TRAN
		DECLARE @tongtien INT
		SET @tongtien = @giaSP * @soluong
		INSERT CTGIOHANG VALUES(@MaKH, @MaSP, @tensp, @giaSP,@soluong,@tongtien)
		COMMIT TRAN
END
--xoa 1 san pham trong gio hang
/*
	4) xóa 1 sản phẩm trong giỏ hàng(proc_xoa1dongCTGH)
	-Tham số: @MaKH, @MaSP
*/
CREATE PROCEDURE proc_xoa1dongCTGH
@MaKH CHAR(15), @MaSP CHAR(15)
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT makh FROM dbo.KHACHHANG WHERE @makh = MaKH) ROLLBACK TRAN
		IF NOT EXISTS(SELECT masp FROM dbo.SANPHAM WHERE @masp = masp) ROLLBACK TRAN
		DELETE FROM dbo.CTGIOHANG WHERE @MaSP = MaSP AND @MaKh = MaKH
		COMMIT TRAN
END

--xoa het san pham trong gio hang cua khach hang
/*
	5) xóa hết Chi tiết giỏ hàng của 1 khách hàng (proc_xoahetCTGIOHANG)
	-Tham số: @MaKH
*/
CREATE PROCEDURE proc_xoahetCTGIOHANG
@MaKH CHAR(15)
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT makh FROM dbo.KHACHHANG WHERE @makh = MaKH) ROLLBACK TRAN
		DELETE FROM dbo.CTGIOHANG WHERE MaKH = @makh
		COMMIT tran
END

--procedure CTKHO
--them hoac cap nhat 1 san pham vao kho kho
/*
	6) thêm hoặc cập nhật 1 sản phẩm trong kho (proc_themCTKHO)
	-Tham số: @MaKho, @MaSP, @tenSP, @soluong
	-Lưu ý: procedure này làm được cả insert và update
		Khi trong bảng CTKHO chưa có sản phẩm này thì sẽ insert vào
		Khi trong bảng đã có dữ liệu này rồi thì sẽ update số
		lượng tồn của sản phẩm
*/
CREATE PROCEDURE proc_themCTKHO
@MaKho CHAR(15), @MaSP CHAR(15), @tenSP NVARCHAR(30), @soluong INT
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT @MaKho FROM dbo.KHO WHERE @MaKho = MaKho) ROLLBACK TRAN
		IF EXISTS(SELECT MaSP FROM dbo.CTKHO WHERE @MaKho = MaKho AND @MaSP = MaSP)
			BEGIN
				UPDATE dbo.CTKHO
				SET soLuongTon = soLuongTon + @soluong
				WHERE @MaKho = MaKho AND @MaSP = MaSP
			END
		ELSE
			BEGIN
				INSERT CTKHO VALUES(@MaKho, @MaSP, @tenSP, @soluong)
			END
		COMMIT TRAN
END
--procedure LICHSUNHAPXUAT
--them 1 LICHSUNHAPXUAT
/*
	7) Thêm 1 phiếu nhập hoặc xuất kho(proc_THEMLICHSUNHATXUAT)
	-Tham số: @MaPhieu, @MaKho, @loai, @NVphutrach, @diachiNX
	-Lưu ý: tham số NgayThucHien đã được tạo tự động bằng proc
*/
CREATE PROCEDURE proc_THEMLICHSUNHATXUAT
@MaPhieu CHAR(15), @MaKho CHAR(15), @loai NVARCHAR(15), @NVphutrach CHAR(15), @diachiNX NVARCHAR(150)
AS BEGIN
	BEGIN TRAN
		IF EXISTS (SELECT MaPhieu FROM dbo.LICHSUNHAPXUAT WHERE @MaPhieu = MaPhieu) ROLLBACK TRAN
		IF NOT EXISTS (SELECT MaKho FROM dbo.KHO WHERE MaKho = @MaKho) ROLLBACK TRAN
		DECLARE @ngay DATE
		SET @ngay = CONVERT(NVARCHAR,YEAR(GETDATE())) + '-'+ CONVERT(NVARCHAR,MONTH(GETDATE())) +'-'+ CONVERT(NVARCHAR,DAY(GETDATE()))
		INSERT LICHSUNHAPXUAT VALUES(@MaPhieu, @MaKho, @loai,@ngay,@NVphutrach, @diachiNX)
		COMMIT TRAN
END
--thêm 1 CTNX 
/*
	8) thêm 1 chi tiết nhập xuất cho 1 phiếu (proc_themCTNX)
	-Tham số: @MaPhieu, @MaSPNX, @tenSPNX, @soluongNX
	-Lưu ý: sau khi thêm 1 CTNX thì bên CTKHO cũng sẽ đồng thời cập nhật
		lại số lượng tồn, nếu xuất thì số lượng tồn bị giảm
*/
CREATE PROCEDURE proc_themCTNX
@MaPhieu CHAR(15), @MaSPNX CHAR(15), @tenSPNX NVARCHAR(30),@soluongNX INT
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS(SELECT maphieu FROM dbo.LICHSUNHAPXUAT WHERE @MaPhieu = MaPhieu) ROLLBACK TRAN
		IF NOT EXISTS(SELECT masp FROM dbo.SANPHAM WHERE masp = @MaSPNX) ROLLBACK TRAN
		INSERT CTNX VALUES(@MaPhieu, @MaSPNX, @tenSPNX, @soluongNX)
		DECLARE @KHO CHAR(15)
		SET @KHO = (SELECT MaKho FROM dbo.LICHSUNHAPXUAT WHERE @MaPhieu = MaPhieu)
		DECLARE @loai NVARCHAR(15)
		SET @loai = (SELECT loai FROM dbo.LICHSUNHAPXUAT WHERE @MaPhieu = MaPhieu)
		IF @loai = N'Xuất'
			BEGIN     
				SET @soluongNX = @soluongNX * (-1)
				EXEC proc_themCTKHO @MaKHO = @KHO, @MaSP = @MaSPNX, @tenSP = @tenSPNX, @soluong = @soluongNX
			END
		ELSE
			EXEC proc_themCTKHO @MaKHO = @KHO, @MaSP = @MaSPNX, @tenSP = @tenSPNX, @soluong = @soluongNX
		COMMIT TRAN
END

--procedure LICHSULUONG
--tra luong cho NV (chỉ cần nhập MaNV với lương thưởng)
/*
	9) Trả lương cho nhân viên (proc_traluong)
	-Tham số: @MaNV, @luongthuong
	-Lưu ý: chỉ cần nhập MaNV với lương thưởng trong tháng đó
		ngày nhận lương được tạo tự động ngay trong thời gian 
		thực thi procedure
*/
CREATE PROCEDURE proc_traluong
@MaNV CHAR(15), @luongthuong INT
AS BEGIN
	BEGIN TRAN
		IF NOT EXISTS (SELECT MaNV FROM dbo.NHANVIEN WHERE MaNV = @MaNV) ROLLBACK TRAN
		DECLARE @luongcung INT, @tongluongnhan INT, @ngaynhanluong date
		SET @luongcung = (SELECT luong FROM dbo.NHANVIEN WHERE MaNV = @MaNV)
		SET @tongluongnhan = @luongcung + @luongthuong
		SET @ngaynhanluong = CONVERT(NVARCHAR,YEAR(GETDATE())) + '-'+ CONVERT(NVARCHAR,MONTH(GETDATE())) +'-'+ CONVERT(NVARCHAR,DAY(GETDATE()))
		INSERT LICHSULUONG VALUES(@MaNV,@ngaynhanluong,@luongcung,@luongthuong,@tongluongnhan)
		COMMIT TRAN
END

--procedure SANPHAM
--cập nhật thông tin sản phẩm
/*
	10) Cập nhật thông tin sản phẩm (proc_capnhatsanpham)
	-Tham số: @MaSP, @tenSP, @giaban, @loaisp, @makho, @MaDM
	-Lưu ý: cập nhật tất cả thông tin của 1 sản phẩm(không thể thay đổi MaSP)
		tự động cập nhật lại tất cả thông tin của MaSP này ở các bảng khác chứ thông tin của nó(CTDH,CTGIOHANG,CTKHO,CTNX)
*/
CREATE PROCEDURE proc_capnhatsanpham
@MaSP CHAR(15), @tenSP NVARCHAR(30), @giaban INT, @loaisp NVARCHAR(15), @makho CHAR(15), @MaDM CHAR(15)
AS BEGIN 
	BEGIN TRAN
		IF NOT EXISTS(SELECT masp FROM dbo.SANPHAM WHERE @masp = masp) ROLLBACK TRAN 
		IF NOT EXISTS(SELECT makho FROM kho WHERE @makho = MaKho) ROLLBACK TRAN
		UPDATE dbo.SANPHAM
		SET tenSP = @tensp, giaBan = @giaban, loaiSP = @loaiSP, MaKho = @makho, MaDM = @MaDM
		WHERE MaSP = @MaSP
		UPDATE dbo.CTDH
		SET tenSP = @tensp, giaSanPham = @giaban
		WHERE MaSP = @MaSP
		UPDATE dbo.CTDH
		SET thanhtien = (soLuong * giaSanPham) - giaGiam
		WHERE MaSP = @MaSP
		UPDATE dbo.CTGIOHANG
		SET tenSP = @tensp, giaSanPham = @giaban
		WHERE MaSP = @MaSP
		UPDATE dbo.CTGIOHANG
		SET tongtien = (soLuong * giaSanPham)
		WHERE MaSP = @MaSP
		UPDATE dbo.CTKHO
		SET tenSP = @tensp
		WHERE MaSP = @MaSP
		UPDATE dbo.CTNX
		SET tenSP = @tensp
		WHERE MaSP = @MaSP
		COMMIT TRAN
END
