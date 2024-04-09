static int[] location(Random random)
{
    int x = random.Next(10);
    int y = random.Next(10);
    return [x,y];
}
var rand = new Random();
int[] ship = location(rand);
Console.WriteLine($"Ship at {ship[0]} {ship[1]}");




// static double Sum(double[] items)
// {
//     double tempSum = 0.0;
//     for (int i=0; i < items.Length; i++)
//     {
//         tempSum += items[i];
//     }
//     return tempSum;
// }
// double[] list=[5,9,1,4.5];
// Console.WriteLine(Sum(list));




// var rand = new Random();
// for (int i = 0; i<5; i++)
// {
//     // int number = rand.Next(5,10);
//     // Console.Write($"{number,15:D}");
//     double number = rand.NextDouble();
//     Console.Write($"{number,15:F4}");
// }
// Console.WriteLine("");
