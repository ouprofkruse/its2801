// int[] ar = new int[4];
// Console.WriteLine(ar.Length);
// Console.WriteLine(ar[1]);

// int[] ar1 = [2,3,4];
// Console.WriteLine(ar1.Length);
// int[,] ar2 = new int[,] {{1,2,3},{4,5,6}};
// Console.WriteLine(ar2.Rank);
// Console.WriteLine(ar2.GetLength(0));
// Console.WriteLine(ar2.GetLength(1));
// Console.WriteLine(ar2[0,0]);
// Console.WriteLine(ar2[0,1]);
// Console.WriteLine(ar2[0,2]);
// Console.WriteLine(ar2[1,0]);
// Console.WriteLine(ar2[1,1]);
// Console.WriteLine(ar2[1,2]);


// int[,] ar3 = new int[2,3];
// int n = 2;
// for (int i1 = 0; i1 < ar3.GetLength(0); i1++)
// {
//     for (int i2 = 0; i2 < ar3.GetLength(1); i2++)
//     {
//         ar3[i1,i2] = n;
//         n = n*2;
//     }
// }
// Console.Write($" {ar3[0,0]}");
// Console.Write($" {ar3[0,1]}");
// Console.WriteLine($" {ar3[0,2]}");
// Console.Write($" {ar3[1,0]}");
// Console.Write($" {ar3[1,1]}");
// Console.WriteLine($" {ar3[1,2]}");

// int[][] ar4 = new int[3][];
// ar4[0] = [1,2,3];
// ar4[1] = [5];
// ar4[2] = [6,7];

// Console.WriteLine(ar4[2][0]);

// static double cube (double x)
// {
//     return x*x*x;
// }
// Console.WriteLine(cube(3));


Console.WriteLine(Cube.Volume(3));
Console.WriteLine(Cube.Area(3));


