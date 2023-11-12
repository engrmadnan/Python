a=eval(input("Enter the Percentage"))
if(a>=80 and a<=100):
    print("A+")
elif(a<=70 and a>=70):
    print("A")
elif(a<=69 and a>=60):
    print("C")
elif(a<=59 and a>=50):
    print("D")
elif(a<=49 and a>=40):
    print("E")
elif(a>100 or a<0):
    print("Enter Correct Value")
else:
    print("Fail")

    