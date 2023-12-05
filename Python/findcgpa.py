def calculate_cgpa(n, sgpa):
  grades = [0] * n
  for i in range(n):
      grades[i] = sgpa[i]
  total_grade = sum(grades)
  cgpa = total_grade / n
  return cgpa
n = int(input("Enter the number of semesters: "))
sgpa = []
for i in range(n):
   sgpa.append(float(input(f"Enter the SGPA for semester {i+1}: ")))
cgpa = calculate_cgpa(n, sgpa)
print("CGPA = ", '%.1f' % cgpa)
