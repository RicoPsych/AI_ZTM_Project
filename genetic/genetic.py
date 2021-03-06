import numpy as np
import random

def fitness(stop_list,full_trip_list, solution):
    assert sorted(solution) == list(range(len(stop_list)))
    fit = 0
    for i in range(len(stop_list)):
        n0 = stop_list[solution[i % len(stop_list)]]
        n1 = stop_list[solution[(i + 1) % len(stop_list)]]
        for f in full_trip_list:
            if (f.start_stop == n0 and f.end_stop == n1) or (f.start_stop == n1 and f.end_stop == n0):
                fit+=f.length
    return fit

class Genetic:
    def __init__(self,stop_list,full_trip_list, population_size=100, elite_size=1, mutation_rate=0.01):
        self.population_size = population_size
        self.elite_size = elite_size
        self.mutation_rate = mutation_rate
        self.stop_list = stop_list
        self.full_trip_list = full_trip_list

    def population_fitness(self, population):
        population_fitness = {}
        for i, individual in enumerate(population):
            # 1/fitness -> change to maximization problem
            population_fitness[i] = 1/fitness(self.stop_list,self.full_trip_list, individual)

        return {k: v for k, v in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True)}

    def best_solution(self, population):
        population_fitness = list(self.population_fitness(population))
        best_ind = population_fitness[0]
        return population[best_ind]

    def initial_population(self):
        population = []
        # Create initial population
        for i in range(self.population_size):
            solution = np.random.permutation(len(self.stop_list))
            population.append(solution)
        return population

    def selection(self, population):
        population_fitness = self.population_fitness(population)
        probability = {}
        sum_fitness = sum(population_fitness.values())
        probability_previous = 0.0
        selection = []

        for key in population_fitness:
            probability[key] = probability_previous + (population_fitness[key]/sum_fitness)
            probability_previous = probability[key]

        n = 0
        for key in population_fitness.keys():
            if n >= self.elite_size:
                break
            selection.append(population[key])
            n += 1

        for i in range(len(population) - self.elite_size):
            rand = np.random.random()
            for key in probability:
                if rand <= probability[key]:
                    selection.append(population[key])
                    break
        return selection

    def crossover_population(self, population):
        children = []
        for i in range(self.elite_size):
            children.append(population[i])

        parents1 = np.random.randint(self.elite_size, len(population), len(population) - self.elite_size)
        parents2 = np.random.randint(self.elite_size, len(population), len(population) - self.elite_size)

        for i in range(len(population) - self.elite_size):
            parent_slice = np.random.randint(0, len(self.stop_list), 2)
            if parent_slice[0] > parent_slice[1]:
                parent_slice[0], parent_slice[1] = parent_slice[1], parent_slice[0]
            child = [None] * len(self.stop_list)

            #Wstawienie do dziecka losowego fragmentu jednego z rodzic??w
            for j in range(parent_slice[0], parent_slice[1] + 1):
                child[j] = population[parents1[i]][j]
            tmp = [item for item in population[parents2[i]] if item not in child]

            k = 0
            for j in range(len(child)):
                if child[j] is None:
                    child[j] = tmp[k]
                    k += 1
            children.append(child)

        return children

    def mutate_population(self, population):
        for i in range(self.elite_size, len(population)):
            for j in range(len(population[i])):
                if np.random.random() <= self.mutation_rate:
                    swap = np.random.randint(0, len(population[i]), 1)
                    population[i][j], population[i][swap[0]] = population[i][swap[0]], population[i][j]
        return population

    def next_generation(self, population):
        selection = self.selection(population)
        children = self.crossover_population(selection)
        next_generation = self.mutate_population(children)
        return next_generation
