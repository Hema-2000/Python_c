#calculate program on simple interest and compound interest
p=int(input("enter the principle"))
t=int(input("enter the timeperiod"))
r=int(input("enter the rate"))

x=(p*t*r)
si=x/100
print(si)

a=p*(pow(1+(r/100),t))
ci=a-p
print(ci)


#Calculate (a+b)**2

a=int(input("enter 1st num"))
b=int(input("enter 2 nd num"))
c=(a+b)**2
print(c)
print(pow(a+b,2))

