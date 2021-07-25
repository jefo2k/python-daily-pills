# [Python daily pills] Day 040 - Comparing Python Objects the Right Way: `is` vs `==`

There’s a subtle difference between the Python identity operator `is` and the equality operator `==`.

The `==` operator compares the value or equality of two objects, whereas the Python `is` operator checks whether two variables point to the same object in memory.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> a = [1, 2, 3]
>>> b = a

>>> a is b
True
>>> a == b
True

>>> c = list(a)

>>> a == c
True
>>> a is c
False
```

> Note: In the vast majority of cases you should use the equality operators == and !=, except when you’re comparing to None.

## References

- A great [geeksforgeeks tutorial](https://www.geeksforgeeks.org/difference-operator-python/).
- A [Realpython](https://realpython.com/courses/python-is-identity-vs-equality/) course.
