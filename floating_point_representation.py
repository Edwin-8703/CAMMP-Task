# inspecting floating point precision in Python
import sys

# Checking how computers represent floating point numbers in Python
test1=0.4
test2=0.3

test_result = test1 - test2
print("Test Result:", test_result)

#Checking if the true result is equal to the expected result
true_result = 0.1
print("Results are equal:", test_result == true_result)

#The rounding difference between the true result and the test result

rounding_difference = abs(test_result - true_result)
print("Rounding Difference:", rounding_difference)

#machine epsilon is the smallest difference between two floating point numbers that can be represented in Python
machine_epsilon = sys.float_info.epsilon
print("Machine Epsilon:", machine_epsilon)


