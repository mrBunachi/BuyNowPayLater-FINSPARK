import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000
nghe_nghiep_options = ['Học sinh', 'Sinh viên', 'Văn phòng', 'Lao động tự do', 'Buôn bán', 'Khác']
gioi_tinh_options = [0, 1]  # 0: Nam, 1: Nữ
tinh_thanh_options = ['Hà Nội', 'Hồ Chí Minh', 'Đà Nẵng', 'Cần Thơ', 'Hải Phòng', 'Đà Lạt']

data = []

for _ in range(n):
    nghe = np.random.choice(nghe_nghiep_options)
    gioi_tinh = np.random.choice(gioi_tinh_options)
    tinh_thanh = np.random.choice(tinh_thanh_options)
    
    # Tuổi
    if nghe == 'Học sinh':
        tuoi = np.random.randint(12, 18)
    else:
        tuoi = int(np.clip(np.random.normal(35, 10), 18, 60))
    
    # Thu nhập (triệu)
    if nghe == 'Học sinh':
        thu_nhap = 0.0
    else:
        thu_nhap = round(np.random.uniform(10, 100), 2)
    
    # Tần suất mua hàng (lần/tháng)
    tan_suat = np.random.randint(0, 31)
    
    # Giá trị trung bình đơn hàng (triệu)
    gia_tri_tb = round(np.random.uniform(0.05, 10), 2)
    
    # Số lần trả tiền trễ
    tra_tre = np.random.randint(0, 6)
    
    # Nợ xấu
    no_xau = 1 if tra_tre >= 1 else 0
    
    # DSR
    dsr = 0.0 if nghe == 'Học sinh' else round(np.random.uniform(0.1, 0.7), 2)
    
    # Chấp nhận
    if no_xau == 1 and dsr > 0.5:
        chap_nhan = np.random.choice([0, 1], p=[0.8, 0.2])
    elif no_xau == 1 or dsr > 0.5:
        chap_nhan = np.random.choice([0, 1], p=[0.6, 0.4])
    else:
        chap_nhan = np.random.choice([0, 1], p=[0.4, 0.6])
    
    data.append([
        tuoi, gioi_tinh, thu_nhap, tinh_thanh, nghe,
        tan_suat, gia_tri_tb, tra_tre, no_xau, dsr, chap_nhan
    ])

df = pd.DataFrame(data, columns=[
    'tuoi', 'gioi_tinh', 'thu_nhap', 'tinh_thanh', 'nghe_nghiep',
    'tan_suat_mua_hang', 'gia_tri_tb_don', 'so_lan_tra_tre', 'no_xau', 'dsr', 'chap_nhan'
])

# Hiển thị 10 dòng đầu
print(df.head(10))

# Lưu file CSV
df.to_csv('du_lieu_tin_dung.csv', index=False)

# Thống kê chap_nhan
print("Phân bố chap_nhan:")
print(df['chap_nhan'].value_counts())
