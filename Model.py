import numpy as np
import random
import matplotlib.pyplot as plt 

def GenesPopulation(sizeofgenom,n):
    return [[1 if random.random()>0.5 else 0 for _ in range(sizeofgenom)] for _ in range(n)]

def Coding(c):
    r = len(c) 
    sum = [c[i+2] * 2**(r-(i+3)) for i in range(len(c)-2)]
    return float((-1)**c[0] * np.exp((-1)**c[1]) * np.sum(sum))

def Fitness(x):
    x = Coding(x)
    return abs(x**3 - x**2 + 1)
    # return x**2
    # return -1*(x**2) + 2*x +10 
    # return -x**2+10*x+1

def EliteSelection(fitness_genes,eliteSize,Minimize = False):
    
    zipedGenes = list(zip(population,fitness_genes))
    
    ranking = sorted(zipedGenes, key=lambda x: x[1], reverse = Minimize)
    bin, y = zip(*ranking)

    sorted_genes = list(bin)

    elite = sorted_genes[:eliteSize]
    rest_of_genes = sorted_genes[eliteSize:]
    
    random.shuffle(elite)
    return elite, rest_of_genes , y 

def Crossover(elite,genes,amountOfPairs):

    k = 0
    s = random.randint(0,len(genes[0]))
    for i in range(amountOfPairs):
        for _ in range(len(elite[i+k])):
            elite1 = elite[i+k][:s] + elite[i+1+k][s:]
            elite2 = elite[i+1+k][:s] + elite[i+k][s:]
        elite[i+k] = elite1
        elite[i+1+k] = elite2
        k += 1

    return elite + genes

def Mutation(x):
    for i in range(len(x)):
        if random.random() < 0.01:
            if x[i] == 0:
                    x[i] = 1
            else:
                    x[i] = 0
    return x

elite_fitness_gens = []
n = 0
n_list = []
x_list = []
mean_list = []
y_list = []

# Tworzymy populacje 
population = GenesPopulation(7,100)

for _ in range(1000):
    
    while True:
        
        # Ocena populacji 
        fitness_genes = list(map(Fitness,population))

        # Selekcja 
        elite_genes, rest_of_genes, sorted_fitness_genes = EliteSelection(fitness_genes,30,Minimize=False)

        # Warunek stopu
        elite_fitness_gens.append(np.mean(sorted_fitness_genes))
        if n > 0:
            if abs(elite_fitness_gens[n] - elite_fitness_gens[n-1]) < 10:
                break
        
        # Krzyżowanie
        crossed_genes = Crossover(elite_genes,rest_of_genes,10)
        
        # Mutacja
        population = list(map(Mutation,crossed_genes))


        n += 1
    
    mapedvalues = list(map(Fitness,population))
    zipedelites = list(zip(population,mapedvalues))
    ranking = sorted(zipedelites, key=lambda x: x[1],reverse=False)
    bin, y = zip(*ranking)
    n_list.append(n)
    x_list.append(Coding(bin[0]))
    y_list.append(y[0])
    mean_list.append(elite_fitness_gens)

    population = GenesPopulation(7,100)
    elite_fitness_gens = []
    n = 0


print(np.mean(x_list))
print(f"Największa wartość: {max(x_list)}")
print(f"Najmniejsza wartość: {min(x_list)}")
print(np.mean(n_list))

x = np.linspace(-2, 2, 100)
y = abs(x**3 - x**2 + 1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax2.hist(x_list,color = 'red')
ax1.axvline(x = 0, color = 'black')
ax1.axhline(y = 0 , color='black')
ax1.plot(x, y)
ax1.scatter(x_list,y_list, color = 'red', s=50, alpha=.3)
plt.show()