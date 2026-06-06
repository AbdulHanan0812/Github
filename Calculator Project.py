
# Calcualtor project 
# using function and loop

def unlim_SUM():#This Function Evalaute Sum
  
   try:
     number = int(input("How many numbers do you want to add = "))
     total = 0
     for i in range(number):
       num =int(input(f" Enter {i + 1} number  = "))
       total +=num
     
     print(f"The Answer is {total}")
  
   except ValueError:
    print("Please Enter Correct Value")

 
 
def unlim_dif():#This Function Evalaute Minus
 try:
    num = int(input(" How many Number do you want to Minus = "))
    total = int(input("Enter 1 Number = "))

    for i in range(1, num):
        number = int(input(f"Enter {i + 1 } Number  = "))
        total -=number
    print(f"The Answer is {total}")
 
 except ValueError:
    print("Please Enter Correct Value")

 
def unlim_mul():#This Function Evalaute Multipily
 try:
    N = int(input("How many numbers do you want to multiply = "))
    total = 1
    for i in range(N):
        X = int(input(f"Enter {i + 1} Number  = "))
        total *=X
    print(f"The Total is {total}")

 except ValueError:
    print("Please Enter Correct Value")




 

def unlim_divide():#This Function Evalaute Divide
 try:
    X = int(input("How many numbers do you want to Divide ="))
    total = float(input("Enter 1 Number = "))
    for i in range( 1 ,X):
        num = float(input(f"Enter {i + 1} Number = "))
        total /=num
    print(f"The Total is {total}")

 except ZeroDivisionError:
    print("Zero Error Please Enter Another Integer")
 except ValueError:
    print("Please Enter Correct Value")


 
  
def square():#This Function Evalaute Square
 try:
    S = int(input(" Enter Number = "))
    result = S * S
    print(result)
 
 
 except ValueError:
    print("Please Enter Correct Value")



 
def cube():#This Function Evalaute Cube
 try:
   I = int(input("Enter Number you find Cube = "))
   Cube = I * I * I
   print(Cube) 

 except ValueError:
    print("Please Enter Correct Value")


while True:
 choice = input("\n Choose This Operation (+ , - , / , * , ** , *** , exit) = ")


 if choice == '+':
    unlim_SUM()
 elif choice == '-':
    unlim_dif()
 elif choice == '/':
    unlim_divide()
 elif choice == '*':
    unlim_mul()

 elif choice == '**':
    square()
 elif choice == '***':
    cube()
 elif choice == 'exit':
    print("Thanks , Good Bye")
 else:
    print("Invelid Choise")


 







