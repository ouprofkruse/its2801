// In this project you will recreate the exact same functionality as in Week 12,
// creating the short range map, placing the ship, and printing the map.
// However, in this version all the work will be done in methods (functions).
// ---
// To get started, create a new dotnet project in your own work area,
// then replace the "Program.cs" file in that area with this one.
// Make sure to follow the steps called out below
//
// This function will create and fill the initial map, and return it.
// The functions WILL NOT access any global variables
//
// Create a function to create and fill the map with '.'
// I have given you a starting point.
static char[,] CreateMap(int dim)
{
    char[,] tempMap = new char[dim,dim];
    //  insert the double loop here to fill the map with '.' characters.
    return tempMap;
}
// Create a function that accepts places the 'E' symbol for the ship.
//  Paramters: the map, an x and a y coordinate
//  Returns nothing

// Create a function that prints the column labels (x coordinates across the output)
// We will call this twice to print this at the top and bottom
//   Parameters: the dimension
//   Returns nothing

// Create a function that prints the map itself, including the leading and trailing
// row labels.
//    Parameters: the map

// these are our permanent variables
int DIM = 10;
char[,] localMap;

// Call the function to set up the empty map - I have done that for you
localMap = CreateMap(DIM);
// Call the function to place the ship
// Call the function to print the top labels
// Call the function to print the map
// Call the function to print the bottom labels