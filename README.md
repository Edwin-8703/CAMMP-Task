# Project Overview: Foundations of Numerical Methods and Floating-Point Errors

This project explores foundational numerical methods, floating-point representation, absolute and relative error, and the convergence of Taylor series approximations for the exponential function \(e^x\).

The experiments use Python and NumPy to perform numerical calculations and Matplotlib to visualize approximation errors.

# Project Structure

CAMMP-Task/
│
├── floating_point_representation.py
├── absolute_relative_errors.py
├── Taylor_series_approximations.py
├── error_visualization.py
└── README.md

# Prerequisites and Requirements

- Python
- Libraries: NumPy and Matplotlib

Install the required libraries using: python3 -m pip install numpy matplotlib

# Script Overview and Usage

1. Floating-Point Representation (floating_point_representation.py)

Investigates floating-point number representation, precision, machine epsilon, and rounding behavior. 
The script demonstrates why some decimal numbers cannot be represented exactly in binary floating-point arithmetic.

Run: python3 floating_point_representation.py

2. Absolute and Relative Errors(absolute_relative_errors.py)

Examines the difference between exact and approximate values using absolute and relative error.

Absolute error: reference value - approximation value

Relative error: Absolute error / reference value

Run: python3 absolute_relative_errors.py

3. Taylor Series Approximations (Taylor_series_approximations.py)

Approximates \(e^x\) using a finite Taylor series and compares the result with NumPy's exponential function. The experiment uses \(x=0.4\) and investigates the effect of increasing the number of terms.

Run: python3 Taylor_series_approximations.py

4. Error Convergence Visualization (error_visualization.py)

Calculates approximation errors for different numbers of Taylor series terms and plots the results on a logarithmic scale. The script saves the generated visualization as `taylor_error.png`.

Run: python3 error_visualization.py

Key Results and Observations

- Floating-point representation: Some decimal values cannot be represented exactly in binary floating-point arithmetic, producing small rounding errors.
- Machine precision: Machine epsilon illustrates the finite precision of floating-point numbers.
- Taylor series convergence: For \(x=0.4\), increasing the number of terms generally brings the approximation closer to the reference value.
- Error reduction: The truncation error decreases rapidly as additional terms are included. Floating-point rounding can eventually limit further improvement.
- Visualization: A logarithmic error plot makes it easier to compare errors across different orders of magnitude.

Conclusion

These experiments demonstrate the importance of numerical precision, error measurement, and convergence when using computers to solve mathematical problems. 
They also show how Taylor series provide increasingly accurate approximations and how floating-point limitations affect numerical calculations.
