# [Python daily pills] Day 046 - Functions as First Class Objects

What does “Functions as First Class Objects” mean?

They can be passed as arguments to other functions, returned as values from other functions, and
assigned to variables and stored in data structures.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Example:

```python
>>> def myfunc(a, b):
...     return a + b
...
>>> funcs = [myfunc]
>>> funcs[0]
<function myfunc at 0x107012230>
>>> funcs[0](2, 3)
5
```

## References

A great [realpython article](https://realpython.com/lessons/functions-first-class-objects-python/).
