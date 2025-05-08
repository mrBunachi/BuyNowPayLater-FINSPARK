import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

def random_job():
    return np.random.choice(['van_phong', 'lao_dong', 'tu_kinh_doanh', 'hoc_sinh', 'khac'])

data = pd.DataFrame({
    'tuoi': np.random.randint(18, 60, n),
    'gioi_tinh': np.random.choice([0, 1], n),  # 0: Nam, 1: Nữ
    'thu_nhap': np.random.randint(3000000, 20000000, n),
    'tinh_thanh': np.random.choice(['HCM', 'HN', 'DaNang', 'CanTho', 'HaiPhong'], n),
    'nghe_nghiep': [random_job() for _ in range(n)],
    'tan_suat_mua_hang': np.random.randint(0, 10, n),
    'gia_tri_tb_don': np.random.randint(100000, 5000000, n),
    'so_lan_tra_tre': np.random.poisson(1, n),
    'no_xau': np.random.choice([0, 1], n, p=[0.9, 0.1]),
    'dsr': np.round(np.random.uniform(0.0, 1.5, n), 2)  # debt-to-income ratio
})

# Gán nhãn: nếu thu nhập cao, DSR thấp, ít nợ xấu => chấp nhận
data['chap_nhan'] = ((data['thu_nhap'] > 8000000) &
                     (data['dsr'] < 0.5) &
                     (data['so_lan_tra_tre'] == 0) &
                     (data['no_xau'] == 0)).astype(int)

data.to_csv('khach_hang_bnpl.csv', index=False)
print("Đã tạo file 'khach_hang_bnpl.csv'")
