import itertools

num_generator = itertools.count(3)
cycle_generator = itertools.cycle(iter([next(num_generator) for i in range(0, 5)]))
for i in range(0, 20):
    print(next(cycle_generator))
