import time
print("This is a fibonacci generator\n")
print("Do you want to generate it? y/n")
answer = input()
int1 = 0
int2 = 1
if answer == "y":
    print("ok\n")
    print(int1)
    while True:
        print(int2)
        int1 += int2
        int2 += int1
        print(int1)
        time.sleep(.1)
else:
    print()