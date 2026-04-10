import numpy as np
import matplotlib.pyplot as plt

def create_array():
       return np.arange(1, 11)
    pass

def array_arithmetic(a, b):
       return a + b
    pass

def slicing_example(arr):
    return arr[:5]
    pass

def matrix_multiplication(a, b):
    return np.dot(a, b)
    pass

def random_numbers():
    return np.random.rand(5)
    pass

def plot_graph():
    x = np.arange(0, 11)
    y = x ** 2
    plt.plot(x, y)
    plt.title("y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    pass
