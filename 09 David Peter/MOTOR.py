import os
import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
path = "D:\\full"
directory = [i for i in os.scandir(path)]
files = []



while (len(directory) > 0):
     new = directory.pop()
     if (new.is_file()):
          files.append(new.path)
     else:
          new_next = [i for i in os.scandir(new)]
          for item in new_next:
               directory.append(item)


X = []
for file in files:
     df = pd.read_csv(file)
     for item in df.head(1000).values.tolist():
          X.append(item)

y = []
for file in files:
     head, tail = os.path.split(file)
     for i in range(1000):
          y.append(head)    


print("Starting training")
X_train, X_test, y_train, y_test = train_test_split(
     X, y)
for i in range(1, 100):
     print("Fitting...")
     clf = RandomForestClassifier(max_depth=i)
     clf.fit(X_train, y_train)
     print("Scoring...")
     print(clf.score(X_test, y_test))
     
     
     
          

          

