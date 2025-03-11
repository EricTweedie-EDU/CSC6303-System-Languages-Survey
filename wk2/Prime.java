// Eric Tweedie CSC6303 week 2
// Convert C++ to Java
import java.util.Scanner;

public class Prime {
    public static boolean isPrime(int n) {
        // conditions to check if n is prime
        if (n <= 1)    return false;
        if (n <= 3)     return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i =5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number;
        // prompt user for input and check if the number is prime or not
        do {
            System.out.print("Enter a positive number (0 or negative to exit): ");
            if (!scanner.hasNextInt()) break;
            number = scanner.nextInt();
            if (number <= 0)    break;
            if (isPrime(number)) System.out.println(number + " is a prime number.");
            else                 System.out.println(number + " is not a prime number.");
        }
        while (true);
        scanner.close();
    }
}