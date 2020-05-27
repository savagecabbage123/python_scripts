import time
import sys
animation = "\|/-\|/"
print("welcome to a caculator")
print("to begin input your first number")
num1 = int(input("type the first number: "))
operator = input("now type in an operator: ")
num2 = int(input("now type your last number: "))
adding = num1 + num2
subtracting = num1 - num2
multiplying = num1 * num2
dividing = num1 / num2
def Calculate():
    for i in range(40):
        time.sleep(0.1)
        sys.stdout.write("\r" + "calculating" + animation[i % len(animation)])
        sys.stdout.flush()
if operator == "+":
    Calculate()
    print(adding)
if operator == "-":
    Calculate()
    print(subtracting)
if operator == "*":
    Calculate()
    print(multiplying)
if operator == "/":
    Calculate()
    print(dividing)