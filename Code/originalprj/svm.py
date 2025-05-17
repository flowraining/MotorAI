from sklearn import svm
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

print("SVM started")
regr = svm.SVC(decision_function_shape='ovo')
regr.fit(x_train_scaled, Y.ravel())
s = str(regr.score(x_test_scaled, Y_test))
with open("score.sc", "w+") as w:
     w.write(s)
w.close()
joblib.dump(regr, 'SVM-class.pkl')
joblib.dump(scaler, 'scaler_SVM.pkl')
