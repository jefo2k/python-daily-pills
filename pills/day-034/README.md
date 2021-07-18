# [Python daily pills] Day 034 - Unpacking Argument Lists

When the arguments are already in a list or tuple but need to be unpacked for a function call requiring separate positional arguments. Who you wanna call?

For instance, the [`range()`](../day-028) function expects separate start and stop arguments. If they are not available separately you can call the function with the `*`-operator to unpack the arguments out of a list or tuple:

> Compatibility note: The unpacking generalizations was introduced in Python 3.5. `*[r]` is equivalent  to `list(r)` in later versions, <= 3.4.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> r1 = range(2, 7)    # normal call with separate arguments
>>> list(r1)
[2, 3, 4, 5, 6]

>>> args = [2, 7]
>>> r2 = range(*args)   # call with arguments unpacked from a list
>>> list(r2)
[2, 3, 4, 5, 6]
```

> Note: The parameters passed to the addition function are stored in a tuple. Thus, we can iterate over the args variable.

In the same fashion, dictionaries can deliver keyword arguments with the `**`-operator:

```python
>>> def parrot(voltage, state="a stiff", action="voom"):
        print("-- This parrot wouldn't", action)
        print("if you put", voltage, "volts through it.")
        print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM
if you put four million volts through it.
E's bleedin' demised !
```

Use operator `*` (for tuples) and `**` (for dictionaries):

```python
>>> print(*[1], *[2], 3, *[4, 5])
1 2 3 4 5

>>> def fn(a, b, c, d):
        print(a, b, c, d)

>>> fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
1 2 3 4
```

## References

- Official Python [documentation](https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists).
- What’s New In Python 3.5: [PEP 448 - Additional Unpacking Generalizations](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-448).
