import tensorflow as tf
from tensorflow import keras


def build_simple_model() -> keras.Sequential:
    model = keras.Sequential([
        keras.layers.Input(shape=(8,)),
        keras.layers.Dense(16, activation="relu"),
        keras.layers.Dense(1, activation="sigmoid"),
    ])
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


def train_simple_model() -> keras.Sequential:
    x_train = tf.random.uniform((200, 8), minval=0, maxval=1)
    y_train = tf.cast(x_train[:, 0] + x_train[:, 1] > 1.0, tf.float32)

    model = build_simple_model()
    model.fit(x_train, y_train, epochs=5, batch_size=32, verbose=0)
    return model


if __name__ == "__main__":
    model = train_simple_model()
    print("TensorFlow example model trained successfully.")
    print("Model summary:")
    model.summary()
