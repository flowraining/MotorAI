


means = [0] * 8


counter = 0
with open("test.csv", "r") as f:
    for line in f:
        data = line.split(",")
        for i in range(len(data)):
            try:
                means[i] += float(data[i])
            except:
                pass
        counter += 1
        
print (means)
print (counter)
means = [x / counter for x in means]
counter = 0
std = [0] * 8
with open("test.csv", "r") as f:
    for line in f:
        data = line.split(",")
        for i in range(len(data)):
            try:
                std[i] += (float(data[i]) - means[i]) ** 2
            except:
                pass
        counter += 1
std = [ (x / counter) ** (0.5) for x in std]


with open("meanstd.sc", "w") as w:
    w.write("mean: " + str(means) + "\n")
    w.write("std: " + str(std) + "\n")