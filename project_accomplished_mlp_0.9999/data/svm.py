from sklearn import svm
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy
import time
import joblib
import matplotlib.pyplot as plt
path = "D:\\D_Demand\\data\\"
# csv = pd.read_csv(path + "train.csv")
# csv_test = pd.read_csv(path + "test.csv")
# classfier = pd.read_csv(path + "classfier.csv")
# classfier_test = pd.read_csv(path + "test_classfier.csv")


# N = 100000
# X = csv.to_numpy()[:N]
# X_test = csv_test.to_numpy()[:N]
# Y = classfier.to_numpy()[:N]
# Y_test = classfier_test.to_numpy()[:N]

# scaler = StandardScaler()
# x_train_scaled = scaler.fit_transform(X)
# x_test_scaled = scaler.transform(X_test)

# print("SVM started")
# regr = svm.SVC(decision_function_shape='ovo', verbose=1)
# regr.fit(x_train_scaled, Y.ravel())
# Y_pred = regr.predict(x_test_scaled)





# plt.show()
# joblib.dump(regr, 'SVM-class.pkl')
# joblib.dump(scaler, 'scaler_SVM.pkl')

N = 100000
regr = joblib.load(open(path + "SVM-class.pkl", "rb"))
scaler = joblib.load(open(path + "scaler_SVM.pkl", "rb"))
csv_test = pd.read_csv(path + "test.csv")
classfier_test = pd.read_csv(path + "test_classfier.csv")
X_test = csv_test.to_numpy()[:N]
Y_test = classfier_test.to_numpy()[:N]
X_test = scaler.transform(X_test)
print (X_test[:100])
Y_pred = regr.predict(X_test)

with open("score.sc", "a+") as w:
    w.write("general " + str(regr.score(X_test, Y_test)) + "\n")
w.close()