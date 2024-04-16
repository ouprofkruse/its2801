public class Ship
{
    protected int _energy;
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
    public virtual string ShipID()
    {
        return $"{name} Shields at {_energy}";
    }
    public void Hit(int energy)
    {
        _energy = Math.Max(0,_energy - energy);
    }
}

public class Romulan : Ship
{
    private bool _cloak;
    public Romulan(string shipName, int energy, int magazine, bool cloak) : base(shipName, energy, magazine)
    {
        this._cloak = cloak;
    }
    public void CloaKStatus()
    {
        if (_cloak) Console.WriteLine($"{name} is cloaked");
        else Console.WriteLine($"{name} is uncloaked");
    }
    public void Cloak()
    {
        _cloak = !_cloak;
    }
    override public string ShipID()
    {
        string tempStat = "";
        if (_cloak) tempStat = " (Cloaked)";
        return $"{name} Shields at {_energy}{tempStat}";
    }
}