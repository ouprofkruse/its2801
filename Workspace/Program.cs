string[] words = [" "];
string? message;
string empty = String.Empty;
string empty2 = "";
string? nullString  = null;
Console.WriteLine(empty);
Console.WriteLine(empty2);
Console.WriteLine(nullString);
Console.Write("> ");
message = Console.ReadLine();
if (message != null)
{
    words = message.Split();
}
else
{
    words = ["n/a"];
}
int nWords = words.Length;
for (int i=0; i < nWords; i++)
{
    Console.WriteLine(words[i]);
}

foreach (string word in words)
{
    Console.WriteLine(word);
}
Console.WriteLine(words[0]);
