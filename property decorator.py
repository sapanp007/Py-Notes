"""
Gives ability to define a function and use it/ call it just like an attribute

Advantages -  if anyone using our class using any method and we want to add additional
functionality to it the we can convert that attribute to a method and add @property
so that we can continue to use that as an attribute

Gives a new way to update the attributes by creating the @property
"""


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email_id = f"{self.first}.{self.last}@gmail.com"
        self.full_name = f"{self.first} {self.last}"


emp1 = Employee('Sapan', 'Sagar')
emp1.first = "Madhu"
print(emp1.full_name, emp1.email_id)
""" 
suppose we want to change the email_id as first or last name is updated,
then we need to get email_id value out of init method and create a method for it
and it should be called when user tries to access email_id attribute

Another situation is that suppose by updating fullname 
we want first and last also to be updated
"""


class PropertyEmployee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email_id(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

    @full_name.deleter
    def full_name(self):
        print("Deleting Name")
        self.first = None
        self.last = None


emp1 = PropertyEmployee('Sapan', 'Sagar')
emp1.first = "Madhu"
print(emp1.full_name, emp1.email_id)
emp1.full_name = "zyz com"
print(emp1.first, emp1.last, emp1.email_id)
del emp1.full_name
print(emp1.first, emp1.last, emp1.email_id)

