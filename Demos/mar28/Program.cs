string? message = "Hello";
//string message2 = " there";
//string message = "abc";
//string? nullString = null;
Console.Write("> ");
message = Console.ReadLine();
string[] words = [];
if (message != null && message != "")
{
    words = message.Split();
}
else
{
    words = ["n/a"];
}

foreach (string word in words)
{
    Console.WriteLine(word);
}

// Console.Write("Message: <");
// Console.Write(words[0]);
// Console.WriteLine(">");
