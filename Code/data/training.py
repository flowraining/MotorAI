import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy
import time
import joblib


path = "D:\\D_Demand\\data\\"
csv = pd.read_csv(path + "train.csv")
csv_test = pd.read_csv(path + "test.csv")
classfier = pd.read_csv(path + "classfier.csv")
classfier_test = pd.read_csv(path + "test_classfier.csv")

X = csv.to_numpy()
X_test = csv_test.to_numpy()
Y = classfier.to_numpy()
Y_test = classfier_test.to_numpy()

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X)
x_test_scaled = scaler.transform(X_test)


# control
normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(numpy.array(X_test))

linear_model = tf.keras.Sequential([
    normalizer,
    tf.keras.layers.Dense(units=1)
])

linear_model.predict(X_test)
linear_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.1),
    loss='mean_squared_error',
    metrics=['mean_absolute_error', 'mean_squared_error', 'accuracy']
)
linear_model.fit(x_train_scaled, Y, epochs=5)
linear_model.evaluate(x_test_scaled, Y_test)


# model = tf.keras.Sequential([
#      tf.keras.layers.Input(shape=(8,1,)),
#      tf.keras.layers.Conv1D(8, 2, activation = 'relu'),
#      tf.keras.layers.MaxPooling1D(),
#      tf.keras.layers.Flatten(),
#      tf.keras.layers.Dense(16, activation = 'relu'),
#      tf.keras.layers.Dense(32, activation = 'relu'),
#      tf.keras.layers.Dense(512, activation = 'relu'),
#      tf.keras.layers.Dense(32, activation = 'relu'),
#      tf.keras.layers.Dense(16, activation = 'relu'),
#      tf.keras.layers.Dense(8, activation = 'sigmoid')
# ])

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train_scaled, Y, epochs=5)

# model.evaluate(x_test_scaled, Y_test)

# model.save('mlp/fault_classfication.h5')
# joblib.dump(scaler, 'scaler.pkl')
