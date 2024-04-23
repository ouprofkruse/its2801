string? answer;
try
{
    Console.Write("> ");
    answer = Console.ReadLine();
    if (answer == null || answer == "")
    {
        // Console.WriteLine("Answer cannot be empty");
        throw new ArgumentOutOfRangeException(nameof(answer),"Answer cannot be empty");
    }
    else
    {
        Console.WriteLine(42/Convert.ToInt64(answer));
    }
}
// catch (System.DivideByZeroException)
catch (Exception e)
{
    // Console.WriteLine("Can't divide by zero");
    Console.WriteLine($"Bad Input, {e.Message}");
    // throw;
}



// Coords location = new Coords(10,20);
// // Console.WriteLine(location.X);
// Console.WriteLine(location.ToString());

// public struct Coords
// {
//     public Coords(double x,double y)
//     {
//         X = x;
//         Y = y;
//     }

//     public double X {get; }
//     public double Y {get; }
//     public override string ToString() =>  $"({X},{Y})";
    
// }