from functional import *
import numpy as np


def test_dot():
    assert dot([1,1,1,1], [1,1,1,1]) == np.dot([1,1,1,1], [1,1,1,1]) 

def test_neuron():
    assert len(create_neuron([1,1,1,1])) == 2 and len(create_neuron([1,1,1,1])[0]) == 4 and type(create_neuron([1,1,1,1])[1]) == float

def test_trainingImprovement():
    np.random.seed(32)
    X = create_x(10000, 3)
    y = create_y(X, .3)
    neuron = create_neuron(X)
    model = train_regression(X, y, neuron, iters=1000)
    assert mse(linear_regression(X, neuron), y) > mse(linear_regression(X, model), y)