#Importing the required library for Taylor series approximations
import numpy as np

test1 = 0.4 # Input value for Taylor series approximation
true_value = np.exp(test1)  # True value of e^0.4

approximation=1.0 # Initial value for the Taylor series approximation

# Calculating the Taylor series approximation of e^x using the first 10 terms
for n in range(1, 11):
    factorial =1
    for i in range(1, n + 1):
        factorial *= i
    # Calculating the nth term of the Taylor series expansion   
    term = (test1 ** n) / factorial 

    #Adding the nth term to the approximation
    approximation += term

#error calculation
absolute_error = abs(approximation - true_value)  
relative_error = absolute_error / abs(true_value)  


print("Taylor Series Approximation of e^0.4:", approximation) 
print("True Value of e^0.4:", true_value)  
print("Absolute Error:", absolute_error)  
print("Relative Error:", relative_error) 
