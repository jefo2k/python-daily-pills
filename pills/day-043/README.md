# [Python daily pills] Day 043 - List comprehension tricks you might not know

Creating lists using list comprehension is more pythonic and easier to read. But did you know that you can create other types of objects with the same technique?

We’ll show you 2 tricks that you might not be using yet. They’ll help make your code easier to read, and easier to write.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Dictionary comprehension

```python
>>> words = ["hello", "old", "friend"]
>>> data = {word: len(word) for word in words}
>>> data
{'hello': 5, 'old': 3, 'friend': 6}
```

## Filtering

```python
>>> words = ['deified', 'radar', 'guns']
>>> palindromes = [word for word in words if word == word[::-1]]
>>> palindromes
['deified', 'radar']
```

## References

A [gitconnected article](https://levelup.gitconnected.com/3-python-list-comprehension-tricks-you-might-not-know-yet-5891d904ee76).
