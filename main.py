first_nb = float(input("first number"))
second_nb = float(input("second number"))

# if the user inputs something other than *, -, /, +
# the user will be asked to pick the operator again
while True:
    operator = input("pick an operator: *, -, /, +")
    if operator == "*":
        print("result", first_nb * second_nb)
    elif operator == "-":
        print("result", first_nb - second_nb)
    elif operator == "/":
        if second_nb == 0:
            print("can't devise by 0")
        else:
            print("result", first_nb / second_nb)
    elif operator == "+":
        print("result", first_nb + second_nb)
    else:
        print("invalid option")
        continue
    break
print("Bye")
