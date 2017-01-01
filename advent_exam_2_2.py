#empty list of bathroom codes
bathroomCode = []

#initial position
position = 5

#get every line into list of lines
lines = [line.rstrip('\n') for line in open('text2.txt')]

#loop through ever line
for number,item in enumerate(lines):
    #loop through every element in line
    for element in lines[number]:
        if (element == "U"):
            if (position == 1):
                pass
            elif (position == 2):
                pass
            elif (position == 3):
                pass
            elif (position == 4):
                pass
            elif (position == 5):
                pass
            elif (position == 6):
                position = 2
            elif (position == 7):
                position = 3
            elif (position == 8):
                position = 4
            elif (position == 9):
                pass
            elif (position == "A"):
                position = 6
            elif (position == "B"):
                position = 7
            elif (position == "C"):
                position = 8
            elif (position == "D"):
                position = "B"
        elif (element == "D"):
            if (position == 1):
                position = 3
            elif (position == 2):
                position = 6
            elif (position == 3):
                position = 7
            elif (position == 4):
                position = 8
            elif (position == 5):
                pass
            elif (position == 6):
                position = "A"
            elif (position == 7):
                position = "B"
            elif (position == 8):
                position = "C"
            elif (position == 9):
                pass
            elif (position == "A"):
                pass
            elif (position == "B"):
                position = "D"
            elif (position == "C"):
                pass
            elif (position == "D"):
                pass
        elif (element == "L"):
            if (position == 1):
                pass
            elif (position == 2):
                pass
            elif (position == 3):
                position = 2
            elif (position == 4):
                position = 3
            elif (position == 5):
                pass
            elif (position == 6):
                position = 5
            elif (position == 7):
                position = 6
            elif (position == 8):
                position = 7
            elif (position == 9):
                position = 8
            elif (position == "A"):
                pass
            elif (position == "B"):
                position = "A"
            elif (position == "C"):
                position = "B"
            elif (position == "D"):
                pass
        elif (element == "R"):
            if (position == 1):
                pass
            elif (position == 2):
                position = 3
            elif (position == 3):
                position = 4
            elif (position == 4):
                pass
            elif (position == 5):
                position = 6
            elif (position == 6):
                position = 7
            elif (position == 7):
                position = 8
            elif (position == 8):
                position = 9
            elif (position == 9):
                pass
            elif (position == "A"):
                position = "B"
            elif (position == "B"):
                position = "C"
            elif (position == "C"):
                pass
            elif (position == "D"):
                pass
    #save final code number to bathroomCode list
    bathroomCode.append(position)
#print final code list
print(bathroomCode)            