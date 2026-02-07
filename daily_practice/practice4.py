for i in range(1,11):
    print(i)

for i in (range(10,0,-1)):
    print(i)

for i in range(20):
    if i%2==0 :
        print(i)

name="jobayer"
for i in name:
    print(i)

for i in range(6):
    print("*"*i)


for i in reversed(range(6)):
    print("*"*i)

for i in range(1,6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


ta=int(input("enter table number: "))
for i in range(1, 11):
    print(ta,"*",i,"=", ta*i)