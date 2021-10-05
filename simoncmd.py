import random
import time
import os

# lists
previous_values = []
pressed_values = []
lost = False

# starts the program off with the 4 first buttons in random order
def start():
    global lost
    # loops until the first 4 buttons have been gone through
    while True:
        ran = random.randrange(1,5)
        # checks if the number generated has already been generated
        if ran in previous_values:
            if len(previous_values) == 4:
                break
        else:
            previous_values.append(ran)
            pressed_values.clear()
            for i in previous_values:
                print("\n")
                print(i)
                time.sleep(1)
                os.system("cls")
            # gets input and goes through each value in the previous_values list
            for i in previous_values:
                press = int(input("match the sequence: "))
                os.system("cls")
                pressed_values.append(press)
                # checks if the input is not equal to the current value of previous_value selected by the for loop
                if press != i:
                    print("you failed")
                    lost = True
                    break
            # breaks out of nested loops
            else:
                continue
            break
            # with gui add restart button, otherwise it will loop in main function forever
            # also add counter
    return

# if the player makes it through the first 4 values then it will continue the program forever unless the player fails using the same logic
def main():
    global lost
    while True:
        ran = random.randrange(1,5)
        previous_values.append(ran)
        pressed_values.clear()
        for i in previous_values:
            print("\n")
            print(i)
            time.sleep(1)
            os.system("cls")
        for i in previous_values:
            press = int(input("match the sequence: "))
            os.system("cls")
            pressed_values.append(press)
            if press != i:
                print("you failed")
                lost = True
                break
        else:
            continue
        break
        # with gui add restart button after this function ends
        # also add counter
    return

start()
if lost == False:
    main()
if lost == True:
    print("you scored",(len(previous_values)-1), "points")