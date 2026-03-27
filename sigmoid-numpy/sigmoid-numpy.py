import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)

    sigmoid = 1 / (1 + np.exp(-x))
    return sigmoid
    
    pass