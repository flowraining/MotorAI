debris = open("D:\\data\\utd\\debris.csv", "r").readlines()
erosion = open("D:\\data\\utd\\erosion.csv","r").readlines()
flaking = open("D:\\data\\utd\\flaking.csv", "r").readlines()
healthy = open("D:\\data\\utd\\healthy.csv", "r").readlines()
nolub = open("D:\\data\\utd\\no lubrication.csv", "r").readlines()
sd = open("D:\\data\\utd\\single defect.csv", "r").readlines()



def int_to_file(num):
     if (num == 0):
          return healthy
     if (num == 1):
          return debris
     if (num == 2):
          return erosion
     if (num == 3):
          return flaking
     if (num == 4):
          return nolub
     return sd
def check(in_file, out_file):
     test = open(in_file, "r")
     classfier = open(out_file, "r")
     content = test.readlines()
     content_class = classfier.readlines()
     for i in range(1, len(content)):
          check = content[i]

          c_file = int_to_file(int(content_class[i]))

          if (not check in c_file):
               raise Exception("you coded something wrong")
check("test.csv", "test_classfier.csv") 
