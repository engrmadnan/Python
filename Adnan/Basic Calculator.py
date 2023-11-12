import time
title="Basic Calculator"

for x in range(16):
    print(title[x], end="")
    time.sleep(0.5)
    
a=input("\nEnter a value= ")
b=input("Enter a value= ")
c=input("Enter an operand +, -, *, / ")
result=a + c + b
final=eval(result)
print("Result is = ",final)
