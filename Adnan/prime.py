inputn = int(input("Enter a number: "))

if inputn > 1:
  
   for i in range(2,inputn):
       if (inputn % i) == 0:
           print(inputn,"is not a prime number.")
           
           break
   else:
       print(inputn,"is a prime number.")    

else:
   print(inputn,"is not a prime number.")

