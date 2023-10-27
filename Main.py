def add(a, b):
  return a + b
 
def subtract(a, b):
  return a - b
 
def multiply(a, b):
  return a * b
 
def divide(a, b):
  return a / b
 
def main():
  print("Welcome to the simple calculator!")
 
  while True:
    operation = input("What operation would you like to perform? (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == "+":
      result = add(num1, num2)
    elif operation == "-":
      result = subtract(num1, num2)
    elif operation == "*":
      result = multiply(num1, num2)
    elif operation == "/":
      result = divide(num1, num2)
    else:
      print("Invalid operation.")
      continue
 
 
    print("The result is:", result)
 
    again = input("Would you like to perform another operation? (y/n): ")
    if again == "n":
      break
 
if __name__ == "__main__":
  main()