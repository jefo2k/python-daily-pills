# [Python daily pills] Day 027 - For Loops

As the `while` loop we covered in the [last pill](../day-026), a `for` loop is used for iterating over a sequence that is either a list, a tuple, a dictionary, a set, or a string.

This structure is less like the `for` keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

Lets see some examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Print each fruit in a fruit list:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in fruits:
  print(x)

apple
banana
cherry
```

Even strings are iterable objects, they contain a sequence of characters:

```python
>>> for x in "banana":
  print(x)

b
a
n
a
n
a
```

With the `break` statement we can stop the loop before it has looped through all the items:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in fruits:
  if x == "banana":
    break
  print(x)

apple
```

With the `continue` statement we can stop the current iteration of the loop, and continue with the next:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in fruits:
  if x == "banana":
    continue
  print(x)

apple
cherry
```

The `else` keyword in a `for` loop specifies a block of code to be executed when the loop is finished:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> for x in fruits:
  if x == "banana":
    continue
  print(x)
else:
  print("Finally finished!")

apple
cherry
Finally finished!
```

> Note: The `else` block will NOT be executed if the loop is stopped by a `break` statement.

## References

A [w3schools tutorial](https://www.w3schools.com/python/python_for_loops.asp).
