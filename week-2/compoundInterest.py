p,t,r,n = map(float,input("enter principle amount, time, rate of interest,compounding frequency per year").split(" "))
ci = p*(1+(r/100)/n)**(n*t)
print(f"compund Interest : {ci}")