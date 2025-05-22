import numpy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense

data_test = numpy.array([_ for _ in range(10)])
leght_test = 3
def create_sequence(data, seq_length):
    data_X, y = [], []
    for i in range(len(data) - seq_length):
        data_X.append(data[i:i + seq_length])
        y.append(data[i+seq_length])
    return numpy.array(data_X),numpy.array(y)
Big_x, y = create_sequence(data_test,leght_test)
Big_x = Big_x.reshape((Big_x.shape[0], Big_x.shape[1], 1))

model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(leght_test, 1)))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mean_squared_error")

model.fit(Big_x,y, epochs=200, verbose=0)

model.save("ML-model/lstm_testmodel.keras")
# test_input = numpy.array([7,8,9]).reshape((1,leght_test,1))

# predicted = model.predict(test_input, verbose=0)
# print("Predicted:", predicted)