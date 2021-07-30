# [Python daily pills] Day 045 - Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** is the class being inherited from, also called base class.

**Child class** is the class that inherits from another class, also called derived class.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Example:

```python
>>> class Person:
...   def __init__(self, fname, lname):
...     self.firstname = fname
...     self.lastname = lname
...   def printname(self):
...     print(self.firstname, self.lastname)
...
>>> class Student(Person):
...   def __init__(self, fname, lname, year):
...     super().__init__(fname, lname)
...     self.graduationyear = year
...   def welcome(self):
...     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
...
>>> student = Student("Mike", "Olsen", 2019)
>>> student.welcome()
Welcome Mike Olsen to the class of 2019
```

> Note: The `super()` function allow the child class inherit all the methods and properties from its parent.

## References

Another great [w3schools article](https://www.w3schools.com/python/python_inheritance.asp).
