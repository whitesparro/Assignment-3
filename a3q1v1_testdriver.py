# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 141
# Instructor: Gang Li

from testing_blackbox_recentTrend import recentTrend

# i.e. the recentTrend() function is sitting in a file called "testing_blackbox_recentTrend.py"

# The empty list is a special case, so always test it!
test = []
expected = None
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# A list of fewer than 20 elements.
test = [0, 1, 2]
expected = 2
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# Testing a list of 2 elements, a One and a Zero.
test = [1, 0]
expected = 1
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# Testing a list of 20 elements, where each is a unique value.
test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
expected = 19
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# Testing a list of 20 elements, with the smaller values before the bigger values.
test = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
expected = 1
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# Testing a list of 20 elements, with the bigger values before the smaller values.
test = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
expected = 1
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)

# Testing a list of a mixture of elements.
test = [0, 1, 2, 0, 1, 2, 2, 1, 0, 1, 0, 2, 0, 2, 1, 1, 0, 1, 0]
expected = 1
result = recentTrend(test)
if result != expected:
    print("Testing recentTrend() with", test, "   Expected:", expected, " Got: ", result)
