from tensorflow.keras.models import load_model

test_model = "ML-model/lstm_testmodel.keras"

model = load_model(test_model)
print("Finish")