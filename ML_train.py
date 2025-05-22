import numpy
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dropout, Dense


data_test = numpy.array([_ for _ in range(10)])
leght_test = 3
def create_sequence(data, seq_length):
    data_X, y = [], []
    for i in range(len(data) - seq_length):
        data_X.append(data[i:i + seq_length])
        y.append(data[i+seq_length])
    return numpy.array(data_X),numpy.array(y)
X, y = create_sequence(data_test,leght_test)
test = X.shape[0]
print(test)

# model = Sequential()
# model.add(LSTM())