import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load data
df = pd.read_csv('du_lieu_tin_dung.csv')

# One-hot encode các biến categorical
df_encoded = pd.get_dummies(df, columns=['nghe_nghiep', 'tinh_thanh'])

# Tách features và target
X = df_encoded.drop(columns=['chap_nhan'])
y = df_encoded['chap_nhan']

# Lấy 800 mẫu đầu làm train, 200 mẫu sau làm test
X_train = X.iloc[:800].reset_index(drop=True)
y_train = y.iloc[:800].reset_index(drop=True)
X_test  = X.iloc[800:1000].reset_index(drop=True)
y_test  = y.iloc[800:1000].reset_index(drop=True)

# Định nghĩa model RandomForest với cấu hình "phức tạp"
model = RandomForestClassifier(
    n_estimators=1000,
    max_depth=20,
    min_samples_split=12,
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict trên tập test
y_pred = model.predict(X_test)

# In ra bảng đánh giá
report = classification_report(y_test, y_pred)
print("Classification Report:\n")
print(report)

# Lưu model và danh sách cột
joblib.dump(model, 'model_bnpl.pkl')
joblib.dump(X.columns.tolist(), 'model_columns.pkl')
