# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 141
# Instructor: Gang Li

def closest_to_zero(num1, num2, num3):
    lowest = min(abs(num1), abs(num2), abs(num3))

    if lowest == 0:
        return 0

    if (abs(num1) == abs(num2)) or (abs(num1) == abs(num3)):
        return abs(num1)
    elif abs(num2) == abs(num3):
        return abs(num2)

    if lowest == abs(num1):
        return num1
    elif lowest == abs(num2):
        return num2
    else:
        return num3
