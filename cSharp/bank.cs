
 
namespace bankNameSpace
{

    public class bank{

        public double balance;
        public string bankName;

        public DateTime time;


        public bank(string bankName, double balance){

            this.bankName = bankName;
            this.balance = balance;
            this.time = DateTime.Now;
        }

        public void deposit(double money){
            this.balance+=money;
            Console.WriteLine("Time of deposit: " + DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss") + " and deposit amount: " + money);
        }

        public bool withDrawal(double money){

            if(balance >= money){

                balance-= money;
                Console.WriteLine("Time of withdrawal: " + DateTime.Now.ToString("dd/MM/yyyy HH:mm:ss") + " and withdrawal amount: " + money);
                return true;
            }
            Console.WriteLine("You don't have enough money to withdraw");
            return false;
        }


        public override string ToString(){
            return "Bank: " + bankName + " Balance: " + balance;
        }
    }
}