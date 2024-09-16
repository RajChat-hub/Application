import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Step 1: Define and compile the model
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10,)))  # Input shape with 10 features
model.add(Dense(64, activation='relu'))
model.add(Dense(4, activation='softmax'))  # Output layer for 4 possible results

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 2: Prepare training data
def generate_math_data(num_samples=1000):
    # Generate simple math problems and their solutions
    X = []
    y = []
    for _ in range(num_samples):
        a, b = np.random.randint(0, 10, size=2)
        operation = np.random.choice(['+', '-', '*', '/'])
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            result = a // b if b != 0 else 0  # Avoid division by zero
        
        X.append([a, b, 1 if operation == '+' else 0, 1 if operation == '-' else 0,
                  1 if operation == '*' else 0, 1 if operation == '/' else 0])
        y.append(result)
    
    # Convert labels to one-hot encoding
    y = to_categorical(y, num_classes=4)
    return np.array(X), np.array(y)

x_train, y_train = generate_math_data()

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Step 3: Save the model
model.save('chat_raj_model.h5')
print("Model saved as 'chat_raj_model.h5'.")
