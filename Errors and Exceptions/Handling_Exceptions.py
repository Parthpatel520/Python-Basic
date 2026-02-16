# try :- try block is used to wrap code that may raise an exception. If an exception occurs, the code in the try block is skipped and the program looks for an except block to handle the exception. 

# except :-  execeptions are handled in the try block. If an exception occurs, it is caught and handled in the except block.

# else :- The else block is used to specify code that will be executed if no exceptions were raised in the try block. It is typically used to perform actions that should only occur if the try block was successful.

# finally :- The finally block is used to specify code that will be executed regardless of whether an exception occurred or not. It is typically used for cleanup operations, such as closing files or releasing resources.

# raise :- The raise statement is used to manually raise an exception. You can specify the type of exception you want to raise and provide an optional error message.
 
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("Program finished.")
    

try:
    x = int(input("Enter number: "))
    result = 10 / x
except ValueError:
    print("Invalid input! Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero!")
    
else:
    print("Result:", result)

finally:
    print("Program finished.")
    
    

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass


for cls in [D, C, B]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("class B")


