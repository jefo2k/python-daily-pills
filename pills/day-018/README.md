# [Python daily pills] Day 018 - Merging two dictionaries with a single expression

In this little pill we'll show how to merge two dictionaries with a single expression.

If you don't know what a Python dictionary is please check [this pill](../day-014).

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## In Python 3.5+

```python
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = {**x, **y}
>>> z
{'a': 1, 'b': 3, 'c': 4}
```

## In Python 2.x

```python
>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = dict(x, **y)
>>> x
{'a': 1, 'b': 2} 
```

> In both examples Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.

## References

Video from [realpython.com](https://www.youtube.com/watch?v=Duexw08KaC8).
