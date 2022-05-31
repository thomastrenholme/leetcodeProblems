using bankNameSpace;
public class bankRunner{
    
    public static void Main(string[] args){


        bank b = new bank("Bay Federal", 1000.50);

        robber jim = new robber("Kim the robber", 9.5);

        b.deposit(100);

        Console.WriteLine(b);

        jim.robBank(b, 1000);

        Console.WriteLine(b);

        jim.robBank(b, 1000);
    }
}