#initial coordinates
x = 0
y = 0

#coordinates of movements
x2 = []
y2 = []

#initial side
side = "N"

#prepared directions and distance from file
direction = ["R","R","L","R","L","R","R","R","L","R","L","R","L","L","L","R","R","R","L","L","R","L","R","R","L","R","L","L","R","R","R","L","L","R","L","L","R","L","R","L","R","L","L","R","R","L","R","L","R","R","R","L","L","L","R","R","R","L","R","L","L","R","R","L","L","R","L","R","R","R","R","R","L","R","R","L","R","R","R","L","R","R","L","R","L","L","L","R","R","L","R","R","L","L","R","L","L","R","L","L","L","R","R","R","L","L","L","R","L","R","R","L","L","L","R","R","L","R","L","R","R","L","R","L","R","L","R","R","L","R","R","R","L","L","R","R","L","L","R","L","L","R","R","R","L","L","L","L","R","L","L","R","R","R","R","L","R","R","L","L","L","L","L","R","L","L","L","L","R"]
distance = [4,4,1,3,5,2,5,1,4,3,5,2,3,4,3,1,5,1,3,1,3,1,2,2,2,5,3,4,4,4,2,4,1,5,1,4,4,1,1,2,5,2,3,2,1,194,2,4,49,1,3,5,4,1,4,2,1,5,3,5,4,4,4,2,3,78,5,4,191,4,3,1,2,1,3,1,3,4,2,2,1,4,5,2,2,4,2,1,2,3,5,2,3,3,3,1,1,5,4,4,2,5,1,4,3,5,4,5,4,5,4,3,2,5,4,3,3,1,5,5,1,3,2,5,5,3,1,4,5,4,2,3,4,5,3,4,5,5,4,4,4,1,5,3,1,4,3,4,1,5,1,2,2,4,4,5,4,1,1,1,3,5,2,4,3,5,4,1,3,3]

#check if there is intersection and in positive case print occurences 
def check():
    for a, b in enumerate(x2):
        if a + 1 == len(x2):
            continue
        elif ((x == x2[a]) and (y == y2[a])):
            #print every occurences of intersection
            print("Shortest path to the destination is "+str(abs(0-x)+abs(0-y)))
    
#add coordinates to list    
def add():
    x2.append(x)
    y2.append(y)
 
 #browse every item in direction list and after every iterate get a new coordinates and new actual side
for number,item in enumerate(direction):
     if side == "N":
         if direction[number] == "R":
             side = "E"
             for w,z in enumerate(range(distance[number])):
                 x +=1
                 add()
                 check()
         else:
             side = "W"
             for w,z in enumerate(range(distance[number])):
                 x -=1
                 add()
                 check()
     elif side == "W":
         if direction[number] == "R":
             side = "N"
             for w,z in enumerate(range(distance[number])):
                 y += 1
                 add()
                 check()
         else:
             side = "S"
             for w,z in enumerate(range(distance[number])):
                 y -= 1
                 add()
                 check()
     elif side == "E":
         if direction [number] == "R":
             side = "S"
             for w,z in enumerate(range(distance[number])):
                 y -= 1
                 add()
                 check()
         else:
             side = "N"
             for w,z in enumerate(range(distance[number])):
                 y += 1
                 add()
                 check()
     elif side == "S":
         if direction [number] == "R":
             side = "W"
             for w,z in enumerate(range(distance[number])):
                 x -= 1
                 add()
                 check()
         else:
             side = "E"
             for w,z in enumerate(range(distance[number])):
                 x += 1
                 add()
                 check()