# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 141
# Instructor: Gang Li

from a3q2v1 import closest_to_zero

#Testing one zero value
test1 = 1
test2 = 0
test3 = 3
expected = 0
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)

#Testing three positive values
test1 = 1
test2 = 2
test3 = 3
expected = 1
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)

#Testing three negative values
test1 = -2
test2 = -1
test3 = -3
expected = -1
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)

#Testing a mixture of positive and negative values
test1 = -1
test2 = 2
test3 = 3
expected = -1
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)

#Testing a draw between a positive and negative value
test1 = 1
test2 = -1
test3 = 3
expected = 1
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)

#Testing two values in a draw AND a zero
test1 = 0
test2 = -1
test3 = 1
expected = 0
result = closest_to_zero(test1, test2, test3)
if result != expected:
    print("Testing recentTrend() with", test1, test2, test3, "   Expected:", expected, " Got: ", result)
