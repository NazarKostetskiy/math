import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


def random_test(n):
    x = range(n)
    # список случайных равномернораспределенных действительных чисел, 4 знак после запятой
    y = [np.random.uniform() for i in x]
    # график распределения для наглядности
    plt.plot(x, y, 'o')
    plt.show()
    # тест Колмогорова-Смирнова на произвольное однородное распределение
    kstest = stats.kstest(y, 'uniform', args=(0, 1))
    # возвращает р значение и статистику
    return kstest


# если р >> alpha - значит, что распределение правильное
# https://www.dummies.com/education/math/statistics/what-a-p-value-tells-you-about-statistical-data/
if __name__ == '__main__':
    k = 10000
    alpha = 0.05
    test = random_test(k)
    print(f'Statistic: {test[0]}, P-value: {test[1]}')
    if test[1] > alpha:
        print(f'True: P-value({test[1]}) greater then alpha({alpha})')
    else:
        print(f'False: P-value({test[1]}) < alpha({alpha})')
