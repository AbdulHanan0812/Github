
# Calcualtor project 
# using function and loop
while True: 
 choice = input(" Choise Operation you want to perform ( + , - , / , * , ** , *** ) =  ")


 def unlim_SUM():#This Function Evalaute Sum
    
     number = int(input("How many numbers do you want to add = "))
     total = 0
     for i in range(number):
       num =int(input(f" Enter {i + 1} number  = "))
       total +=num
     
     print(f"The Answer is {total}")




 def unlim_dif():#This Function Evalaute Minus
    num = int(input(" How many Number do you want to Minus = "))
    total = int(input("Enter 1 Number = "))

    for i in range(1, num):
        number = int(input(f"Enter {i + 1 } Number  = "))
        total -=number
    print(f"The Answer is {total}")


 def unlim_mul():#This Function Evalaute Multipily
    N = int(input("How many numbers do you want to multiply = "))
    total = 1
    for i in range(N):
        X = int(input(f"Enter {i + 1} Number  = "))
        total *=X
    print(f"The Total is {total}")




 def unlim_divide():#This Function Evalaute Divide
    X = int(input("How many numbers do you want to Divide ="))
    total = float(input("Enter 1 Number = "))
    for i in range( 1 ,X):
        num = float(input(f"Enter {i + 1} Number = "))
        total /=num
    print(f"The Total is {total}")



 def square():#This Function Evalaute Square
    S = int(input(" Enter Number = "))
    result = S * S
    print(result)




 def cube():#This Function Evalaute Cube
  I = int(input("Enter Number you find Cube = "))
  Cube = I * I * I
  print(Cube) 







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

 else:
    print("Invelid Choise")






    

