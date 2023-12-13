import employee

x = 7
y = 12


class Manager(employee.Employee):
    mgr_count = 0

    def __init__(self, name, salary, departament):
        self.name = name
        self.salary = salary
        self.departament = "A03 " + departament
        Manager.mgr_count += 1

    def display_employee(self):
        print("Salary: ", self.salary)


e1 = employee.Employee("Gigi", 10)
m1 = Manager("Ion", 100, "IT")
m2 = Manager("Ionela", 5, "HR")
m3 = Manager("Jhon", 25, "Curatenie")
m4 = Manager("Marian", 33, "Design")

e1.display_employee()
m1.display_employee()
m2.display_employee()
m3.display_employee()
m4.display_employee()

print(e1.empCount)
print(m3.mgr_count)
