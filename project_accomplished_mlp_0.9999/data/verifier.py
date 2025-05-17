import tensorflow as tf
import pandas as pd
import joblib
import numpy as np

import matplotlib.pyplot as plt
path = "D:\\D_Demand\\data\\"
model = tf.keras.models.load_model(path + 'mlp\\fault_classfication.h5')



csv_test = pd.read_csv(path + "test.csv")
classfier_test = pd.read_csv(path + "test_classfier.csv")

X_test = csv_test.to_numpy()
Y_test = classfier_test.to_numpy()
scaler = joblib.load(open(path + "scaler.pkl", "rb"))
X_test = scaler.transform(X_test)

Y_pred = model.predict(X_test)
num_err = 0
for i in range(len(Y_test)):
     if (np.argmax(Y_pred[i]) != Y_test[i][0]):
          num_err += 1
X_test = [x for x in X_test if (str(x[0]) != 'nan')]
Y_test = [x for x in Y_test if (str(x) != 'nan')]
with open("scoreMLP.sc", "a+") as w:
     w.write("general " + str(1 - num_err/len(Y_test)) + "\n")
#model.evaluate(X_test, Y_test)
w.close()

