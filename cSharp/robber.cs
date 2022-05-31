namespace bankNameSpace{


    public class robber{
        
        private string robberName;
        private double robberStrength;

        private Boolean isInJail;

        public robber(string robberName, double robberStrength){
            this.robberName = robberName;

            this.robberStrength = robberStrength;
        }

        public bool robBank(bank b, double amtToSteal){

            if(isInJail){
                Console.WriteLine("{0} is in jail and cannot rob the bank", this.robberName);
                return false;
            }
            if(b.balance > amtToSteal){

                Random r = new Random();

                double chance =  r.Next(1, 100);

                Console.WriteLine("Chance: " + chance);

                if (robberStrength >= chance){
                    Console.WriteLine("Mmmmmmm.... Money!!!");
                    Console.WriteLine("On: " + DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss") + "\nA Massive robbery was commited on: " + b.bankName
                    + "\nThe amount stolen was: " + amtToSteal + " by Robber: " + robberName);

                    b.balance-=amtToSteal;
                    return true;
                }
                else{
                    Console.WriteLine("Robber: " + robberName + " was unable to rob the bank: " + b.bankName + " and is now in jail");
                    isInJail = true;
                    return false;
                }

            }
            else{
                Console.WriteLine("Grrr. .. no money. " );
                return false;
            }
        }
    }
}