
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np

# Step 1: Define and compile the model
model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(32,)))  # Increased size of the first layer
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))  # Added an additional hidden layer
model.add(Dense(10, activation='softmax'))  # Output layer for 10 classes

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 2: Generate and split data
x_train = np.random.random((5000, 32))  # Increased sample size
y_train = np.random.randint(10, size=(5000, 10))  # 10 classes, one-hot encoded

# Split the data into training and validation sets
split_index = int(0.8 * len(x_train))
x_val, y_val = x_train[split_index:], y_train[split_index:]
x_train, y_train = x_train[:split_index], y_train[:split_index]

# Step 3: Define callbacks for saving the model and early stopping
checkpoint = ModelCheckpoint('model1.keras', save_best_only=True, monitor='val_loss', mode='min', verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', mode='min', patience=5, verbose=1)

# Step 4: Train the model with validation data and callbacks
model.fit(
    x_train, y_train,
    epochs=20,  # Increased epochs
    batch_size=64,  # Increased batch size
    validation_data=(x_val, y_val),  # Validation data
    callbacks=[checkpoint, early_stopping]  # Callbacks
)

# Step 5: Save the final model (in case early stopping does not save the best model)
model.save('model1.keras')
print("Model saved as 'model1.keras'.")

