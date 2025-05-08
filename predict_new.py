import pandas as pd
import joblib

# Dữ liệu mới (1 khách hàng)
new = pd.DataFrame([{
    'tuoi': 30,
    'gioi_tinh': 0,
    'thu_nhap': 12000000,
    'tinh_thanh': 'HCM',
    'nghe_nghiep': 'van_phong',
    'tan_suat_mua_hang': 3,
    'gia_tri_tb_don': 1500000,
    'so_lan_tra_tre': 0,
    'no_xau': 5,
    'dsr': 0.3
}])

# One-hot encode giống training
full_df = pd.read_csv('khach_hang_bnpl.csv')
all_encoded = pd.get_dummies(pd.concat([full_df, new], ignore_index=True), columns=['nghe_nghiep', 'tinh_thanh'])
new_encoded = all_encoded.tail(1).drop(columns=['chap_nhan'])

# Load mô hình & dự đoán
model = joblib.load('model_bnpl.pkl')
prediction = model.predict(new_encoded)

print("Kết quả:", "CHẤP NHẬN" if prediction[0] == 1 else "TỪ CHỐI")
