import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from keras import layers

x = np.array(range(8))
y = np.array([1, 2, 3, 4, 5, 6, 7, 8])

inputs = keras.Input(shape=(1,), dtype=tf.int32)
hidden = layers.Dense(4, activation="relu")(inputs)
outputs = layers.Dense(1)(hidden)

model = keras.Model(inputs=inputs, outputs=outputs, name="neural_array_model")

model.summary()

loss_fn = tf.keras.losses.MeanAbsoluteError(
    reduction="auto", name="mean_absolute_error"
)

model.compile(
    loss=loss_fn,
    metrics=["accuracy"],
)

history = model.fit(x, y, batch_size=8, epochs=100, validation_split=0.01)

test_scores = model.evaluate(x, y, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])

results = model.predict(x)

print(results)

plt.plot(x, y, label="desired_results")
plt.plot(x, results, label="results")
plt.legend()
plt.show()
