str = input("enter a string")
print(str.replace('a','x'))

li = list(str)
for i in range(len(li)):
    if li[i] == 'a':
        li[i] = 'x'
        

print("".join(li))