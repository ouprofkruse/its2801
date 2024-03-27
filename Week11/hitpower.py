# This is the python file you will convert to C#. 
# Please follow the C# setup instructions below first, 
# then go to the details for this project.

# ===  C# Setup  ===
# On the Linux VM:
# -- On the command line (the terminal app or the terminal pane in VS Code)
#    enter the command 'sudo apt install dotnet-sdk-8.0' (enter your password when prompted)
#    check with the command 'dotnet --version' (on the command line),
#    you should see '8.0.103' (the last number might be different)
# -- In VS Code go to the Extensions section (5th icon down on the left)
#    Enter 'C#' in the search box, select C# (Base language support...), and click Install
#      Note: if you end up installing the 'C# Dev Kit', no problem, but realize that the
#      'Run' button (arrow at the top right) won't work it will display an error.
# Note for Windows users:
#     Instead of the 'apt install' step, go to
#     https://dotnet.microsoft.com/en-us/download, make sure the site displays .NET 8.0 and download 
#     .NET SDK x64 
#     The VS Code instructions are the same
#     Check your dotnet installation using 'dotnet --version' in the VS Code terminal panel
#       (you could also use the Powershell command prompt)
# ======================

# ===  Project Instructions  ===
# Note: in these instructions I will use 'week11' as the name of the project, you can use anything you want.
# (1) Use Open Folder in VS Code to navigate to the directory where you usuallly store your scripts
#      (not inside the class repo!)
# (2) At the VS Code Terminal prompt, type 'dotnet new console -o week11' -- you should see a 'week11' 
#     directory appear.
# (3) Use Open Folder in VS Code to navigate the the new directory, week11. You should see Program.cs and
#     other files.  Open Program.cs in VS Code.
# (4) Use Open File to open this file (hitpower.py) so you can refer to it.
#     You may find it convenient to copy the python code to Program.cs and comment it (use Ctrl-/)
# (5) Delete the default content in the Programs.cs file and enter your code instead
#     (follow the hints in the python code below)
# (6) To run your code, go to the commnand prompt in the terminal pane and type 'dotnet run'
# (7) When you are done, submit ONLY the Program.cs file on Blackboard
#
# =============  Context  =================
# In the Startrek game, we can fire phasers at klingons. The starting energy diminshes over distance.
# We want to compute the energy that hits the enemy, assuming it weakens with the square of the distance.
# Since units in scifi games are a bit arbitrary, we use a fudge factor to make sure the power at
# the smalles possible distance equals the starting energy.
# The combat area is 0.9 by 0.9 units large, so the smallest distance is 0.1
# and the largest distance is about 1.2.
#
# =============  python code with hints for C#  =============
# remember to put a ';' at the end of each C# line
#
distance = 0.2    # in C# you need to define the type as well - use double
fudge_factor = 0.01  # declare the type and change to C# naming convention
energy = 1000  # declare the type

hit_energy = energy * fudge_factor / distance**2 # declare type, replace ** with Math.Pow

print(hit_energy)  # replace with Console.WriteLine
