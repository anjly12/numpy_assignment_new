import numpy as np
import matplotlib.pyplot as plt

def create_array():
    pass
    return np.arange(1, 11)

def array_arithmetic(a, b):
    pass
    return a + b

def slicing_example(arr):
    pass
    return arr[:5]

def matrix_multiplication(a, b):
    pass
    return np.dot(a, b)

def random_numbers():
    pass
    return np.random.rand(5)

def plot_graph():
    pass
    x = np.arange(0, 11)
    y = x ** 2

    plt.plot(x, y)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
