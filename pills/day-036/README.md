# [Python daily pills] Day 036 - Emulate switch/case statements with dicts and lambdas

Python doesn’t have `switch/case` statements so it’s often necessary to write long `if/elif/else` chains as a workaround. Here’s a little trick you can use to emulate `switch/case` statements in Python using dictionaries and first-class functions.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Chained `if/elif/else`, `switch/case` style:

```python
>>> def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None

>>> dispatch_if('add', 2, 8)
10
>>> dispatch_if('mul', 2, 8)
16
>>> dispatch_if('unknown', 2, 8)
>>>
```

Pythonic style:

```python
>>> def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()

>>> dispatch_dict('add', 2, 8)
10
>>> dispatch_dict('mul', 2, 8)
16
>>> dispatch_dict('unknown', 2, 8)
>>>
```

## References

A cool [realpython lesson](https://realpython.com/courses/emulating-switch-case-python/).
