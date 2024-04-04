# """
# Here we build a 10x10 character map, 
# fill it with "." symbols,
# and add the "E" symbol at an indicated location.
# """

DIM = 10  # constant for the map size
SHIP = [3,7]  #  x & y coordinates for the ship

# in python, we represent the map by a list of lists.
# to make the first index the x-coordinate we need to build the 
# map column by column.
# In C#, we declare a 2-dimensional array instead.
local_map = []
for x in range(DIM):   # loop over x
    column = []  # we need a temporary variable to build the column
#                   in C# we will not need this.
    for y in range(DIM):  # loop over y
        if x == SHIP[0] and y == SHIP[1]:  # checking if this is the ship location
            column.append("E")   # Add either the ship symbol of the empty symbol
        else:                    # in C# we directly store the character
            column.append(".")   # in the array directly at this point
    local_map.append(column)     # add the column to the map - not needed in C#

# print the x-coordinate values along the top
# the end="" argument keeps print from adding a newline
# In C# we use Write here (instead of WriteLine)
print("  ", end="")  # leave two spaces at the left edge
for x in range(DIM):
    print(f"{x:2n}",end="")  # Print the x value in 2 character spaces
print("")  # force a newline
# print the map: the y value is shown at the left and right edge.
for y in range(DIM):  # loop over the y coordinate (rows)
    print(f"{y:2n}",end="")  # print the y value in two character spaces
    for x in range(DIM):  # loop over x coordinates
        print(" "+local_map[x][y],end="")  # print a space followed by the data character
    print(f"{y:2n}")  # end the line by printing the y coordinate value
# repeat the earlier code to print the x coordinates at the bottom
#  calls for using a function in the future, right?
print("  ", end="")
for x in range(DIM):
    print(f"{x:2n}",end="")
print("")

