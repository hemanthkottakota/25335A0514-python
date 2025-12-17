import numpy as np

names = np.chararray((3,), itemsize=10)
names[:] = ['hemanth', 'kumar', 'kottakota']

print(names)
print(names.upper())
print(names.count(b'a'))