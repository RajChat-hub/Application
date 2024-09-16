
import tensorflow as tf
import numpy as np

def build_model(vocab_size, embedding_dim, max_seq_length):
    inputs = tf.keras.Input(shape=(max_seq_length,))
    embedding_layer = tf.keras.layers.Embedding(vocab_size, embedding_dim)
    encoder_embedding = embedding_layer(inputs)
    encoder_lstm = tf.keras.layers.LSTM(128, return_sequences=True, return_state=True)
    encoder_output, state_h, state_c = encoder_lstm(encoder_embedding)
    decoder_lstm = tf.keras.layers.LSTM(128, return_sequences=True)
    decoder_output = decoder_lstm(encoder_output, initial_state=[state_h, state_c])
    outputs = tf.keras.layers.Dense(vocab_size, activation='softmax')(decoder_output)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)
    return model

vocab_size = 5000
embedding_dim = 50
max_seq_length = 100

model = build_model(vocab_size, embedding_dim, max_seq_length)
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

x_train = np.random.randint(0, vocab_size, size=(1000, max_seq_length))
y_train = np.random.random((1000, max_seq_length, vocab_size))

model.fit(x_train, y_train, epochs=10, batch_size=32)
model.save('chat_raj_model.h5')
print('Model saved as chat_raj_model.h5.')

