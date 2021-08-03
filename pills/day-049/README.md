# [Python daily pills] Day 049 - Count Objects with Counter

The `Counter()` function is available in Python’s Collections module. We can use this function to count the frequency of each unique item in an iterable list. This function holds the frequency of each unique item in iterable as a key, value pair.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Example:

```python
>>> from collections import Counter
>>> list1 = [1,1,1,1,2,2,3,3,3,4,5,5,5,6,6,6,6]
>>> Counter(list1)
Counter({1: 4, 6: 4, 3: 3, 5: 3, 2: 2, 4: 1})
```

## References

A great [gitconnected article](https://levelup.gitconnected.com/10-python-tricks-to-code-like-a-pro-programmer-a5faaf596542).
