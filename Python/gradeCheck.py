def calculate_grade(marks):
   grades = {
       100: "Excellent",
       90: "A",
       80: "B",
       70: "C",
       60: "D",
       50: "F",
   }
   for mark, grade in sorted(grades.items(), reverse=True):
       if marks >= mark:
           return grade
   return "IF"

def calculate_sgpa(n, marks):
   grades = [0] * n
   for i in range(n):
       grades[i] = calculate_grade(marks[i])

   sgpa = sum(marks) / n

   return sgpa

n = int(input("Enter the number of subjects: "))

marks = []

for i in range(n):
   marks.append(int(input(f"Enter the marks for subject {i+1}: ")))
sgpa = calculate_sgpa(n, marks)
for i in range(n):
   print(f"Subject {i+1}: Grade = {calculate_grade(marks[i])}, Marks = {marks[i]}")
print("SGPA = ", '%.1f' % sgpa)
