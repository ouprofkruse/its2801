
// As before, create a new project and copy this file to it, replacing the 
// default file created by dotnet.

// In this file, code the "top level" statements 
// -- Do NOT create a "program" class or a "main" method, this version of
// dotnet does not require that.

// -- Do NOT add "using system", this dotnet version does that automatically.

// Create a file "Classes.cs" - this is where you will place all the class definitions.

// ===============================
// For this project:
// -- Create a class LocalMap to hold the map data. The data will be internal
//    to the class (private or protected)
//    The constructor for this class will basically be the CreateMap function from last week
// -- Create a method to print the map header and footer
//    This method is internal to the class (just like the data); you can derive this
//    from the same method you created last week.
// -- Create a method to print the map data including the header and footer;
//    you can derive this from last week's print function.
// +++ New functionality +++
// -- Create a Ship class; you can start with the examples from the lecture notes, but
//    there are some differences.
//    This class needs a constructor that initializes
//    - shield energy
//    - number of torpedoes
//    - name
//    - "short" name; a single character that will identify the ship on the map
//        initialize this to " "

// -- Derive a "Federation" class from the Ship class; make sure to call the base constructor
//    Add a method that takes an (x,y) location coordinate as input; 
//    store the location as a class property

// -- Derive an "Enemy" class from the Ship class
//    Call the base constructor and also intialize a bool "cloak" property - 
//    set the cloak property randomly to true or false.

// -- Go back to the map class and 
//    -- create a method that puts a federation symbol on the map
//       Input arguments are
//       - A federation object
//       This method needs to store the location of the federation ship in an internal variable
//    -- create a method that puts an enemy on the map
//       Input arguments are 
//       - An enemy object
//         If the enemy is cloaked, place a "?" symbol, otherwise place the ship short name
//         This method randomly places the enemy ship, taking care not
//         to put it at a location that is already occupied by another ship (map is not ".")
// ============
// In this file (Program.cs)
// constant
const int DIM = 10;

// Create one map object
// Create one Federation ship, Enterprise, short name "E"
// Call the function to place the ship on the map, location is your choice
// Create 3 Enemy ships with short name "K" for Klingon, names are your choice
// Create 1 Enemy ship with short name "R" for Romulan, name is your choice
// Place the enemy ships on the map
// Print the map