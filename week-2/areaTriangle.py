'''area of triangle by sides'''
import math
side1,side2,side3 = map(float,input("enter three sides").split(" "))
semiPerimeter = (side1+side2+side3)*0.5
area = round(math.sqrt(semiPerimeter*(semiPerimeter-side1)*(semiPerimeter-side2)*(semiPerimeter-side3)),2)
print(area)