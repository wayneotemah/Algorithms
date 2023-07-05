import random

"""
# this genetic algorithm is for optimizing the value of the function of -(x**2) +5

"""
best = -10000
populations = [[random.randint(0, 1) for x in range(6)] for i in range(4)]

patents = []
new_populations = []
print()


def fitness_score():
    global populations, best
    fit_value = []

    for i in range(4):
        chromosome_value = 0

        for j in range(5, 0, -1):
            chromosome_value += populations[i][j] * (2 ** (5 - j))

        chromosome_value = (
            -1 * chromosome_value if populations[i][0] == 1 else chromosome_value
        )
        # print(chromosome_value)
        fit_value.append(-(chromosome_value**2) + 5)

    fit_value, populations = zip(*sorted(zip(fit_value, populations), reverse=True))
    print(fit_value)
    print(populations)

    best = fit_value[0]


def selectparent():
    global parents
    parents = populations[0:2]
    print(parents)


def crossover():
    global parents
    cross_point = random.randint(0, 5)
    print(f"random cross point: {cross_point}")
    parents = parents + tuple(
        [(parents[0][0: cross_point + 1] + parents[1][cross_point + 1: 6])]
    )
    parents = parents + tuple(
        [(parents[1][0: cross_point + 1] + parents[0][cross_point + 1: 6])]
    )

    print(f"crossover: {parents}")


def mutation():
    global populations, parents
    mute = random.randint(1, 2)
    if mute == 2:
        x = random.randint(0, 3)
        y = random.randint(0, 5)
        print("MUTATION")
        parents[x][y] = 1 - parents[x][y]
    populations = list(parents)
    print(populations)


for _ in range(1000):
    fitness_score()
    selectparent()
    crossover()
    mutation()
print("best score :")
print(best)
print("sequence........")
print(populations[0])
