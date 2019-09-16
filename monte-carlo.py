from scipy import random
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi


def f(x):
    return x**7+x**5+x**3


def y(x):
    return 2*sin(3*x)


def g(x):
    return 1/((x+1)*(x**(1/2)))


def monte_carlo(a: float, b: float, function, n: int):
    xrand = np.zeros(n)
    area = []
    integral = 0

    for i in range(len(xrand)):
        xrand[i] = random.uniform(a, b)

    for i in range(n):
        integral += function(xrand[i])
        answer = (b - a) / n * integral
        area.append(answer)

    answer = (b-a)/n*integral
    # plt.hist(area, bins = 20, ec='black')
    # plt.show()
    print('Answer: ', answer)
    return answer


if __name__ == '__main__':
    monte_carlo(0, 1, f, 100000)  # expected 13/24
    monte_carlo(0, pi, y, 100000)  # expected 4/3
    # k = 0
    # for i in range(80):
    #     k+=monte_carlo(0.000005, 999999, g, 1000000)  # expected pi
    # print(k/80)  # ~ 2,9