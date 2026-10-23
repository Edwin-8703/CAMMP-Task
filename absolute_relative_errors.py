test1=0.4
test2=0.3

test_result = test1 - test2
true_result = 0.1

#Calculating the absolute error
absolute_error = abs(test_result - true_result)
print("Absolute Error:", absolute_error) 

#Calculating the relative error
relative_error = absolute_error / abs(true_result)
print("Relative Error:", relative_error) 

#Calculating the percentage error
percentage_error = relative_error * 100
print("Percentage Error:", percentage_error, "%")   

