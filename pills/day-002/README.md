# Python daily pills - Day 002: The dir function

In this pill we will cover a powerful inbuilt function in Python3, the `dir` funcition.

## Symptoms

You are not sure about the attributes and methods of an object.

## Remedy

Use the `dir` function:

```python
>>> s = 'a simple string'
>>> print(dir(s))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

> Note: the "`>>>`" in the example above indicates that the command was executed in the Python interpreter, also known as [REPL](https://docs.python.org/3/tutorial/interpreter.html)

## Explanation

The dir function returns a list of valid attributes for the object in its argument, which means we can use it to return an object’s methods.

> Note: dir only provides an interesting set of names more than a full list.

## References

For more details about the dir function, [check this out](https://docs.python.org/3/library/functions.html#dir).
