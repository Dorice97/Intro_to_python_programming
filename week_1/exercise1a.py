#simple calculator program

#request user to enter first number 

first_number = input("enter first number: ") 

first_number=int(first_number) 

#request user to enter an operator 

operator = input("enter an operator (+,-,/,*): ") 

#request user to enter second number 

second_number = input("enter second number: ") 
second_number=int(second_number) 

# assign operators;addition,subtraction,multiplication, division

if operator == "+": 
    print (first_number + second_number) 

elif operator == "-": 
     print(first_number - second_number) 

elif operator =="/": 
    print(first_number/second_number) 

elif operator =="*": 
     print(first_number*second_number) 

else: 
     print("invalid operator!") 


