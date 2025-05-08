from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load mô hình và các cột
model = joblib.load('model_bnpl.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form
        new = pd.DataFrame([{
            'tuoi': int(data['tuoi']),
            'gioi_tinh': int(data['gioi_tinh']),
            'thu_nhap': int(data['thu_nhap']),
            'tinh_thanh': data['tinh_thanh'],
            'nghe_nghiep': data['nghe_nghiep'],
            'tan_suat_mua_hang': int(data['tan_suat_mua_hang']),
            'gia_tri_tb_don': int(data['gia_tri_tb_don']),
            'so_lan_tra_tre': int(data['so_lan_tra_tre']),
            'no_xau': int(data['no_xau']),
            'dsr': float(data['dsr']),
        }])

        # One-hot encode
        new_encoded = pd.get_dummies(new, columns=['nghe_nghiep', 'tinh_thanh'])

        # Đảm bảo đúng các cột như khi train
        for col in model_columns:
            if col not in new_encoded.columns:
                new_encoded[col] = 0
        new_encoded = new_encoded[model_columns]

        # Dự đoán
        result = model.predict(new_encoded)[0]
        return render_template('form.html', result="CHẤP NHẬN" if result == 1 else "TỪ CHỐI")
    except Exception as e:
        return f"Lỗi: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
