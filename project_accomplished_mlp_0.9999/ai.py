import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy
import time
import joblib

csv = pd.read_csv("train.csv")
csv_test = pd.read_csv("test.csv")
classfier = pd.read_csv("classfier.csv")
classfier_test = pd.read_csv("test_classfier.csv")

X = csv.to_numpy()
X_test = csv_test.to_numpy()
Y = classfier.to_numpy()
Y_test = classfier_test.to_numpy()

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X)
x_test_scaled = scaler.transform(X_test)

model = tf.keras.Sequential([
     tf.keras.Input(shape = (8,)),
     tf.keras.layers.Dense(16, activation = 'relu'),
     tf.keras.layers.Dense(16, activation = 'relu'),
     tf.keras.layers.Dense(6, activation = 'softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train_scaled, Y, epochs=5)

model.evaluate(x_test_scaled, Y_test)

model.save('mlp/fault_classfication.h5')
joblib.dump(scaler, 'scaler.pkl')
