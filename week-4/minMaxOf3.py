num1,num2,num3 = map(int,input("enter three numbers").split(" "))
# print("maximum of given numbers :",max(li))
# print("minimum of given numbers :",min(li))
# if num1>num2:
#     if num1>num3:
#         print(num1)
#     else:
#         print(num3)
# else:
#     if num2>num3:
#         print(num2)
#     else:
#         print(num3)
        
maximum = num1 if num1 > num2 and num1 > num3 else num2 if num2 > num3 else num3
minimum = num1 if num1 < num2 and num1 < num3 else num2 if num2 < num3 else num3
print(f"maximum of given numbers : {maximum}")
print(f"minimum of three numbers : {minimum}")

                    
        
