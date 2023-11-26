'''
a =[13, -123, 334, 344, -4, 0]

for num in a:
    if num > 0:
        print(f"The number {num} is positive")
        
    elif num < 0:
        print(f"The number {num} is negative")
        
    else:
        print("The number is neither +ve nor -ve")
        
'''
'''
for x in range(1,10):
    if(x%2==0):
        print(f"The {x} in Even")
        
    else:
        print(f"The {x} is Odd")
        '''
'''while loop'''
'''
count=0
while count<5:
    print(f" {count}")
    count+=1
    '''
'''
user_input=input("Enter the input or exit for exit")
while user_input!='exit':
    user_input=input("Enter the input or (exit) for exit")
    '''

num=0
while num < 10 and num %2 ==0:
    print(f"{num} is even")
    num+=2
print('loop finish')
    
    

