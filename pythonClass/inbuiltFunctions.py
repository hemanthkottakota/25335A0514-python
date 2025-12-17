a = "10"
print(type(a))
print(int(a))
print(float(int(a)))
print(bool(a))
def iter():
    a = 0
    while True:
        yield a
        print(a)
        a+=1
        
a = iter()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
