#-----------Imbied Voice Function-------------- 





pass












History_File = 'history.txt'

#-------History Saving Section---------

def show_history():
   try:
      with open(History_File , 'r') as file:
        lines = file.readlines()
        if not lines:
           print("No History Found")
           return
        for line in reversed(lines):
           print(line.strip())
          
   except FileNotFoundError:
     print("File Does not Exist")
        
   

def clear_history():
    with open(History_File , 'w') as file:
        pass
    print("History Cleared")


def save_history(equation , result):
   with open(History_File , 'a') as file:
    file.write(f"{equation} = {result}\n")


#------------Calculation Function-----------------------

def calculation():
    op = input("Enter Operation (+ - * /) = ")

    try:
        count = int(input("How Many Numbers = "))
    except ValueError:
        print("Please Enter Integer Value")
        return
    
    if count <= 0:
      print("Please enter at least one number")
      return 
    
    numbers = []

    for i in range(count):
        value = float(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    if op == "+":
        result = sum(numbers)

    elif op == "-":
        result = numbers[0]
        for num in numbers[1:]:
            result -= num

    elif op == "*":
        result = 1
        for num in numbers:
            result *= num

    elif op == "/":
        result = numbers[0]
        try:
            for num in numbers[1:]:
                result /= num
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return

    else:
        print("Invalid Operation")
        return

    print("Result =", result)

    equation = f" {op} ".join(map(str, numbers))
    save_history(equation, result)
    
    return result
#------------------Main Function-------------------

def main():
    while True:
        print("1. Calculation")
        print("2. View History")
        print("3. Clear History")
        print("4. Exit")

        try:
            user_input =int(input("Enter choice = "))
        except ValueError:
            print("Please Enter Only Numeric Values")
            continue

        if user_input == 1:
            calculation()

        elif user_input == 2:
            show_history()

        elif user_input == 3:
            clear_history()

        elif user_input == 4:
            print("Goodbye")
            break

        else:
            print("Invalid Input")
if __name__ == "__main__":
    main()