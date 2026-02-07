a=int(input("enter a number: "))
print(a)

if(a>0):
    print("number is positive.")
elif(a<0):
    print("number is negative.")
else:
    print("number is zero.")


b=int(input("enter a number: "))

if b%3==0 and b%5==0:
    print("divisible by 3 and 5.")
else:
    print("not divisible.")

age=int(input("enter a age: "))

if age< 13:
    print("child")
elif age>=13 and age<=18:
    print("teenager")
else:
    print("adult")


c=int(input("enter a number: "))

if c%2==0 :
    print("even")
else:
    print("odd")

num=int(input("enter a number: "))

if num>=80:
    print("got A+")
elif 80> num>=60:
    print("got A")
elif 60> num> 39:
    print("got B")
else:
    print("fail")

pas= input("enter password: ")

if len(pas)<6:
    print("weak")
elif 6 <len(pas)<10:
    print("moderate")
else:
    print("strong")

