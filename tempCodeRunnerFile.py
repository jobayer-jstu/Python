a=int(input("enter a number: "))
print(a)

b=int(input("enter 2nd number: "))

if(a>b):
    print(a)
else:
    print(b)

age=int(input("enter a age: "))

if(age>18):
    print("they are adult")
elif(age==18):
    print("they are 18")

even=int(input("enter number: "))

if(even%2==0):
    print("number is even")
else:
    print("not even")

n1=int(input("enter n1:"))
n2=int(input("enter n2:"))
sum=n1+n2
difference=n1-n2
product=n1*n2
quotient=n1/n2
print(sum)
print(difference)
print(product)
print(quotient)

ax=int(input("enter num: "))
if(1<=ax<=100):
    print("inside 1 to 100")
else:
    print("not inside")