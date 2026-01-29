str = input("enter a string")
print(f'{str} is palindrome') if str == str[::-1] else print(f'{str} is not a palindrome')


print(f'{str} is palindrome') if str == "".join(reversed(str)) else print(f'{str} is not a palindrome')



rString = ""
for i in range(len(str)-1,-1,-1):
    rString += str[i]
     
print(f'{str} is palindrome') if str == rString else print(f'{str} is not a palindrome')
    