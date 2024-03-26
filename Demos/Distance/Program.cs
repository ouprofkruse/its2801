// See https://aka.ms/new-console-template for more information

long[] loc1 = [3,4];
long[] loc2 = [2,3];

double distance;
distance = Math.Pow(loc1[0]-loc2[0],2);
distance += Math.Pow(loc1[1]-loc2[1],2);
distance = Math.Sqrt(distance);

Console.WriteLine(distance);
