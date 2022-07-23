#!/usr/bin/env python

import numpy as np
import pandas as pd



#Dot product numpy also has a built in dot function but I made my own instead of using it
dot = lambda x, y : sum([a*b for a, b in zip(x,y)])

#Create a nn style neuron based on input size for this program we will use only one
create_neuron = lambda x:([np.random.rand() * 5 - 2.5 for i in range(len(x))], np.random.rand())

#Relu activation function
relu = lambda x : max([0,x])

#Linear activation function
lin = lambda x : x

#Calculate the dot product plus the bias of a neuron then feed to activation function
process_neuron = lambda x, y, func = lin : func(dot(x[0], y) + x[1])

#returns updated nueron based on error
update_neuron = lambda neur, error: (
    [i + ((((i * np.random.rand()) * (error *2)) - error)) for i in neur[0] ],
    neur[1] + ((((neur[1] * np.random.rand()) * error) - error / 2))
    
)

#Create a toy regression dataset with linear features
create_x = lambda size, var_count :  [
    [(np.random.rand() * 2 -1)  for b in range( var_count)] for i in range( size)
]
create_y = lambda x, error : [sum([i + (i * np.random.rand() * error - error / 2) for i in a]) for a in x]

#Get mean squared error
mse = lambda y1, y2, : sum([(a-b)**2 for a,b in zip(y1,y2)]) / len(y2)

#this is a null model linear regression
null_model = lambda X, y: [np.mean(y) for _ in range(len(y))]

#Convert a 2d array first to a dictionary then to a dataframe
column = lambda data, ind: [a[ind]for a in data]
x_to_df = lambda x: pd.DataFrame({ f"X{i}":column(x, i) for i in range(len(x[0]))})



#Run a linear regression
linear_regression = lambda x, neuron: [process_neuron(neuron, i) for i in x]

#check which of two neurons generates a better regression model
better_regression  = lambda x, y, neur1, neur2, fit=mse: neur1 if mse(linear_regression(x, neur1),y) < fit(linear_regression(x, neur2),y) else neur2

#take a neuron, mutate it based of mean squared error and return either the original or new one base off performance
attempt_improvement = lambda x, y, neur: better_regression(x, y, neur, update_neuron(neur,mse(linear_regression(x, neur), y)))

#Train the model
train_regression = lambda x, y, neur, iters = 50 : (
    neur if iters <=0 
    else 
        train_regression(
                            x, 
                            y, 
                            attempt_improvement(x,y,neur),
                            iters -1
                        )
)



if __name__ == "__main__":
    print("Creating Dataset")
    np.random.seed(32)
    X = create_x(10000, 3)
    y = create_y(X, .3)
    X_train, y_train = X[0:8000], y[0:8000]
    X_test, y_test = X[8000::], y[8000::]
    
    
    neuron = create_neuron(X)
    print("Generating and Training Model")
    model = train_regression(X_train, y_train, neuron, iters=1000)


    improvement = abs(mse(linear_regression(X_train, model), y_train) /mse(linear_regression(X_train, neuron), y_train) - 1) *100

    print("\nTrain Data Mean Squared Errors:")
    print(f"\tNull Model: {mse(null_model(X_train, y_train),y_train)}")
    print(f"\tUntrained Model: {mse(linear_regression(X_train, neuron), y_train)}")
    print(f"\tTrained Model: {mse(linear_regression(X_train, model), y_train)}")
    print(f"\tTraining improved model by: {'{:.2f}'.format(improvement)}%")

    improvement = abs(mse(linear_regression(X_test, model), y_test) /mse(linear_regression(X_test, neuron), y_test) - 1) *100

    print("\nTest Data Mean Squared Errors:")
    print(f"\tNull Model: {mse(null_model(X_train, y_train), y_test)}")
    print(f"\tUntrained Model: {mse(linear_regression(X_test, neuron), y_test)}")
    print(f"\tTrained Model: {mse(linear_regression(X_test, model), y_test)}")
    print(f"\tTraining improved model by: {'{:.2f}'.format(improvement)}%")











