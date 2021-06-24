# Python daily pills - Day 003: Sorting lists

This time we will show how easy sort a list in Python is.

## Symptoms

You need to put the elements of a list in order and don't know how.

## Remedy

Use `sort` function:

```python
# sorting a number list
>>> lst = [334, 5, 2, -4, 0, 23, 64, 85, 9, 4]
>>> lst_sorted = sorted(lst)
>>> lst_sorted
[-4, 0, 2, 4, 5, 9, 23, 64, 85, 334]
# descending order
>>> lst_sorted_reverse = sorted(lst, reverse=True)
>>> lst_sorted_reverse
[334, 85, 64, 23, 9, 5, 4, 2, 0, -4]

# sorting a string list
>>> avengers = ['Spider-Man', 'Ant-Man', 'Thor', 'Hulk', 'Captain America', 'Black Panther', 'Iron Man']
>>> avengers_sorted = sorted(avengers)
>>> avengers_sorted
['Ant-Man', 'Black Panther', 'Captain America', 'Hulk', 'Iron Man', 'Spider-Man', 'Thor']
# descending order
>>> avengers_sorted_reverse = sorted(avengers, reverse=True)
>>> avengers_sorted_reverse
['Thor', 'Spider-Man', 'Iron Man', 'Hulk', 'Captain America', 'Black Panther', 'Ant-Man']
```

> Note: the "`>>>`" in the example above indicates that the command was executed in the Python interpreter, also known as [REPL](https://docs.python.org/3/tutorial/interpreter.html)

## Explanation

The `sorted` function sorts the elements of a given iterable in a specific order (either ascending or descending) and returns the sorted iterable as a list.

The syntax of the `sorted` function is:

```python
sorted(iterable, key=None, reverse=False)
```

## References

For more details about sorting lists check this links:

- [docs.python.org](https://docs.python.org/3/library/stdtypes.html?highlight=sort#list.sort)
- [programiz](https://www.programiz.com/python-programming/methods/built-in/sorted)
