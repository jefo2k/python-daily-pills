# [Python daily pills] Day 035 - Anonymous functions

Sometimes, naming a function is not worth the trouble. An example is when you’re sure the function will only be used once. For such cases, Python offers us anonymous functions, also called lambda functions.

A lambda function can be assigned to a variable, creating a concise way of defining a function:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> add_one = lambda x: x + 1
>>> add_one(3)
4
```

It gets more interesting when you need to use a function as an argument. In such cases, the function is often used only once. As you may know, map applies a function to all elements of an iterable object. We can use a lambda when calling map:

```python
>>> numbers = [1, 2, 3, 4]
>>> times_two = map(lambda x: x * 2, numbers)
>>> list(times_two)
[2, 4, 6, 8]
```

> Note: When you need to apply a relatively simple operation on each element of an iterable object, using map() in combination with a lambda function is concise and efficient.

## References

A great [python.land article](https://python.land/deep-dives/functions).
