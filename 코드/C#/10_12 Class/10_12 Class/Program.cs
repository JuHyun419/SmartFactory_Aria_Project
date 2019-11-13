using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace _10_12_Class
{
    public class MyClass
    {

        static public void Hi()
        {
            Console.WriteLine("안녕하세용");
        }

        public void Hi2()
        {
            Console.WriteLine("안녕하세용2");
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            MyClass.Hi();
            MyClass myClass = new MyClass();
            myClass.Hi2();
        }
    }
}
