import pandas as pd
from sklearn.model_selection import train_test_split
import os
import numpy as np

directory = os.listdir(".")
def file_class_to_int(file):
     file_s = file.strip("csv").strip(".")
     if (file_s == "healthy"):
          return 0
     if (file_s == "debris"):
          return 1
     if (file_s == "erosion"):
          return 2
     if (file_s == "flaking"):
          return 3
     if (file_s == "no lubrication"):
          return 4
     return 5
def put(total, X):
     for item in X:
          total.append(item)
def split_file(file):
     print(file)
     df = pd.read_csv(file)
     np_X = df.values.tolist()
     np_Y = [file_class_to_int(file)] * len(df)
     return [np_X, np_Y]
def combine_file(i, o, i_test, o_test):
     total = []
     total_class = []
     for file in directory:
          if (file != "train_test_split.py"):
               X, Y= split_file(file)
               put(total, X)
               put(total_class, Y)
     X_train, X_test, Y_train, Y_test = train_test_split(total, total_class, test_size=0.25)
     df_train = pd.DataFrame(X_train, columns = ['ia1', 'ib2', 'X_Vibration3', 'Flux4', 'TI_Temp5', 'Z_Vibration6', 'Acc_Temp7', 'Y_Vibration8'])
     df_train_class = pd.DataFrame(Y_train, columns = ['motor_health'])
     df_test = pd.DataFrame(X_test, columns = ['ia1', 'ib2', 'X_Vibration3', 'Flux4', 'TI_Temp5', 'Z_Vibration6', 'Acc_Temp7', 'Y_Vibration8'])
     df_test_class = pd.DataFrame(Y_test, columns = ['motor_health'])
     df_train.to_csv(i, index = False)
     df_train_class.to_csv(o, index = False)
     df_test.to_csv(i_test, index = False)
     df_test_class.to_csv(o_test, index = False)
     
combine_file("train.csv", "classfier.csv", "test.csv", "test_classfier.csv")
