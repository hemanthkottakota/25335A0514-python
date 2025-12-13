import math




#area of circle using math module methods 1.pi 2.pow()
radius = int(input("enter radius"))
print(f"area of circle :{math.pi*pow(radius,radius)}")


#finding all cos,sin fundamental values
for angle in range(0,361,30):
   rad = math.radians(angle)
   print(f"sin {angle}: {round(math.sin(rad),1)}")
   print(f"cos {angle}: {round(math.cos(rad),1)}")
   print(f"tan {angle}: {round(math.tan(rad),1)}")