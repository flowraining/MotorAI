import pandas as pd
from sklearn.model_selection import train_test_split
import os
import numpy as np
from os import listdir
from os.path import isfile, join, isdir
import time

def get_all_file(directory):
     all_files = []

     # Walk through the directory and its subdirectories
     for foldername, subfolders, filenames in os.walk(directory):
          for filename in filenames:
               # Get the full path of the file
               file_path = os.path.join(foldername, filename)
               # Append the file path to the list
               all_files.append(file_path)

     return all_files
directory = get_all_file("D:\\D_Demand\\data\\data")
def file_class_to_int(file):
     file_s = os.path.basename(file).strip("csv").strip(".")
     print(file_s)
     time.sleep(1)
     if (file_s == "Healthy"):
          return 0
     if (file_s == "Debris"):
          return 1
     if (file_s == "Erosion"):
          return 2
     if (file_s == "Flaking"):
          return 3
     if (file_s == "Lubrication"):
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
          if (file[len(file) - 3:] == "csv"):
               X, Y= split_file(file)
               put(total, X)
               put(total_class, Y)
     X_train, X_test, Y_train, Y_test = train_test_split(total, total_class, test_size=0.99999)
     df_train = pd.DataFrame(X_train, columns = ['ia1', 'ib2', 'X_Vibration3', 'Flux4', 'TI_Temp5', 'Z_Vibration6', 'Acc_Temp7', 'Y_Vibration8'])
     df_train_class = pd.DataFrame(Y_train, columns = ['motor_health'])
     df_test = pd.DataFrame(X_test, columns = ['ia1', 'ib2', 'X_Vibration3', 'Flux4', 'TI_Temp5', 'Z_Vibration6', 'Acc_Temp7', 'Y_Vibration8'])
     df_test_class = pd.DataFrame(Y_test, columns = ['motor_health'])
     df_train.to_csv(i, index = False)
     df_train_class.to_csv(o, index = False)
     df_test.to_csv(i_test, index = False)
     df_test_class.to_csv(o_test, index = False)
     
combine_file("train.csv", "classfier.csv", "test.csv", "test_classfier.csv")
