print("-------------------A SIMPLE CALCULATOR------------------------------")
another ="y"
while another == "y": 
  num1 = int(input("Enter the first Number: "))
  operator = input("Enter an operator. E.g (+, -, * or /): ")
  num2 = int(input("Enter the second number: "))
  if operator == "+":
    print(f"Result of the summation is {num1 + num2}")
  elif operator == "-":
    print(f"Result of the subtraction is {num1 - num2}")
  elif operator == "*":
    print(f"Result of the multiplication is {num1 * num2}")
  else:
    print(f"Result of the division is {num1 / num2}")
  another = input("Would you like to perform another calculation( y or n): ")
else:
  print("Thank you and good bye")



