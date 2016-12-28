#initial coordinates
x = 0
y = 0

#initial side
side = "N"

#prepared directions and distance from file
direction = ["R","R","L","R","L","R","R","R","L","R","L","R","L","L","L","R","R","R","L","L","R","L","R","R","L","R","L","L","R","R","R","L","L","R","L","L","R","L","R","L","R","L","L","R","R","L","R","L","R","R","R","L","L","L","R","R","R","L","R","L","L","R","R","L","L","R","L","R","R","R","R","R","L","R","R","L","R","R","R","L","R","R","L","R","L","L","L","R","R","L","R","R","L","L","R","L","L","R","L","L","L","R","R","R","L","L","L","R","L","R","R","L","L","L","R","R","L","R","L","R","R","L","R","L","R","L","R","R","L","R","R","R","L","L","R","R","L","L","R","L","L","R","R","R","L","L","L","L","R","L","L","R","R","R","R","L","R","R","L","L","L","L","L","R","L","L","L","L","R"]
distance = [4,4,1,3,5,2,5,1,4,3,5,2,3,4,3,1,5,1,3,1,3,1,2,2,2,5,3,4,4,4,2,4,1,5,1,4,4,1,1,2,5,2,3,2,1,194,2,4,49,1,3,5,4,1,4,2,1,5,3,5,4,4,4,2,3,78,5,4,191,4,3,1,2,1,3,1,3,4,2,2,1,4,5,2,2,4,2,1,2,3,5,2,3,3,3,1,1,5,4,4,2,5,1,4,3,5,4,5,4,5,4,3,2,5,4,3,3,1,5,5,1,3,2,5,5,3,1,4,5,4,2,3,4,5,3,4,5,5,4,4,4,1,5,3,1,4,3,4,1,5,1,2,2,4,4,5,4,1,1,1,3,5,2,4,3,5,4,1,3,3]
          
#browse every item in direction list and after every iterate get a new coordinates and new actual side
for number,item in enumerate(direction):
     if side == "N":
         if direction[number] == "R":
             side = "E"
             x +=distance[number]
         else:
                 side = "W"
                 x -=distance[number]
     elif side == "W":
         if direction[number] == "R":
             side = "N"
             y += distance[number]
         else:
             side = "S"
             y -= distance[number]
     elif side == "E":
         if direction [number] == "R":
             side = "S"
             y -= distance[number]
         else:
             side = "N"
             y += distance[number]
     elif side == "S":
         if direction [number] == "R":
             side = "W"
             x -= distance[number]
         else:
             side = "E"
             x += distance[number]

#print final coordinates 
print([x,y])