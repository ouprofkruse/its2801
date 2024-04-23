string? answer;
try
{
    Console.Write("> ");
    answer = Console.ReadLine();
    if (answer == null || answer == "")
    {
        throw new ArgumentOutOfRangeException(nameof(answer),"Answer cannot be empty");
    }
    else
    {
        Console.WriteLine(42/Convert.ToInt64(answer));
    }
}
catch (Exception e)
{
    Console.WriteLine($"Bad input, {e.Message}");
}