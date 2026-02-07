# def isMean(x, y):
#     print("gmean is : ", (x*y)/(x+y))

# def isGreater(x, y):
#     if(x> y):
#         print("first number is greater.")
#     elif(x ==y):
#         print("number is equal.")
#     else:
#         print("second number is greater.")
# a= 5 
# b= 6
# isMean(a,b)
# isGreater(a,b)

# c= 162
# d= 156
# isMean(c, d)
# isGreater(c,d)


def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    
    print("average is: " ,sum / len(number))

average(4, 5, 6, 8)

average(int(input()))
