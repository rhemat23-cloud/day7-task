from abc import ABC, abstractmethod
from functools import reduce


# Abstract Base Class

class AbstractUser(ABC):

    @abstractmethod
    def get_details(self):
        pass


# Parent Class

class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Student Class

class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student -> Name: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


# Faculty Class

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}"


# Temporary Faculty

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

    def get_details(self):
        return f"TempFaculty -> Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Duration: {self.duration}"


# Create Data

students = [
    Student("Ram", 101, "CSE", 60000),
    Student("Arun", 102, "IT", 45000),
    Student("Priya", 103, "ECE", 70000),
    Student("Kumar", 104, "MECH", 30000)
]

faculty = [
    Faculty("Dr.Smith", 201, 50000),
    Faculty("Dr.John", 202, 28000),
    TempFaculty("Dr.Alex", 203, 35000, "6 Months")
]


# Print All Details

print("\n--- Student Details ---")
for s in students:
    print(s.get_details())

print("\n--- Faculty Details ---")
for f in faculty:
    print(f.get_details())


# Sorting

students.sort(key=lambda x: x.fees)
faculty.sort(key=lambda x: x.salary)

print("\n--- Students Sorted by Fees ---")
for s in students:
    print(s.get_details())

print("\n--- Faculty Sorted by Salary ---")
for f in faculty:
    print(f.get_details())


# map() -> Extract Student Names

student_names = list(map(lambda s: s.name, students))
print("\nStudent Names:", student_names)


# filter()

high_fee_students = list(filter(lambda s: s.fees > 50000, students))
print("\nStudents with Fees > 50000")
for s in high_fee_students:
    print(s.get_details())

high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculty))
print("\nFaculty with Salary > 30000")
for f in high_salary_faculty:
    print(f.get_details())


# reduce()

total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculty, 0)

print("\nTotal Fees Collected:", total_fees)
print("Total Faculty Salary:", total_salary)



# Higher Order Function

def process_users(users, func):
    return list(map(func, users))


names = process_users(students, lambda s: s.name)
print("\nNames using Higher Order Function:", names)
