# a=1
# while a<21:
#     print(a)
#     a+=1


# a=1
# while a<21:
#     if a%2==0:
#         print(a)
#     a+=1


# count=0
# a=int(input("enter range: "))
# while a>0:
#     count+=a
#     a=a-1
# print(count)



# a=int(input("enter table number: "))
# i=1
# while i<11:
#     print(a,"*",i,"=",a*i)
#     i+=1



# a=12
# geuss=0
# while geuss!=a:
#     geuss=int(input("enter number: "))
#     if(geuss>a):
#         print("too high")
#     elif geuss<a:
#         print("too low")
# print("correct")



# a=1
# while a<30 :
#     if a>25 and a%7==0:
#         break
#     print(a)
#     a=a+1


a=12345
for i in reversed(str(a)):
    print(i)