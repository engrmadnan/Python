a=eval(input("Enter the Percentage"))
if(100 >= a>=90):
    print("A+")
    if (a>=95):
        print("Distinction")
    else:
        print("bara")
elif(a<80 and a>=70):
    print("A")
elif(a<70 and a>=60):
    print("B")
elif(a<60 and a>=50):
    print("C")
elif(a<50 and a>=40):
    print("D")
elif(a>100 or a<0):
    print("Enter Correct Value")
else:
    print("Fail")

    