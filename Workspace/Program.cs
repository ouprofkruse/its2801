static void Matrix(int[,] data)
{
    for (int x = 0; x < data.GetLength(0); x++)
    {
        for (int y = 0; y < data.GetLength(1); y++)
        {
            Console.Write($"{data[x,y]}  ");
        }
        Console.WriteLine("");
    }
}
int[,] input = new int[,] {{1,2},{3,4}};
Matrix(input);