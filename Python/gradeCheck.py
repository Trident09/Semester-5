def find_grade(marks):
   if marks == 100:
       return "Excellent"
   elif marks >= 90:
       return "A"
   elif marks >= 80:
       return "B"
   elif marks >= 70:
       return "C"
   elif marks >= 60:
       return "D"
   elif marks >= 50:
       return "F"
   else:
       return "IF"

marks = float(input("Enter the marks for the subject: "))
grade = find_grade(marks)
print("Marks: " + str(marks) + ", Grade: " + grade)
