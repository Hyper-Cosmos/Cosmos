import numpy as np


class AnalogyGA:
    def __init__(self, pop_size):
        self.pop_size = pop_size

    def initializingPop(self):
        initial_pop = []
        for _ in range(self.pop_size):
            random_value = round(np.random.uniform(0, 1), 2)
            initial_pop.append(random_value)

        return initial_pop


ga = AnalogyGA(pop_size=10)

populasi_awal = ga.initializingPop()
print("Bilangan acak dalam array: ", populasi_awal)