"""
Filename: oops_multilevel_inheritance.py
Purpose: Demonstrate multilevel inheritance in Python.
author: muralitheda
last-updated:11DEC2025
"""

# Real-time: Intern → Employee → Person.

class Person:
    """
    🥇 Grandparent Class: Takes a foundational attribute.
    """
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f"Person Name: {self.name}"

class Employee(Person):
    """
    🥈 Parent Class: Inherits Person, adds a job-specific attribute.
    """
    def __init__(self, name, employee_id):
        # 1. Call the parent's constructor (Person) to initialize 'name'
        super().__init__(name)
        self.employee_id = employee_id

    def get_id(self):
        return f"Employee ID: {self.employee_id}"

class Intern(Employee):
    """
    🥉 Child Class: Inherits Employee, adds an Intern-specific attribute.
    """
    def __init__(self, name, employee_id, project_title):
        # 2. Call the parent's constructor (Employee) to initialize 'name' and 'employee_id'
        super().__init__(name, employee_id)
        self.project_title = project_title

    def profile_summary(self):
        # The Intern object can access ALL attributes defined in the chain.
        print(self.get_name())               # Method from Person
        print(self.get_id())                 # Method from Employee
        print(f"Project Title: {self.project_title}") # Attribute from Intern
        return "Full profile generated successfully."

# --- Demonstration ---

# When creating the Intern, we must provide all three required parameters.
intern_object = Intern(name="Alex Smith", employee_id="INT4021", project_title="Data Cleanup")

print(intern_object.profile_summary())

print("\n--- Direct Attribute Access ---")
print(f"Name (from Person):   {intern_object.name}")
print(f"ID (from Employee):     {intern_object.employee_id}")

print(f"1. Is the Child an instance of Parent?      {isinstance(intern_object, Person)}")
print(f"2. Is the Child an instance of Grandparent? {isinstance(intern_object, Employee)}")
