from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a simple model
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(784,)))
print("Keras is working!")
