public class Ship
{
    private int _energy;
    public string name;
    public Ship(string shipName, int energy)
    {
        _energy = energy;
        name = shipName;
    }
    public string ShipID()
    {
        return $"{name} Shields at {_energy}";
    }
    public void Hit(int energy)
    {
        _energy = Math.Max(0,_energy-energy);
    }
}