n = int(input("Enter the number = "))
if(n<0):
    print("negative")
else:
    if(n<=100):
        print("Number is lesser than 100")
    elif(n<=500):
        print("Number is between 100 and 500")
    else:
        print("Number is greater than 500")