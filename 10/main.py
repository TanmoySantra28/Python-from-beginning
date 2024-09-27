n = int(input("Enter number = "))
match n:
    # if n is 0
    case 0:
        print("The number is 0")
    #case with if-condition
    case _ if n%2==0:
        print("The number is Even")
    case _:
        print("The number is Odd")
 