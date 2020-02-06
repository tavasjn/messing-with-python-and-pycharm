# t = 3
# a = 6
#
# print(t + a)

# phrase = "BAMF"
#
# print("Tavas is a " + phrase)


def calc():
    num1 = int(input("Choose your First Number: "))
    num2 = int(input("Choose your Second Number: "))
    type = input("/, *, +, - choose one of these for you equations: ")
    if type == "/":
        print(num1 / num2)
    elif type == "*":
        print(num1 * num2)
    elif type == "+":
        print(num1 + num2)
    elif type == "-":
        print(num1 - num2)

print(calc())