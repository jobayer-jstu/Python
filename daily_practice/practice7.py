a=5
b=7
c=9
if a>b>c:
    print(a)
elif b>a>c:
    print(b)
else:
    print(c)

print(max(a,b,c))


a,b= b,a
print(a)
print(b)

year=int(input("enter a year: "))

if (year%4==0 and year%100!=0) or year%400==0:
        print("leap year")
else:
        print("not")

count=0
r=int(input("enter range: "))
while r>0:
    count=count+r
    r=r-1
print(count)

fact=1
for i in range(1,r+1):
    fact=fact*i
print(fact)


for i in range(1, r+1):
    for j in range( i):
        print(i, end=" ")
    print( )

for i in range(1, r+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print( )


for i in reversed(str(r)):
    print(i)


for i in range(1,10):
    if i in (3,5,7):
        continue
    print(i)