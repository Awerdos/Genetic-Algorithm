import numpy as np
import random
import matplotlib.pyplot as plt 

def generator_population(sizeofgenom,n):
    return [[1 if random.random()>0.5 else 0 for _ in range(sizeofgenom)] for _ in range(n)]

def coding(c):
    r = len(c) 
    sum = [c[i+2] * 2**(r-(i+3)) for i in range(len(c)-2)]
    return float((-1)**c[0] * np.exp((-1)**c[1]) * np.sum(sum))

def fitness(x):
    # return abs(x**3 - x**2 + 1)
    # return x**2
    return -1*(x**2) + 2*x +10 

def Selecting(list_,sizeofgood,sizeofpair,s):
    k = 0
    list = list_[:sizeofgood]
    random.shuffle(list)
    for i in range(sizeofpair):
        for j in range(len(list[i+k])):
            list1 = list[i+k][:s] + list[i+1+k][s:]
            list2 = list[i+1+k][:s] + list[i+k][s:]
        list[i+k] = list1
        list[i+1+k] = list2
        k += 1
    return list + list_[sizeofgood:]

def Mutation(x):
    for i in range(len(x)):
        if random.random() < 0.1:
            if x[i] == 0:
                    x[i] = 1
            else:
                    x[i] = 0
    return x

population = generator_population(7,100)
listofbest = []
epochs = 1000

for i in range(epochs):

    codinglist = list(map(coding,population))
    mapedvalues = list(map(fitness,codinglist))

    zipedlists = list(zip(population,mapedvalues))
    ranking = sorted(zipedlists, key=lambda x: x[1], reverse=True)
    bin, y = zip(*ranking)

    listofbest.append(np.mean(y))

    sorted_population = list(bin)
    cross = Selecting(sorted_population,10,5,4)

    population = list(map(Mutation,cross))

codinglist = list(map(coding,population))
mapedvalues = list(map(fitness,codinglist))
zipedlists = list(zip(population,mapedvalues))
ranking = sorted(zipedlists, key=lambda x: x[1],reverse=True)
bin, y_ = zip(*ranking)
print(f"maximum is in x = {coding(bin[0])}")

# x = np.linspace(-5,5)
# d = [fitness(x) for x in range(len(x))]

# plt.plot(x,d)
# # plt.plot(coding(bin[0]))
# plt.show()