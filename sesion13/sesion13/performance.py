import time

def medicion_rendimiento(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)


def procesar(limite: int):
    return [x**2 for x in range(limite)]

#medicion_rendimiento(lambda : procesar(50000))

import timeit

print(timeit.timeit("[x**2 for x in range(100)]"))
print(timeit.timeit("map(lambda x: x**2, range(100))"))







