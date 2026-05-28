# Find the number of holes in piece of sheet metal. 0s represent empty space, 1s represent metal. Holes are where 0s including contigious 0s at the top, left, right, and bottom positions. Holes on the edge do not count as a hole. 

# answer should be 1
input1 = [
    [1, 1, 1, 1, 1], 
    [1, 1, 0, 1, 1], 
    [1, 0, 0, 0, 1], 
    [1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 1]
    ]

# answer should be 1
input2 = [
    [1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1], 
    [1, 1, 0, 0, 0], 
    [1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 1]
    ]

# Need to loop through the 2d array and stop when find a 0, else continue
# When find a 0, enter the 0 need to check the surounding positions
# Need to loop through the 
def countHoles(input): 
     