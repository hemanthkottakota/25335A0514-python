li = list(map(int,input("enter list elements").split(" ")))
print(f"minimum : {min(li)} maximum : {max(li)}")

maxValue = minValue = li[0]
for i in range(len(li)):
    if li[i]<=minValue:
        minValue = li[i]
    if li[i]>maxValue:
        maxValue = li[i]
        
print(f"minimum : {minValue} maximum : {maxValue}")   
    

