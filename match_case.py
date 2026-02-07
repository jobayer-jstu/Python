x= int(input("Enter a number: "))
match x:
    case _ if x < 10:
        print("number is less than 10")
    case _ if 10<=x >20:
        print("10 to 20")
    case _ if 21<= x> 30:
        print("20 to 30")

    case _ if 30<=x > 40:
        print("number is 30 to 40")
    case _ :
        print("getter than 40")
