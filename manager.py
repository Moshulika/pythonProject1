import employee
import pytest

# Nanescu Eduard, x%3==1
x = 7
y = 12


class Manager(employee.Employee):
    mgr_count = 0

    def __init__(self, name, salary, departament):
        self.name = name
        self.salary = salary
        self.departament = "A03 " + departament
        Manager.mgr_count += 1


    # x%3==1
    def display_employee(self):
        print("Salary: ", self.salary)

# Facem mai multe instante ale claselor de care avem nevoei
e1 = employee.Employee("Gigi", 10)
m1 = Manager("Ion", 100, "IT")
m2 = Manager("Ionela", 5, "HR")
m3 = Manager("Jhon", 25, "Curatenie")
m4 = Manager("Marian", 33, "Design")

# Afisam detalii despre manageri/angajati
e1.display_employee()
m1.display_employee()
m2.display_employee()
m3.display_employee()
m4.display_employee()

# Printam nr. de anagajati/manageri
print(e1.empCount)
print(m3.mgr_count)
