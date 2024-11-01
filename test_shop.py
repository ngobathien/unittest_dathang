# test_shop.py

import unittest
from shop import dat_hang

class TestShop(unittest.TestCase):
    
    def test_dat_hang_hop_le(self):
        ket_qua = dat_hang(1, 2, 7000000)  # Đặt 2 điện thoại với số dư 7000000
        self.assertEqual(ket_qua, "Đặt hàng thành công")

    def test_so_luong_khong_hop_le(self):
        ket_qua = dat_hang(1, 0, 7000000)  # Số lượng không hợp lệ
        self.assertEqual(ket_qua, "Số lượng không hợp lệ")

        ket_qua = dat_hang(1, -3, 7000000)  # Số lượng âm
        self.assertEqual(ket_qua, "Số lượng không hợp lệ")

    def test_so_du_khong_hop_le(self):
        ket_qua = dat_hang(1, 2, -100000)  # Số dư không hợp lệ
        self.assertEqual(ket_qua, "Số dư không hợp lệ")

    def test_so_du_khong_du(self):
        ket_qua = dat_hang(1, 3, 5000000)  # Đặt 3 điện thoại nhưng số dư không đủ
        self.assertEqual(ket_qua, "Số dư không đủ để đặt hàng")
    
    def test_dat_hang_voi_so_luong_lon(self):
        ket_qua = dat_hang(1, 100, 400000000)  # Đặt 100 điện thoại với số dư đủ
        self.assertEqual(ket_qua, "Số lượng không được vượt quá 50")

    def test_dat_hang_voi_so_luong_1(self):
        ket_qua = dat_hang(1, 1, 3000000)  # Đặt 1 điện thoại với số dư đúng
        self.assertEqual(ket_qua, "Đặt hàng thành công")
    
    def test_so_du_bang_chinh_xac_tong_tien(self):
        ket_qua = dat_hang(1, 2, 6000000)  # Số dư bằng tổng tiền
        self.assertEqual(ket_qua, "Đặt hàng thành công")

    def test_so_du_nho_hon_tong_tien(self):
        ket_qua = dat_hang(1, 2, 5999999)  # Số dư nhỏ hơn tổng tiền
        self.assertEqual(ket_qua, "Số dư không đủ để đặt hàng")

    def test_san_pham_khong_ton_tai(self):
        ket_qua = dat_hang(0, 1, 3000000)  # Sản phẩm không tồn tại
        self.assertEqual(ket_qua, "Sản phẩm không tồn tại")

        ket_qua = dat_hang(-1, 1, 3000000)  # Sản phẩm không tồn tại
        self.assertEqual(ket_qua, "Sản phẩm không tồn tại")

if __name__ == '__main__':
    unittest.main()
