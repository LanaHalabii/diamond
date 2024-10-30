row = int(input("Enter the number of rows"))

#upper part of diamond
for i in range (1, row+1):
    for j in range(1, row-i+1): #this is couting columns to leave spaces at row-i+1, depending on the input
        print(" ", end="")
    for j in range (1, i*2): #this is counting rows to add the stars accordingly, and is multiplied by two to create symmetrical stars
        print("*", end="")
    print()
