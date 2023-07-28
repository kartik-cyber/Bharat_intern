def calculate(x, y, operator):
  if operator == "+":
    return x + y
  elif operator == "-":
    return x - y
  elif operator == "*":
    return x * y
  elif operator == "/":
    return x / y
  else:
    raise ValueError("Invalid operator")


def main():
  x = int(input("Enter the first number: "))
  y = int(input("Enter the second number: "))
  operator = input("Enter the operator (+, -, *, /): ")

  result = calculate(x, y, operator)
  print(f"The result of {x} {operator} {y} is: {result}")


if __name__ == "__main__":
  main()