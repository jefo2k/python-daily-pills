# [Python daily pills] Day 016 - Built-in Data Structures (Part 3): Tuples

Tuples are one of 4 built-in data types in Python used to store collections of data, the other 3 are Sets, [Lists](../day-013) and [Dictionaries](../day-014), all with different qualities and usage.

Tuples are used to store multiple items in a single variable.

Tuples are the same as lists are with the exception that the data once entered into the tuple cannot be changed no matter what.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Creating a Tuple:

```python
>>> my_tuple = (1, 2, 3) #create tuple
>>> my_tuple
(1, 2, 3)

>>> my_other_tuple = tuple([4, 5, 6]) #create tuple from a list
>>> my_other_tuple
(4, 5, 6)
```

> Note: You create a tuple using parenthesis or using the `tuple()` function.

Accessing Elements:

```python
>>> my_tuple2 = (1, 2, 3, 'edureka') #access elements
>>> for x in my_tuple2:
    x
...
1
2
3
'edureka'
>>> my_tuple2
(1, 2, 3, 'edureka')
>>> my_tuple2[0]
1

>>> print(my_tuple2[:])
(1, 2, 3, 'edureka')
>>> print(my_tuple2[3][4]) #access 4th character of element 3, 0 based index
e
```

Appending Elements:

```python
>>> my_tuple = (1, 2, 3)
>>> my_tuple = my_tuple + (4, 5, 6) #add elements
>>> my_tuple
(1, 2, 3, 4, 5, 6)
```

> Note: In the last code snippet, the `+` operator will take another tuple to appended to the original one. The result will be a new tuple assigned to `my_tuple` variable.

Other Functions:

```python
>>> my_tuple = (1, 2, 3, ['hindi', 'python'])
>>> my_tuple[3][0] = 'english' # the list inside a tuple can be modified
>>> my_tuple
(1, 2, 3, ['english', 'python'])

>>> my_tuple[0] = 0 # will throw an error: Tuples are imutables
TypeError: 'tuple' object does not support item assignment

>>> my_tuple.count(2)
1
>>> my_tuple.index(['english', 'python'])
3
```

## References

Check out this [link](https://www.w3schools.com/python/python_tuples.asp) for more details in Python Tuples.
