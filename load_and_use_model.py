import tensorflow as tf
import numpy as np

# Step 1: Load the model from the .h5 file
loaded_model = tf.keras.models.load_model('model.h5')
print("Model loaded from 'model.h5'.")

# Step 2: Prepare some data to test the model
x_test = np.random.random((10, 32))  # 10 samples, 32 features

# Step 3: Make predictions
predictions = loaded_model.predict(x_test)

print("Predictions:")
print(predictions)
