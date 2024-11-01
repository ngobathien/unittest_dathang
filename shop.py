# shop.py

def dat_hang(ma_san_pham, so_luong, so_du):
    # Kiểm tra số lượng đặt hàng
    if so_luong <= 0:
        return "Số lượng không hợp lệ"
    
    # Kiểm tra số dư
    if so_du < 0:
        return "Số dư không hợp lệ"
    
    # Giả định giá sản phẩm
    gia_san_pham = 3000000  # Giá mỗi điện thoại (giả định)
    tong_tien = gia_san_pham * so_luong

    # Kiểm tra số dư có đủ không
    if so_du < tong_tien:
        return "Số dư không đủ để đặt hàng"

    # Kiểm tra tình trạng sản phẩm
    # Giả định rằng nếu ma_san_pham là 0 thì sản phẩm không tồn tại
    if ma_san_pham <= 0:
        return "Sản phẩm không tồn tại"
    
    # Giả định rằng không thể đặt hàng quá số lượng cho phép (ví dụ: 50 điện thoại)
    so_luong_max = 50
    if so_luong > so_luong_max:
        return f"Số lượng không được vượt quá {so_luong_max}"

    # Xử lý đặt hàng thành công
    return "Đặt hàng thành công"
