def joba():
    print("welcome code")
joba()

def with_pera(name):
    print("hello", name)

with_pera("jobayer")
with_pera("hossen")

def add(a,b):
    print("result- ",a+b)

add(5,6)



def square(a):
    print("square is - ",a*a)

square(12)

def even_odd(number):
    if number%2==0:
        print("even")
    else:
        print("odd")

even_odd(
    int(input("enter number:"))
)

def maxx(a,b,c):

    print(max(a,b,c))



z=list(map(int,(input("enter 3 number: ").split())))

maxx(z[0],z[1],z[2])

