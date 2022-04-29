pi = 3.141592653589793238462643383279502884
mode = input("pick a mode:\n(1)calculator mode\n(2)conversion mode\n-")


# angle plan conversions units
def angle_plan():
    while True:
        convertion = input("(1)radian to degree|(2)radian to grade\n(3)degree to radian|(4)degree to grade"
                           "\n(5)grade to radian|(6)grade to degree\n-")
        number = float(input("number to convert: "))
        if convertion == "1":
            print(number, "radian = ", number * 180 / pi, "degrees")
        elif convertion == "2":
            print(number, "radian = ", number * 200 / pi, "gon")
        elif convertion == "3":
            print(number, "degree =", number * pi / 180, "rad")
        elif convertion == "4":
            print(number, "degree =", number * 200 / 180, "gon")
        elif convertion == "5":
            print(number, "Grade =", number * pi / 200, "rad")
        elif convertion == "6":
            print(number, "Grade =", number * 180 / 200, "degrees")
        else:
            print("Invalid option.")
            continue
        break
        

# time conversions units
def time():
    while True:
        convertion = input("(1)Day to hour|(2)Day to minute\n(3)Hour to day|(4)Hour to minute\n"
                           "(5)Minute to Day|(6)Minute to Hour")
        number = float(input("number to convert: "))
        if convertion == "1":
            print(number, "Day = ", number * 24, "Hour")
        elif convertion == "2":
            print(number, "Day = ", number * 1440, "Minute")
        elif convertion == "3":
            print(number, "Hour = ", number / 24, "Day")
        elif convertion == "4":
            print(number, "Hour = ", number * 60, "Minute")
        elif convertion == "5":
            print(number, "Minute = ", number / 24, "Hours")
        elif convertion == "6":
            print(number, "Minute = ", number * 60, "Hours")
        else:
            print("Invalid option")
            continue
        break


# calculator mode
if mode == "1":
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


# convertion mode
elif mode == "2":
    while True:
        category = input("Which category do you want:\n(1)Planar_angle\n(2)time\n-")
        if category == "1":
            angle_plan()
        elif category == "2":
            time()
        else:
            print("invalid option")
            continue
        break
print("bye!")
