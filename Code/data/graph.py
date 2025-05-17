import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []


with open("scoreMLP.sc", "r") as f:
    for line in f:
        data = line.split(" ")
        x.append(data[0])
        y2.append(float(data[1]))

with open("score.sc", "r") as f:
    counter = 0
    for line in f:
        data = line.split(" ")
        print( x[counter] == data[0])
        y1.append(float(data[1]))
        counter+=1
plt.plot(x, y1, label ='SVM')
plt.plot(x, y2, '-.', label ='CNN')

plt.xlabel("vibration hertz of data")
plt.ylabel("accuracy")
plt.legend()
plt.title('accuracy based on vibration hertz')
plt.show()