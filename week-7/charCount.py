str = input("enter a string")
c = input("enter a character")
print(f"count of {c} in given string {str} using inbult methods : {str.count(c)}")

count = 0
for i in str:
    if i == c:
        count +=1
print(f"count of {c} in given string {str} without using inbult methods : {count}")

