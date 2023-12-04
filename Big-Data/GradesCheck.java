import java.util.Scanner;

public class GradesCheck {
  public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
      System.out.println("Enter the marks for the subject: ");
      float marks = scanner.nextFloat();
      String grade = findGrade(marks);
      System.out.println("Marks: " + marks + ", Grade: " + grade);
  }

  private static String findGrade(float marks) {
      if (marks == 100) {
          return "Excellent";
      } else if (marks >= 90) {
          return "A";
      } else if (marks >= 80) {
          return "B";
      } else if (marks >= 70) {
          return "C";
      } else if (marks >= 60) {
          return "D";
      } else if (marks >= 50) {
          return "F";
      } else {
          return "IF";
      }
  }
}
