import numpy as np
arr = np.array(list(map(int,input("enter student marks").split(" "))))
print("given student marks")
for m in arr:
    print(m,end=" ,")
print()    
print(f"student total marks:{np.sum(arr)}")
print(f"student average marks:{np.mean(arr)}")
print(f"student highest marks:{np.max(arr)}")
print(f"student least marks:{np.min(arr)}")




