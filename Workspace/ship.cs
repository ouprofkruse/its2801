public class Ship
{
    private int _energy;
    private int _magazine;
    private int _torpedoes = 0;
    public int Torpedoes
    {
        get {return _torpedoes;}
        set 
        {
            if (value > _magazine) _torpedoes=_magazine;
            else _torpedoes = value;
        }
    }
    public string name;
    public Ship(string shipName, int energy, int magazine)
    {
        _energy = energy;
        _magazine = magazine;
        name = shipName;
    }
    public string ShipID()
    {
        return $"{name} Shields at {_energy}";
    }
    public void Hit(int energy)
    {
        _energy = Math.Max(0,_energy - energy);
    }
}