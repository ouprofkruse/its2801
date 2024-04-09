const int DIM = 10;
int[] SHIP = [3,7];

char[,] localMap = new char[DIM,DIM];

for (int x = 0; x < DIM; x++)
{
    for (int y = 0; y < DIM; y++)
    {
        if (x == SHIP[0] && y == SHIP[1])
        {
            localMap[x,y] = 'E';
        }
        else
        {
            localMap[x,y] = '.';
        }
    }
}

Console.Write("  ");
for (int x = 0; x < DIM; x++)
{
    Console.Write($"{x,2}");
}
Console.WriteLine("");
for (int y = 0; y < DIM; y++)
{
    Console.Write($"{y,2}");
    for (int x = 0; x < DIM; x++)
    {
        Console.Write($" {localMap[x,y]}");
    }
    Console.WriteLine($"{y,2}");
}

Console.Write("  ");
for (int x = 0; x < DIM; x++)
{
    Console.Write($"{x,2}");
}
Console.WriteLine("");