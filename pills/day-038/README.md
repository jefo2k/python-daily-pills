# [Python daily pills] Day 038 - 6 ways to reverse a string in Python

Python String doesn’t have a built-in `reverse()` function. However, there are various ways to reverse a string in Python.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Using `for` Loop

```python
>>> string = "Hello World!"
>>> reversed_string = ""
>>> for c in string:
        reversed_string = c + reversed_string

>>> reversed_string
'!dlroW olleH'
```

## Using `while` Loop

```python
>>> string = "Hello World!"
>>> reversed_string = ""
>>> length = len(string) - 1
>>> while length >= 0:
        reversed_string = reversed_string + string[length]
        length = length - 1

>>> reversed_string
'!dlroW olleH'
```

## Using [`join()`](https://docs.python.org/3/library/stdtypes.html#str.join) and [`reversed()`](https://docs.python.org/3/library/functions.html#reversed)

```python
>>> string = "Hello World!"
>>> ''.join(reversed(string))
'!dlroW olleH'
```

## Using recursion

```python
>>> def reverse_recursion(s):
        if len(s) == 0:
            return s
        else:
            return reverse_recursion(s[1:]) + s[0]

>>> reverse_recursion("Hello World!")
'!dlroW olleH'
```

## Using List `reverse()`

```python
>>> string = "Hello World!"
>>> temp_list = list(string)
>>> temp_list.reverse()
>>> ''.join(temp_list)
'!dlroW olleH'
```

## Using slicing

```python
>>> string = "Hello World!"
>>> string[::-1]
'!dlroW olleH'
```

> Note: The fastest (and easiest?) way is to use a slice that steps backwards, -1.

## References

- A nice [journaldev article](https://www.journaldev.com/23647/python-reverse-string).
- Another great [w3schools tutorial](https://www.w3schools.com/python/python_howto_reverse_string.asp).
