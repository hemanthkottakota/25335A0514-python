def sumList(li):
    sum = 0
    for i in li:
        sum += i
    return sum

li = list(map(int,input("enter list elements").split(" ")))

print(f"sum of elements with inbuilt functions : {sum(li)}")
print(f"sum of elements without inbuilt functions : {sumList(li)}")

