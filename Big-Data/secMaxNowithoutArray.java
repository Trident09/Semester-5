import java.util.Scanner;

public class secMaxNowithoutArray {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the total number of numbers: ");
        int n = scanner.nextInt();

        int max = Integer.MIN_VALUE;
        int secondMax = Integer.MIN_VALUE;

        System.out.println("Enter the numbers: ");
        for (int i = 0; i < n; i++) {
            int number = scanner.nextInt();

            if (number > max) {
                secondMax = max;
                max = number;
            } else if (number > secondMax && number < max) {
                secondMax = number;
            }
        }

        if (secondMax == Integer.MIN_VALUE) {
            System.out.println("There is no second largest number.");
        } else {
            System.out.println("The second largest number is: " + secondMax);
        }
    }
}
