// import math
// location1 = [2,5]
// location2 = [3,6]
// # distance is square-root(x-distance-squared + y-distance-squared)
// x_dist2 = (location1[0]-location2[0])**2
// y_dist2 = (location1[1]-location2[1])**2
// distance = math.sqrt(x_dist2+y_dist2)
// print(distance)

long[] location1 = [2,5];
long[] location2 = [3,6];

double xDist2 = Math.Pow(location1[0]-location2[0],2);
double yDist2 = Math.Pow(location1[1]-location2[1],2);

double distance = Math.Sqrt(xDist2+yDist2);
Console.WriteLine(distance);
