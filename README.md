# Hướng dẫn sử dụng Unit Test cho chức năng đặt hàng

Dự án này bao gồm các unit test để kiểm tra chức năng đặt hàng cho shop bán điện thoại, đảm bảo tính đúng đắn của hàm `dat_hang` trong file `shop.py`.

## Cách Sử Dụng Unit Test

### 1. Chạy Unit Test với `pytest`

1. Đảm bảo rằng bạn đã cài đặt `pytest`:

   pip install pytest

2. Chạy unit test bằng lệnh sau để có kết quả rõ ràng hơn:

   pytest test_shop.py

   - Để xuất báo cáo HTML, sử dụng lệnh:

     pip install pytest pytest-html

   - Lệnh này tạo ra một giao diện hiển thị kết quả chạy test bằng file html

     pytest --html=report.html

3. Mở file `report.html` trong trình duyệt để xem báo cáo chi tiết về kết quả các test.
