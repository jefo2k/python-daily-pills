# [Python daily pills] Day 041 - The Walrus Operator `:=`

The biggest change in Python 3.8: the introduction of assignment expressions `:=`. This operator is often called the walrus operator as it resembles the eyes and tusks of a walrus on its side.

Assignment expressions allow you to assign and return a value in the same expression.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> sample_data = [
...     {"id": 1, "name": "Amol", "project": False},
...     {"id": 2, "name": "Kiku", "project": False},
...     {"id": 3, "name": None, "project": False},
...     {"id": 4, "name": "Lini", "project": True},
...     {"id": 4, "name": None, "project": True},
... ]

# With Python 3.8 Walrus Operator
>>> for entry in sample_data:
...     if name := entry.get("name"):
...         print("Found Person:", name)

Found Person: Amol
Found Person: Kiku
Found Person: Lini

# Without Walrus Operator
>>> for entry in sample_data:
...     name = entry.get("name")
...     if name:
...         print('Found Person:', name)

Found Person: Amol
Found Person: Kiku
Found Person: Lini
```

## References

- A awesome [realpython tutorial](https://realpython.com/lessons/assignment-expressions/).
- The [Python 3.8 documentation](https://docs.python.org/3/whatsnew/3.8.html).
- [pythonexamples](https://pythonexamples.org/python-walrus-operator/).
