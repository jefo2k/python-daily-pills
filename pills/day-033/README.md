# [Python daily pills] Day 033 - Sum an arbitrary number of arguments

As mentioned in [last pill](../day-032), functions are building blocks in Python. They take zero or more arguments and return a value. Python is pretty flexible in terms of how arguments are passed to a function.

Let's see an example of a function that sums up an arbitrary number of arguments using `*args`.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> def addition(*args):
   result = 0
   for i in args:
      result += i
   return result

>>> print(addition())
0
>>> addition(1,4)
5
>>> addition(1,7,3)
11
```

> Note: The parameters passed to the addition function are stored in a tuple. Thus, we can iterate over the args variable.

## References

A great [towardsdatascience article](https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749).
