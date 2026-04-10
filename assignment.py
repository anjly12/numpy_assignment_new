import numpy as np
import matplotlib.pyplot as plt

def create_array():
    return np.arange(1, 11)
    pass

def array_arithmetic(a, b):
     return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b
    }
    pass

def slicing_example(arr):
     return {
        "first_5": arr[:5],
        "last_5": arr[-5:],
        "middle": arr[5:11],
        "reversed": arr[::-1]
    }
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

    plt.plot(x, y, label="y = x^2")
    plt.title("Graph of y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()
    pass
