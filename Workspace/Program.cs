// Ship enterprise = new Ship("Enterprise",5000,10);
// Console.WriteLine(enterprise.name);
// enterprise.name = "NC 1701";
// Console.WriteLine(enterprise.ShipID());
// enterprise.Hit(1500);
// Console.WriteLine(enterprise.ShipID());
// enterprise.Torpedoes = 11;
// Console.WriteLine(enterprise.Torpedoes);

Coords location = new Coords(10,20);
Console.WriteLine(location.X);
Console.WriteLine(location.ToString());
public struct Coords
{
    public Coords(double x, double y)
    {
        X = x;
        Y = y;
    }

    public double X { get; }
    public double Y { get; }

    public override string ToString() => $"({X}, {Y})";
}