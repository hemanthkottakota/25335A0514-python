num = int(input("enter a number"))
power = int(input("enter power of the number"))
sum = 1
for _ in range(power):
    sum*=num
    
print(f"the power of {num} to the {power} is : {sum}")