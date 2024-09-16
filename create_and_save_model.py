import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# Step 1: Define and compile the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(32,)))  # Input shape with 32 features
model.add(Dense(64, activation='relu'))
model.add(Dense(10, activation='softmax'))  # Output layer for 10 classes

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 2: Train the model on dummy data
x_train = np.random.random((1000, 32))  # 1000 samples, 32 features
y_train = np.random.randint(10, size=(1000, 10))  # 10 classes, one-hot encoded

model.fit(x_train, y_train, epochs=10, batch_size=32)

# Step 3: Save the model as an .h5 file
model.save('model.h5')
print("Model saved as 'model.h5'.")
