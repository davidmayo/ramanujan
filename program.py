import math

# Define f(n) := The result of the Ramanujan nested radical, truncated after n levels
# 
# This function has this property:
# f(n) = sqrt(1 + (n+1) * f(n+1))
#
# This is the way we will define our recursive version.
#
# I could also solve that for f(n+1) to get a version that doesn't have to have an
# inner function, but I didn't do that.

# Mayo's version
def function_recursive(n: int) -> float:
    # You can put a function in a function in Python, no problem.
    # Not sure about in Matlab.
    def inner_function(inner_n: int, max_n: int) -> float:
        if inner_n == max_n:
            # This is the stopping condition. If we're calculating "function(10)",
            # And we've gone from 1, to 2, to 3, ... and we're at 10 now,
            # We can stop
            return 1.0
        else:
            # Otherwise, we go on to the next layer
            
            return math.sqrt(1 + (inner_n + 1) * inner_function(inner_n + 1, max_n))
            #                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            #                                    A function calling itself = recursion
    return inner_function(1, n)


# Some guy's iterative version from
# https://www.johndcook.com/blog/tag/ramanujan/
#
# A very important result from computer science: Every recursive algorithm (like what I did above)
# can be turned into an iterative algorithm (meaning something in a loop that does not have recursion).
#
# Iterative version is sometimes harder to understand than recursive version, but almost always
# performs better for computer-y reasons relating to "call stack depth limit".
# (In Python, for the particular kind of recursion I'm doing, this is not actually true, but that's not important here.)
def function_iterative(n):
    value = 1.0
    for number in range(n, 1, -1):
        value = math.sqrt(value * number + 1)
    return value


# Do some calculations
MAX_NUMBER = 50

x_values = list(range(1, MAX_NUMBER+1))
y_values_recursive = []
y_values_iterative = []

for n in x_values:
    y_values_recursive.append(function_recursive(n))
    y_values_iterative.append(function_iterative(n))

# Results
print(f"Did calculations from n=1 to n={MAX_NUMBER}")
print(f"f({MAX_NUMBER}) = {y_values_recursive[-1]} [recursive]")
print(f"f({MAX_NUMBER}) = {y_values_iterative[-1]} [iterative]")
print(f"Are all the results exactly the same? {y_values_recursive == y_values_iterative}")

# Let's plot it, why not.
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x_values, y_values_recursive, label="Iterative [Other guy]")
ax.plot(x_values, y_values_iterative, label="Recursive [Mayo]")
ax.set_xlabel("n")
ax.set_ylabel("f(n)")
ax.set_title("Ramanujan infinite radical thingy")
ax.legend()

# Plots are on top of each other.
plt.show()