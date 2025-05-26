import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# โหลดข้อมูล
df = pd.read_csv('data/gpt_maindata_max.csv')
X = df.drop("183", axis=1)
y = df["183"]

# แบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# สร้างและฝึกโมเดล
model = RandomForestClassifier()
model.fit(X_train, y_train)

# ทำนายและประเมินผล
y_pred = model.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

joblib.dump(model, 'ML-model/gpt-pose_model_max.pkl')