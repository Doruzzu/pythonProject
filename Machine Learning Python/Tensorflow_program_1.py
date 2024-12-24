import numpy as np
import tensorflow as tf

w = tf.Variable(0, dtype=tf.float32)
optimiser = tf.keras.optimizers.Adam(0.1)


def train_step():
    with tf.GradientTape() as tape:
        cost = w ** 2 - 10 * w + 25
    trainable_variables = [w]
    grads = tape.gradient(cost, trainable_variables)
    optimiser.apply_gradients(zip(grads, trainable_variables))
print(w)
train_step()
print(w)
print(tf.__version__)