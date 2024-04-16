public class Ship
{
    protected int _energy;
    public string name;
    private int _torpedoes;
    private int _magazine;
    public int Torpedoes
    {
        get {return _torpedoes;}
        set
        {
            if (value > _magazine) _torpedoes = _magazine;
            else if (value < 0) _torpedoes = 0;
            else _torpedoes = value;
        }
    }
    public Ship(string shipName,int energy, int magazine)
    {
        _energy = energy;
        name = shipName;
        _magazine = magazine;
        _torpedoes = 0;
    }
    public virtual string shipID()
    {
        return $"{name} Shields at {_energy}; {_torpedoes} Torpedoes ready";
    }
}

public class Romulan : Ship
{
    private bool _cloak;
    public Romulan(string shipName, int energy, int magazine, bool cloak) : base(shipName,energy,magazine)
    {
        _cloak = cloak;
    }
    public void CloakStatus()
    {
        if (_cloak) Console.WriteLine($"{name} is cloaked");
        else Console.WriteLine($"{name} is uncloaked");
    }
    public override string shipID()
    {
        string tempStat = "";
        if (_cloak) tempStat = "(Cloaked)";
        return $"{name} Shields at {_energy} {tempStat}";
    }
}
