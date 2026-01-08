import math
def prime(num):
    for i in range(2,int(math.sqrt(num//2))+1):
        if num%i == 0:
            print(f"{num} is not a prime number")
            return
    print(f"{num} is prime number")






def recurPrime(num,i = 2):
    count = 0
    if i>math.sqrt(num):
        return True
    if num % i == 0:
        return False
    else:
        return recurPython(num,i+1)


while True:
    choice = int(input("enter 1 - recurrsion \nenter 2 - non recurssion\n 3 - exit"))
    if choice == 1:
        num = int(input("enter a number"))
        call = recurPrime(num)
        print(f"{num} is prime\n") if call !=0 else print(f"{num} is not a prime\n")
    elif choice == 2:
        num = int(input("enter a number"))
        prime(num)
    else:
        break