import numpy as np
import tensorflow as tf
from tensorflow import keras

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Specify the letters to recognize
letters = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter the training data to only include the specified letters
letter_indices = np.argwhere(np.isin(y_train, letters)).flatten()
x_train = x_train[letter_indices]
y_train = y_train[letter_indices]

# Filter the test data to only include the specified letters
letter_indices = np.argwhere(np.isin(y_test, letters)).flatten()
x_test = x_test[letter_indices]
y_test = y_test[letter_indices]

# Reshape the data to have a depth of 1
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# Normalize the data
x_train = x_train / 255
x_test = x_test / 255

# One-hot encode the labels
y_train = keras.utils.to_categorical(y_train, len(letters))
y_test = keras.utils.to_categorical(y_test, len(letters))

# Create the model
model = keras.Sequential([
    keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(len(letters), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)
