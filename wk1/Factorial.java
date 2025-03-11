// Eric Tweedie CSC6303 week 1
// Project 1 converting Python code into Java code
// IDE is VS Code

import java.util.Scanner;

public class Factorial {
    // Java code to find the factorial of a number provided by the user
    public static void fact() {
        Scanner user = new Scanner(System.in);
        int n;
        
        System.out.print("Enter a positive Integer: ");
        n = user.nextInt();
        
        while (n < 0) {
            System.out.print("Sorry, only positive numbers, enter again: ");
            n = user.nextInt();
        }
        
        if (n == 0) {
            System.out.println("The factorial of 0 is 1");
        } else {
            long f = 1;
            for (int i = 1; i <= n; i++) {
                f *= i;
            }
            System.out.println("The factorial of " + n + " is " + f);
        }
        
        user.close();
    }
    public static void main(String[] args) {
        Factorial.fact();
    }
}
