#given program
print(5+3*2)
print(2*3**2)
print(2**3**2)# associativity right to left
print((2**3)**2)

#experimentation
"""
split() - used to split a string with specific character
map() - used to point every value in a iterable
"""
a,b,c = map(int,input("enter three subject marks").split(" "))
average1 = a+b+c/3
average2 = (a+b+c)/3
print(average1)#gives wrong average value due to operator precedence
print(average2)