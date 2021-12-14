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
        return(rFib(num-1) + rFib(num-2))

print(rFib(-6))

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
            return(rTrib(num-1) + rTrib(num-2) + rTrib(num-3))

print(rTrib(-8))


