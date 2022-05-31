

 using System;

 class Person
 {
     public string name; 
     public double weight;
     public int age;


     public Person()
     {
         name = "Jim Bean";
         weight = 175.6;
         age = 25;
     }

     public Person(name, weight, age)
     {
         this.name = name;
         this.weight = weight;
         this.age = age;
     }

     public Person(name, weight=175.6, age=25)
     {
         this.name = name;
         this.weight = weight;
         this.age = age;
     }
 }




class Poop
{

    static void Main(string[] args)
    {

        Program newProg = new Program();
    }
}