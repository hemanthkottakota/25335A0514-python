def fibanocii(num):
    f =0
    s=1
    if num  == 0 or num == 1:
        print(0)
        return 
        
    print(f ,s ,end = " ")
    for _ in range(2,num):
        t = f+s
        print(t, end = " ")
        f,s = s,t

def fibanocci_recursive(num,f = 0,s = 1):
    # i = 2
    
    # if num  == 0 or num == 1:
    #     print(0)
    #     return 
    # # if num == 2:
    # #     print(f ,s ,end = " ")
    # if i == num:
    #     return
    # t = f+s
    # print(t,end = " ")
    # return fibanocci_recursive(num-1,s,t)
    if num <= 0:
        return
    
    print(f, end=" ")
    return fibanocci_recursive(num - 1, s, f + s)


while True:
    choice = int(input("\nenter 1 - recurrsion \nenter 2 - non recurssion\n 3 - exit\n"))
    if choice == 1:
        num = int(input("enter a postive number"))
        value = fibanocci_recursive(num)
    elif choice == 2:
        num = int(input("enter a postive number"))
        value = fibanocii(num)
    else:
        break
    
    