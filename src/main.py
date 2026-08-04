# This will initialize a variable to start the while loop
x = 0

# Main loop
while x == 0:
    # prompts user for input
    userInput = int(input("Please enter a number [1: counting numbers, any number: exit]: "))

    # checks if the user input is 1 or anything
    if userInput == 1:
        count = 1
        while count < 11:
            print(count)
            count +=1
    else:
        print("Exiting the program.")
        break