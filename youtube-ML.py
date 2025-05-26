import pandas
from sklearn.model_selection import train_test_split

df = pandas.read_csv("data/test_dataset.csv")

X = df.drop('150', axis=1)
y = df['150']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)