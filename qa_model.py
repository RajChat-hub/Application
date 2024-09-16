import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding, Concatenate
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

# Step 1: Define the model
def build_model(vocab_size, embedding_dim, max_seq_length):
    # Encoder
    encoder_input = Input(shape=(max_seq_length,))
    encoder_embedding = Embedding(input_dim=vocab_size, output_dim=embedding_dim)(encoder_input)
    encoder_lstm = LSTM(64, return_sequences=False, return_state=True)
    _, encoder_state_h = encoder_lstm(encoder_embedding)

    # Decoder
    decoder_input = Input(shape=(max_seq_length,))
    decoder_embedding = Embedding(input_dim=vocab_size, output_dim=embedding_dim)(decoder_input)
    decoder_lstm = LSTM(64, return_sequences=True)(decoder_embedding, initial_state=[encoder_state_h, encoder_state_h])
    decoder_dense = Dense(vocab_size, activation='softmax')(decoder_lstm)
    
    model = Model(inputs=[encoder_input, decoder_input], outputs=decoder_dense)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Step 2: Prepare training data
def prepare_data(questions, contexts, answers, tokenizer, max_seq_length):
    tokenized_questions = tokenizer.texts_to_sequences(questions)
    tokenized_contexts = tokenizer.texts_to_sequences(contexts)
    tokenized_answers = tokenizer.texts_to_sequences(answers)
    
    questions_padded = pad_sequences(tokenized_questions, maxlen=max_seq_length, padding='post')
    contexts_padded = pad_sequences(tokenized_contexts, maxlen=max_seq_length, padding='post')
    answers_padded = pad_sequences(tokenized_answers, maxlen=max_seq_length, padding='post')
    
    answers_categorical = to_categorical(answers_padded, num_classes=len(tokenizer.word_index) + 1)
    
    return [questions_padded, contexts_padded], answers_categorical

# Example data
questions = ["What is the capital of France?"]
contexts = ["The capital of France is Paris."]
answers = ["Paris"]

# Tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + contexts + answers)

max_seq_length = 10
vocab_size = len(tokenizer.word_index) + 1

# Prepare data
x_train, y_train = prepare_data(questions, contexts, answers, tokenizer, max_seq_length)

# Build and train the model
model = build_model(vocab_size, embedding_dim=50, max_seq_length=max_seq_length)
model.fit(x_train, y_train, epochs=10, batch_size=1)

# Step 3: Save the model
model.save('chat_raj_model.h5')
print("Model saved as 'chat_raj_model.h5'.")
