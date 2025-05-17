
from sklearn.neighbors import KNeighborsClassifier
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


print("KNN started")
regr = KNeighborsClassifier(n_neighbors=3)
regr.fit(X, Y.ravel())
s = str(regr.score(X_test, Y_test))
with open("score_KNN.sc", "w+") as w:
     w.write(s)
w.close()
joblib.dump(regr, 'knn-class.pkl')
