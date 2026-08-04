x = 0

while x == 0:
    userInput = input("Please enter a number [1: counting numbers, 2: exit]: ")
    if userInput == "1":
        count = 1
        while count < 11:
            print(count)
            count +=1
    else:
        print("Exiting the program.")
        break