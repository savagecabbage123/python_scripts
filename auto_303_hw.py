import math

cont = ""

def first(Ex, Ey, varx, vary, rho):
    answer = 2*Ex - Ey
    return answer

def second(Ex, Ey, varx, vary, rho):
    answer = Ex + Ey
    return answer

def third(Ex, Ey, varx, vary, rho):
    answer = 4*(varx + pow(Ex,2)) - 4*(rho*math.sqrt(varx*vary) + Ex*Ey) + (vary + pow(Ey,2)) - pow(first(Ex, Ey, varx, vary, rho), 2)
    return answer

def thirdV(Ex, Ey, varx, vary, rho):
    answer = (varx + pow(Ex,2)) + 2*(rho*math.sqrt(varx*vary) + Ex*Ey) + (vary + pow(Ey,2)) - pow(second(Ex, Ey, varx, vary, rho), 2)
    return answer

def fourth(Ex, Ey, varx, vary, rho):
    answer = 2*(varx + pow(Ex,2)) + (rho*math.sqrt(varx*vary) + Ex*Ey) - (vary + pow(Ey,2))
    return answer

def fifth(Ex, Ey, varx, vary, rho):
    answer = fourth(Ex, Ey, varx, vary, rho) - first(Ex, Ey, varx, vary, rho)*second(Ex, Ey, varx, vary, rho)
    return answer

def sixth(Ex, Ey, varx, vary, rho):
    answer = fifth(Ex, Ey, varx, vary, rho)/(math.sqrt(third(Ex, Ey, varx, vary, rho)*thirdV(Ex, Ey, varx, vary, rho)))
    return answer

while cont != "n":
    Ex = int(input("enter Ex:"))
    Ey = int(input("enter Ey:"))
    varx = int(input("enter varX:"))
    vary = int(input("enter varY:"))
    rho = float(input("enter rho:"))

    select = int(input("select question number: "))
    if select == 1:
        print("answer: ", first(Ex, Ey, varx, vary, rho))
    elif select == 2:
        print("answer: ", second(Ex, Ey, varx, vary, rho))
    elif select == 3:
        print("answer: ", third(Ex, Ey, varx, vary, rho))
    elif select == 4:
        print("answer: ", fourth(Ex, Ey, varx, vary, rho))
    elif select == 5:
        print("answer: ", fifth(Ex, Ey, varx, vary, rho))
    elif select == 6:
        print("answer: ", sixth(Ex, Ey, varx, vary, rho))
    else:
        print("not a question")
    cont = input("continue?: ")
