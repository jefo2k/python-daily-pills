# Python daily pills - Day 004: Find element in a list

Now it's time to learn how to find if an element is inside a list.

## Symptoms

You are using a for loop and testing each element to check if it is in the list.

## Remedy

Python offers at least 2 (two) more concise ways to check whether an element is part of a list:

```python
>>> avengers = ['Spider-Man', 'Ant-Man', 'Thor', 'Hulk', 'Captain America', 'Black Panther', 'Iron Man']

# using index function to find the location of an item
>>> idx = avengers.index('Hulk')
>>> idx
3 # 0 based index
>>> idx = avengers.index('Superman')
Traceback (most recent call last):
ValueError: 'Superman' is not in list # Error! Superman isn't in the list

# using in operator to check if something is inside a list
>>> if 'Thor' in avengers:
  print('Thor is an Avenger!')
else:
  print('Not an Avenger...')
...
Thor is an Avenger!
```

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Explanation

The `index` function returns a position of an element on a list if it exists. Return a `ValueError` if the element isn't in the list.

The `in` operator check if the element is inside a list.

## References

For more details about find a element on a list, check this links:

- Index function in [datacamp](https://www.datacamp.com/community/tutorials/python-list-index)
- In operator in [w3schools](https://www.w3schools.com/python/python_operators.asp#:~:text=Python-,Membership,-Operators)
