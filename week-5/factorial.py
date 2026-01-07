
def factorial(n):
    fact = 1
    # if n == 0 or n == 1:
    #     return 1
    for i in range(1,n+1):
        fact*=i
    return fact
    
def factorial_recursion(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial_recursion(n-1)



while True:
    choice = int(input("enter 1 - recurrsion \nenter 2 - non recurssion\n 3 - exit"))
    if choice == 1:
        num = int(input("enter a postive number"))
        value = factorial_recursion(num)
    elif choice == 2:
        num = int(input("enter a postive number"))
        value = factorial(num)
    else:
        break
    print(f'"factorial of {num} : {value}')