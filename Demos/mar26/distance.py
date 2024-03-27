import math
location1 = [0,0]
location2 = [.9,.9]
# distance is square-root(x-distance-squared + y-distance-squared)
x_dist2 = (location1[0]-location2[0])**2
y_dist2 = (location1[1]-location2[1])**2
distance = math.sqrt(x_dist2+y_dist2)
print(distance)