class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.id = emp_id
        self.department = department
        self.salary = salary


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self):
        name = input("Enter Employee Name: ")
        emp_id = int(input("Enter Employee ID: "))
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        new_employee = Employee(name, emp_id, department, salary)
        self.employees.append(new_employee)

    def remove_employee(self):
        emp_id = int(input("Enter Employee ID to remove: "))
        for employee in self.employees:
            if employee.id == emp_id:
                self.employees.remove(employee)
                break

    def update_salary(self):
        emp_id = int(input("Enter Employee ID to update salary: "))
        new_salary = float(input("Enter New Salary: "))
        for employee in self.employees:
            if employee.id == emp_id:
                employee.salary = new_salary
                break

    def calculate_total_payroll(self):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.salary
        return total_payroll

    def display_employees_in_department(self):
        department = input("Enter Department to display employees: ")
        for employee in self.employees:
            if employee.department == department:
                print(
                    f"Name: {employee.name}, ID: {employee.id}, Department: {employee.department}, Salary: {employee.salary}"
                )

    def display_highest_and_lowest_paid_employees(self):
        sorted_employees = sorted(self.employees, key=lambda x: x.salary, reverse=True)
        print("Highest paid employee:")
        print(
            f"Name: {sorted_employees[0].name}, ID: {sorted_employees[0].id}, Department: {sorted_employees[0].department}, Salary: {sorted_employees[0].salary}"
        )
        print("Lowest paid employee:")
        print(
            f"Name: {sorted_employees[-1].name}, ID: {sorted_employees[-1].id}, Department: {sorted_employees[-1].department}, Salary: {sorted_employees[-1].salary}"
        )

    def give_salary_raise(self):
        percentage = float(input("Enter Percentage for Salary Raise: "))
        for employee in self.employees:
            employee.salary += employee.salary * (percentage / 100)


# Instantiate the EmployeeManagementSystem
ems = EmployeeManagementSystem()

while True:
    print("\n1. Add Employee")
    print("2. Remove Employee")
    print("3. Update Salary")
    print("4. Calculate Total Payroll")
    print("5. Display Employees in Department")
    print("6. Display Highest and Lowest Paid Employees")
    print("7. Give Salary Raise")
    print("8. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        ems.add_employee()
    elif choice == 2:
        ems.remove_employee()
    elif choice == 3:
        ems.update_salary()
    elif choice == 4:
        print(f"Total payroll: ${ems.calculate_total_payroll()}")
    elif choice == 5:
        ems.display_employees_in_department()
    elif choice == 6:
        ems.display_highest_and_lowest_paid_employees()
    elif choice == 7:
        ems.give_salary_raise()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Please try again.")
