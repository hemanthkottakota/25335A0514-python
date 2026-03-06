#To write a program to implement read(), readline(), readlines(), write(), writelines() methods on files.
f = open("sample.txt", "w")
f.write("25335a0514\n")
f.write("Welcome to Python lab\n")
f.writelines(["internal1\n", "internal2\n"])
f.close()

f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()

f = open("sample.txt", "r")
line = f.readline()
print(line)
f.close()

f = open("sample.txt", "r")
lines = f.readlines()
print(lines)
f.close()
