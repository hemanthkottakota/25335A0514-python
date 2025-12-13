a = 10
b = 10.10
c = "hello world"
d = True
e = "10"
print("normal values")
print(a,b,c,d,e)

print("after converting all to integers")
print(int(b),int(d),int(e))
#print(int(c)) ValueError: invalid literal for int() with base 10: 'hello world'

print("after converting all to strings")
print(str(a),str(b),str(d))

print("after converting all to float")
print(float(a),float(d),float(e))
#print(float(c)) ValueError: could not convert string to float: 'hello world'

print("after converting all to boolean")
print(bool(a),bool(b),bool(c),bool(d),bool(e))