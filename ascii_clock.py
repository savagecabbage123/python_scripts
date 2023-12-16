numlist = [
    ["000", " 1 ", "222", "333", "4 4", "555", "666", "777", "888", "999", " "],
    ["0 0", "11 ", "  2", "  3", "4 4", "5  ", "6  ", "  7", "8 8", "9 9", ":"],
    ["0 0", " 1 ", "222", "333", "444", "555", "666", "  7", "888", "999", " "],
    ["0 0", " 1 ", "2  ", "  3", "  4", "  5", "6 6", "  7", "8 8", "  9", ":"],
    ["000", "111", "222", "333", "  4", "555", "666", "  7", "888", "999", " "]
]

input_list = []
clock_input = input("Enter the time: \n")

#clock input is valid length
if len(clock_input) < 6 and len(clock_input) > 3:
    #splits up string into pieces in a list
    for char in clock_input:
        input_list.append(char)
    #determine if colon is in the string and if its in a correct spot
    #make sure that : is at correct position
    if len(input_list) == 4 and ":" == input_list[1]:
        #success
        #convert colon to 10
        pos = input_list.index(":")
        input_list[pos] = "10"

        #print clock
        for i in range(len(numlist)):
            print(numlist[i][int(input_list[0])], end=" ")
            print(numlist[i][int(input_list[1])], end=" ")
            print(numlist[i][int(input_list[2])], end=" ")
            print(numlist[i][int(input_list[3])], end=" ")
            print()
    elif len(input_list) == 5 and ":" == input_list[2]:
        #success
        #convert colon to 10
        pos = input_list.index(":")
        input_list[pos] = "10"

        #print clock
        for i in range(len(numlist)):
            print(numlist[i][int(input_list[0])], end=" ")
            print(numlist[i][int(input_list[1])], end=" ")
            print(numlist[i][int(input_list[2])], end=" ")
            print(numlist[i][int(input_list[3])], end=" ")
            print(numlist[i][int(input_list[4])], end=" ")
            print()
    else:
        print("invalid clock input")
else:
    print("invalid clock input")
