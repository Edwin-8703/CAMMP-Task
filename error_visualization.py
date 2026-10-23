#importing the required libraries for error visualization
import numpy as np
import matplotlib.pyplot as plt

test1 = 0.4 # Input value for Taylor series approximation
true_value = np.exp(test1)  # True value of e^0.4

approximation=1.0 # Initial value for the Taylor series approximation

# store the absolute and relative errors for each term for visualization
absolute_errors = []
relative_errors = []    

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

    # appending the errors to the lists for visualization
    absolute_errors.append(absolute_error)
    relative_errors.append(relative_error)

#visualizing error using line graphs
plt.figure(figsize=(12, 6))

# Plot absolute error
plt.subplot(1, 2, 1)
plt.plot(range(1, 11), absolute_errors, marker='o', color='b')
plt.title('Absolute Error in Taylor Series Approximation')
plt.xlabel('Number of Terms')
plt.ylabel('Absolute Error')
plt.yscale('log')
plt.grid(True)

# Plot relative error
plt.subplot(1, 2, 2)
plt.plot(range(1, 11), relative_errors, marker='o', color='r')
plt.title('Relative Error in Taylor Series Approximation')
plt.xlabel('Number of Terms')
plt.ylabel('Relative Error')
plt.yscale('log')
plt.grid(True)

plt.tight_layout()

#saving the plot as an image file
plt.savefig("taylor_error.png", dpi=300, bbox_inches="tight")
plt.show()