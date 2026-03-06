import random

f = open("sample2.txt", "w")

nums = []
for i in range(20):
    n = random.randint(1,100)
    f.write(str(n) + "\n")

f.close()

f = open("sample2.txt","r")
print(f.read())
f.close()