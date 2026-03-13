# Dự Đoán Điểm Toán Của Học Sinh (Predict Student Scores)
- Dự án này sử dụng Machine Learning để dự đoán điểm môn Toán (math score) của học sinh dựa trên các yếu tố nhân khẩu học và kết quả học tập khác (như điểm đọc, điểm viết, trình độ học vấn của phụ huynh, v.v.).
- Mô hình học máy cốt lõi được sử dụng trong phiên bản hiện tại là Hồi quy tuyến tính (Linear Regression), kết hợp cùng Pipeline của scikit-learn để tự động hóa quá trình tiền xử lý dữ liệu.
## Yêu cầu hệ thống (Prerequisites)
- Để chạy được dự án này, bạn cần cài đặt Python (khuyến nghị phiên bản 3.7 trở lên) và các thư viện cần thiết. Bạn có thể cài đặt thông qua pip:
`pip install pandas scikit-learn`
## Cấu trúc dữ liệu
Dự án yêu cầu file dữ liệu đầu vào có tên StudentScore.xls đặt ở cùng thư mục với file mã nguồn
Các đặc trưng (Features) bao gồm:
- **Target (Biến mục tiêu):**math score (Điểm toán)
- **Numerical Features (Dữ liệu số):**reading score, writing score
- **Ordinal Features (Dữ liệu thứ bậc):**parental level of education, gender, lunch, test preparation course
- **Nominal Features (Dữ liệu định danh):**race/ethnicity
## Luồng xử lý (Pipeline)
Mã nguồn sử dụng ColumnTransformer và Pipeline để tiền xử lý dữ liệu một cách tối ưu trước khi đưa vào mô hình:
1. **Xử lý dữ liệu bị thiếu (Imputation):** Sử dụng giá trị trung vị (median) cho dữ liệu số và giá trị xuất hiện nhiều nhất (most_frequent) cho dữ liệu phân loại.
2. **Chuẩn hóa dữ liệu (Scaling):** Sử dụng StandardScaler cho các cột điểm số (đọc, viết)
3. **Mã hóa dữ liệu (Encoding):** OrdinalEncoder để mã hóa các biến có tính thứ tự hoặc nhị phân.
4. **Huấn luyện:** Dữ liệu sau xử lý sẽ được đưa vào mô hình LinearRegression. (Mã nguồn cũng đã import sẵn RandomForestRegressor và SVR nếu bạn muốn thử nghiệm thay đổi mô hình).
## Đánh giá mô hình (Metrics)
Sau khi chạy, script sẽ in ra terminal các chỉ số đánh giá hiệu suất của mô hình trên tập kiểm thử (test set):
- **MAE (Mean Absolute Error):** 4.181966418321512
- **MSE (Mean Squared Error):** 28.82105656383288
- **R2 (R-Squared)**: 0.8815597679452446
Các chỉ số cho thấy mo hình sẵn sàng sử dụng với độ tin cậy cao. Các biến số như reading score và writing score đóng vai trò rất lớn trong việc đưa ra dự đoán chính xác này.