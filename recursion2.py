import sys

# Write rFib(num). Recursively compute and return numth Fibonacci value. As earlier, treat first two (num = 0, num = 1) Fibonacci vals as 0 and 1. Examples: 
# rFib(2) = 1 (0+1); 
# rFib(3) = 2 (1+1); 
# rFib(4) = 3 (1+2); 
# rFib(5) = 5 (2+3).rFib(3.65) = rFib(3) = 2, rFib(-2) = rFib(0) = 0.

def rFib(num):
    if num <= -1:
        return rFib(num * -1) * -1
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return(rFib(int(num-1)) + rFib(int(num-2)))

print(rFib(-6.2))

# Write function rTrib(num) to mimic Fibonacci, adding previous three values instead of two. First three Tribonacci numbers are 0, 0, 1, so rTrib(3) = 1 (0+0+1); rTrib(4) = 2 (0+1+1); rTrib(5) = 4 (1+1+2); rTrib(6) = 7 (1+2+4). Handle negatives and non-integers appropriately and inexpensively.

def rTrib(num):
    if num <= -1:
        return rTrib(num * -1) * -1
    if num > -1:
        if num <= 0:
            return 0
        elif num == 1:
            return 0
        elif num == 2:
            return 1
        else:
            return(rTrib(int(num-1)) + rTrib(int(num-2)) + rTrib(int(num-3)))

print(rTrib(-9.9))

# This function accepts two non-negative integer values, num1 and num2, and follows these rules:

# ackermann(0,num2) == num2+1;
# ackermann(num1,0) == ackermann(num1-1,1) if num1 > 0 (de lo contrario, ver #1);
# ackermann(num1,num2) == ackermann(num1-1,ackermann(num1,num2-1)).


def naive_ackermann(num1, num2):
    if num1 == 0:
        return num2 + 1
    elif num2 == 0:
        return naive_ackermann(num1 - 1, 1)
    else:
        return naive_ackermann(num1 - 1, naive_ackermann(num1, num2 - 1))

print(naive_ackermann(2,2))


# Zib(0) == 1;
# Zib(1) == 1;
# Zib(2) == 2;
# Zib(2n+1) == Zib(n)+Zib(n-1)+1, if n > 0 (i.e. odd values 3 and higher);
# Zib(2n) == Zib(n)+Zib(n+1)+1, if n > 1 (i.e. even values 4 and higher).
# Create the Zibonacci(num) function. What is Zibonacci(10)? Zibonacci(100)?

# Second: For a given number that might be a Zibonacci result, find the largest index that maps to that result. bestZibNum(3186) == 2467, bestZibNum(3183) == null.

def zibonacci(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num%2 == 1:
        return zibonacci(num)+zibonacci(num-1)+1
    else:
        return zibonacci(num)+zibonacci(num+1)+1

# print(zibonacci(10))
# RuntimeError: maximum recursion depth exceeded

print(sys.getrecursionlimit())
# Recursion limit is 1000
