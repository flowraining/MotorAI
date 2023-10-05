import tensorflow as tf
import pandas as pd
from sklearn.preprocessing import StandardScaler
import time
import numpy as np
import joblib

new_model = tf.keras.models.load_model('mlp/fault_classfication.h5')

# Check it accuracy, make sure its not lying

df = pd.read_csv("erosion.csv")
scaler = joblib.load('scaler.pkl')

x_scale = scaler.transform(df.to_numpy())

for item in new_model.predict(x_scale):
     print(np.argmax(item))
time.sleep(10000)
