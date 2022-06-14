from matplotlib import pyplot as plt
from genetic.genetic import Genetic
from genetic.genetic import fitness
from load.LoadData import stops

def plot_improvement(ax, stop_list,full_trip_list,steps):
    progress = []
    for solution in steps:
        progress.append(fitness(stop_list,full_trip_list,solution))
    ax.plot(progress)
    ax.set_ylabel('Distance')
    ax.set_xlabel('Iteration step')

def genetic_run(stop_list,full_trip_list,generations=500, population_size=100, elite_size=3, mutation_rate=0.1):
    genetic = Genetic(stop_list,full_trip_list,population_size=population_size, elite_size=elite_size, mutation_rate=mutation_rate)
    population = genetic.initial_population()
    best_solution = genetic.best_solution(population)
    steps = [best_solution]

    for i in range(generations):
        population = genetic.next_generation(population)
        best_solution = genetic.best_solution(population)
        steps.append(best_solution)

    fig, ax = plt.subplots(ncols=1, figsize=(10,5))
    plot_improvement(ax,stop_list,full_trip_list,steps)
    plt.show()

    return best_solution
