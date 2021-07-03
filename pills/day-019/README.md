# [Python daily pills] Day 019 - Swap two variables in Python

Two ways to swap the values of two variables:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Using a temporary variable

```python
>>> a = 11
>>> b = 7

>>> temp = a
>>> a = b
>>> b = temp

>>> a
7
>>> b
11
```

## Without a temporary variable (Tuple swap)

```python
>>> a = 11
>>> b = 7

>>> a, b = b, a
>>> a
7
>>> b
11
```

> If you don't know what a Python tuple is please check out [this pill](../day-016).

## References

From [30secondsofcode](https://www.30secondsofcode.org/articles/s/python-swap-variables).
