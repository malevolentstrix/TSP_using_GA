# BY JITHIN JOHN
# AM.EN.U4AIE20135
# CSE(AI) | B - BATCH

import numpy
import random
import itertools
import graphviz
import time
g = [None]*100

cities = [1, 2, 3, 4, 5]
citycount = 5
routecount = (citycount*(citycount - 1))/2
routes = [4, 4, 7, 3, 2, 3, 5, 2, 3, 6]
tours = [['1-2', 4], ['1-3', 4], ['1-4', 7], ['1-5', 3], ['2-3', 2],
         ['2-4', 3], ['2-5', 5], ['3-4', 2], ['3-5', 3], ['4-5', 6]]

maxdistance = 0
for i in range(len(routes)):
    maxdistance = maxdistance + routes[i]

print(cities)
print(routes)
print(tours)

populationcount = random.randrange(1, 5)*10

if (populationcount/3) % 2 != 0:
    xovercount = populationcount/3 + 1
elif (populationcount/3) % 2 == 0:
    xovercount = populationcount/3

mutationcount = (populationcount - xovercount/2)/2
mutationcount = int(mutationcount)
randomtourscount = populationcount - xovercount/2 - mutationcount
print("population: ", populationcount, " crossovers: ", xovercount,
      " mutations: ", mutationcount, " random tours: ", randomtourscount)

population = []
citysequence = []

for i in range(populationcount):

    citysequence = []
    for j in range(citycount):
        citysequence.append([])
        citysequence[j].append(cities[j])
        citysequence[j].append(random.uniform(0, 1))

    citysequence = sorted(citysequence, key=lambda i: i[1])
    citysequence2 = []
    for j in range(citycount):
        citysequence2.append(citysequence[j][0])

    population.append(citysequence2)

print(population)
for i in range(len(population)):
    print(len(population[i]), population[i])
maxgeneration = eval(input("Give generetion count: "))
generation = 0
while generation < maxgeneration:

    xovercount = int(xovercount)

    print(xovercount)

    for v in range(0, xovercount, 2):
        parent1 = population[v]
        parent2 = population[v+1]
        child = []
        partcount = random.randrange(2, len(parent1)-1)

        part1 = []
        for i in range(partcount, len(parent1)):
            part1.append(parent1[i])

        random.shuffle(part1)

        seen = False
        part2 = []
        for i in range(len(parent2)):
            seen = False
            for j in range(len(part1)):
                if part1[j] == parent2[i]:
                    seen = True
            if seen == False:
                part2.append(parent2[i])

        child = [part2] + [part1]
        child = list(itertools.chain.from_iterable(child))
        population.append(child)

    for v in range(xovercount+1, xovercount+1+mutationcount):

        way = random.randrange(0, 1)
        if way == 0:
            parent1 = population[v]
            child1 = parent1

            partcount1 = random.randrange(2, 4)
            partplace1 = random.randrange(0, len(parent1)-partcount1)
            part1 = []
            for i in range(partplace1, partplace1+partcount1):
                part1.append(parent1[i])

            random.shuffle(part1)
            for i in range(partplace1, partplace1+partcount1):
                child1[i] = part1[i-partplace1]

            population.append(child1)
        elif way == 1:
            parent2 = population[v]
            child2 = parent2

            partcount2 = random.randrange(2, 4)
            partplace2 = random.randrange(0, len(parent2)-partcount2)
            part2 = []
            for i in range(partplace2, partplace2+partcount2):
                part2.append(parent2[i])
            beforepart = []
            for i in range(0, partplace2):
                beforepart.append([parent2[i]])
            afterpart = []
            for i in range(partplace2+partcount2, len(parent2)):
                afterpart.append([parent2[i]])

            parenttomutate = beforepart + [part2] + afterpart
            if partplace2 == 0:
                move = random.randrange(1, len(parenttomutate))
            elif partplace2 == len(parent2):
                move = random.randrange(0, len(parenttomutate)-1)
            else:
                r = list(range(0, partplace2-1)) + \
                    list(range(partplace2+1, len(parenttomutate)))
                move = random.choice(r)

            parenttomutate.pop(partplace2)
            parenttomutate.insert(move, part2)
            child2 = list(itertools.chain.from_iterable(parenttomutate))

            population.append(child2)

    randomtourscount = int(randomtourscount)
    for i in range(randomtourscount):

        citysequence = []
        for j in range(citycount):
            citysequence.append([])
            citysequence[j].append(cities[j])
            citysequence[j].append(random.uniform(0, 1))

        citysequence = sorted(citysequence, key=lambda i: i[1])
        citysequence2 = []
        for j in range(citycount):
            citysequence2.append(citysequence[j][0])

        population.append(citysequence2)

    for i in range(len(population)):
        population[i].append(population[i][0])
        if len(population[i]) != len(cities)+1:
            del (population[i])[-1]

    toursdistance = []
    for i in range(len(population)):
        g[i] = graphviz.Digraph('Tour{0}'.format(
            str(i+1)), filename='TourGraph{0}'.format(str(i+1)), comment='chorr')
        tourdistance = 0
        for j in range(len(population[i])-1):
            for v in range(len(tours)):
                if tours[v][0] == (str(population[i][j])+"-"+str(population[i][j+1])):
                    tourdistance = tourdistance + tours[v][1]
                    g[i].edge('City'+str(population[i][j]), 'City' +
                              str(population[i][j+1]), label=str(tours[v][1]), color='green')
                    #graphpathvals[v] = tours[v][1]
                    print("numbers needed")
                    print(str(population[i][j]), str(
                        population[i][j+1]), tours[v][1])
                elif tours[v][0] == (str(population[i][j+1])+"-"+str(population[i][j])):
                    tourdistance = tourdistance + tours[v][1]
                    #graphpathvals[v] = tours[v][1]
                    print("numbers needed2")
                    print(str(population[i][j]), str(
                        population[i][j+1]), tours[v][1])
                    g[i].edge('City'+str(population[i][j]), 'City' +
                              (str(population[i][j+1])), label=str(tours[v][1]), color='red')
                g[i].attr(label=r'\n\nDiagram for\n{0}\n'.format(
                    str(population[i]))+' which has tour distance {0}'.format(str(tourdistance)))
        time.sleep(1)
        g[i].render()
        # g[i].view()
        toursdistance.append(tourdistance)

    result = (list(zip(population, toursdistance)))
    print(result)
    result = sorted(result, key=lambda i: i[1])
    population = []
    print("generation is: ", generation + 1)
    for i in range(len(result)):
        duplicate = False
        population.append(result[i][0])
        if result[i][1] < maxdistance:
            maxdistance = result[i][1]
            besttour = []
            besttour.append(result[i][0])
        elif result[i][1] == maxdistance:
            for j in range(len(besttour)):
                if besttour[j] == result[i][0]:
                    duplicate = True
            if duplicate == False:
                besttour.append(result[i][0])

        print("tour ", i+1, " is: ", result[i][0], " with length ",
              len(result[i][0]), " and distance is: ", result[i][1])
    print("This is the population")
    print(len((population))/2)
    population = population[:int(len(population)/2)]

    for i in range(len(population)):
        population[i] = (population[i])[:-1]

    generation = generation + 1


for i in range(len(besttour)):
    print("best tour ", besttour[i], " with distance ", maxdistance)
    