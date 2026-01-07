start,end = map(int,input("enter the starting point and ending point").split(" "))
li = [print(f"{i} : even") if i%2 ==0 else print(f"{i} : odd") for i in range(start,end+1)]
  