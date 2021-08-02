# [Python daily pills] Day 048 - Create an Iterator

Enum is a class in Python for creating enumerations, which are a set of symbolic names attached to **unique**, **constant** values.

In order to create an Enum, it is necessary to create a class which is the name of the Enum that you want.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Example:

```python
>>> class Person:
...   John = 0
...   Paul = 1
...   George = 2
...   Ringo = 3
...
>>> Person.John
0

# using the range function
>>> class Person:
...   John, Paul, George, Ringo = range(4)
...
>>> Person.Paul
1
```

## References

A nice [towardsdatascience article](https://towardsdatascience.com/12-python-tips-and-tricks-for-writing-better-code-b57e7eea580b).
