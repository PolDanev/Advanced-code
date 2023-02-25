from art import logo
 

def add(n1, n2):
  return n1 + n2

def subtract(n1 , n2):
  return n1 - n2

def multiplay(n1 , n2):
  return n1 * n2

def divide (n1, n2):
  return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiplay,
              "/": divide,
             }


def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  should_continue = True
  
  while should_continue:
    
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_func = operations[operation_symbol]
    answer = calculation_func(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to EXIT. ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()

