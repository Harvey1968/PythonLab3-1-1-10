#3.1.1.10 LAB: Comparison operators and conditional execution

#User inputs a Plant name
plantName = input("Enter plant name: ")
if plantName == "Spathiphyllum":
    print('"Yes - Spathiphyllum is the best plant ever!"\n')
#    exit() #Left in to show that it is not required

#'elif' NOT 'if' or will output line 6 and 11 print statements
elif plantName == "spathiphyllum":
    print('"No, I want a big Spathiphyllum!"\n')
#    exit() #Left in to show that it is not required

#If user input is not some variation of "Spathiphyllum" then the below will happen
else:
    print('"Spathiphyllum! Not', plantName, end='!"\n\n')
#    exit() #Left in to show that it is not required