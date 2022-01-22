
# Solving Travelling Salesman Problem Using Genetic Algorithm

### Done as part of the Final Project Evaluation for 19BIO201 - Intelligence of Biological Systems - 3

- It starts with a population of a random size and random pathways (the first city is the last one)
- The user chooses the number of generations to run before the genetic algorithm starts.
- By adding pathways through crossover, mutations, and random routes, the population is doubled at the end of each generation.
- Only half of the greatest will survive to the following generation, according to the survival of the fittest theory.
- In order for the algorithm to avoid becoming stuck in a local minimum solution, new paths are built at each iteration.
- Routes through crossover genetic function are produced at every generation
- Routes through mutation genetic function are also produced at each generation.

What is crossing over?

_The procedure by which two parents generate an offspring is known as crossover. As a result, it crosses a few paths in each generation's initial population. After deleting the cities from the first route, we elected to cross over the second route. A new crossing path appears as a result of this._

What is mutation? And how much types are there in this program?

_Mutation is also a straightforward process that occurs when a parent gives rise to an offspring. In this program two kinds of mutation is present, both of which are chosen at random. The first method involves picking a small section of the parent and rearranging the cities in that section to create a new route. The second method is to take a little piece of the parent and shift it to another portion of the parent, thereby creating a new route._

## By Jithin John