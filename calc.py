# Building a calculator

print("Basic calculator! Type in 'q' to quit.")

while True:
    x_input = input("Give me a number: ")
    if x_input.lower() == "q":
        print("Goodbye!")
        break
    try:
        x = float(x_input)
    except ValueError:
        print("Please enter a valid (float/int) number.")
        continue

    o = input("Give me an operator (+, -, *, /, **, ^, %, //, or q to quit): ")
    if o == "q":
        print("Goodbye!")
        break
    
    y_input = input("Give me yet another number: ")
    if y_input.lower() == "q":
        print("Goodbye!")
        break
    try:
        y = float(y_input)
    except ValueError:
        print("Please enter a valid (float/int) number.")
        continue

    try:
        if o == "+":
            res = x + y       
        elif o == "-":
            res = x - y
        elif o == "/":
            res = x / y 
        elif o == "*":
            res = x * y
        elif o == "**" or o == "^":
            res = x ** y
        elif o == "%":
            res = x % y
        elif o == "//":
            res = x // y
        else:
            print("Unknown operator.")
            continue
        print(f"Ans is {x} {o} {y} = {res}")

    except ZeroDivisionError:
        print("You can't divide by zero!")