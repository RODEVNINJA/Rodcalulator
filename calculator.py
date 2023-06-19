# import math 
print("This is a calculator that takes 3 numbers and operation to be carried out on them and returns the answer")
Value_1 = int(input("Enter 1st number "))
operator_1 = input("Enter an operation ")
Value_2 = int(input("Enter 2nd number "))
operator_2 = input("Enter an operation ")
Value_3 = int(input("Enter 3rd number "))
# operators = {+,-,/,*}
add = "+"
subtract = "-"
divide = "/"
multiply = "*"
if operator_1 == add and operator_2 == add: 
    print(Value_1 + Value_2 + Value_3)
elif operator_1 == add and operator_2 == subtract:
    print(Value_1 + Value_2 - Value_3)
elif operator_1 == add and operator_2 == multiply:
    print(Value_1 + Value_2 * Value_3)
elif operator_1 == add and operator_2 == divide:
    print(Value_1 + Value_2 / Value_3)
elif operator_1 == subtract and operator_2 == add:
    print(Value_1 - Value_2 + Value_3)
elif operator_1 == subtract and operator_2 == subtract:
    print(Value_1 - Value_2 - Value_3)
elif operator_1 == subtract and operator_2 == multiply:
    print(Value_1 - Value_2 * Value_3)
elif operator_1 == subtract and operator_2 == divide:
    print(Value_1 - Value_2 / Value_3)
elif operator_1 == multiply and operator_2 == add:
 print(Value_1 * Value_2 + Value_3)
elif operator_1 == multiply and operator_2 == subtract:
    print(Value_1 * Value_2 - Value_3)
elif operator_1 == multiply and operator_2 == divide:
    print(Value_1 * Value_2 / Value_3)
elif operator_1 == multiply and operator_2 == multiply:
    print(Value_1 * Value_2 * Value_3)
elif operator_1 == divide and operator_2 == add:
    print(Value_1 / Value_2 + Value_3)
elif operator_1 == divide and operator_2 == subtract:
    print(Value_1 / Value_2 - Value_3)
elif operator_1 == divide and operator_2 == multiply:
    print(Value_1 / Value_2 * Value_3)
elif operator_1 == divide and operator_2 == divide:
    print(Value_1 / Value_2 / Value_3)
print("Goodbye")
