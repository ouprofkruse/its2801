Ship enterprise = new Ship("NCC 1701",5000,10);
enterprise.Torpedoes = 11;
// Console.WriteLine(enterprise.Torpedoes);
Console.WriteLine(enterprise.shipID());

Romulan flagship = new Romulan("T'Met",4000,12,true);
flagship.Torpedoes = 15;
Console.WriteLine(flagship.shipID());
// flagship.CloakStatus();