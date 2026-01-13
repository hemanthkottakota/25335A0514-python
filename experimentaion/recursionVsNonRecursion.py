import time


def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial_recursion(n-1)



def factorial(n):
    fact = 1
    # if n == 0 or n == 1:
    #     return 1
    for i in range(1,n+1):
        fact*=i
    return fact


num = int(input("enter a number"))
initialTime = time.time_ns()
factorial_recursion(num)
endingTime = time.time_ns()
print(f"time taken to run factorial recursion : {endingTime - initialTime}")

initialTime = time.time_ns()
factorial(num)
endingTime = time.time_ns()
print(f"time taken to run factorial non recursion : {endingTime - initialTime}")
