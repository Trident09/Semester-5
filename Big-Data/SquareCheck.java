import java.util.Scanner;

public class SquareCheck {
   public static void main(String[] args) {
       Scanner scanner = new Scanner(System.in);
       System.out.println("Enter a number: ");
       int num = scanner.nextInt();
       if (isPerfectSquare(num)) {
           System.out.println(num + " is a perfect square.");
       } else {
           System.out.println(num + " is not a perfect square.");
       }
   }

   private static boolean isPerfectSquare(int number) {
       if (number < 0) return false;
       int sqrt = (int) Math.sqrt(number);
       return sqrt * sqrt == number;
   }
}
