# [Python daily pills] Day 030 - Nested For Loops

Loops can be nested in Python, as they can with other programming languages.

## Syntax

```python
for [first iterating variable] in [outer loop]: # Outer loop
    [do something]  # Optional
    for [second iterating variable] in [nested loop]:   # Nested loop
        [do something]
```

## Example 1

```python
>>> num_list = [1, 2, 3]
>>> alpha_list = ['a', 'b', 'c']
>>> for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)

1
a
b
c
2
a
b
c
3
a
b
c
```

## Example 2

```python
>>> list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]
>>> for list in list_of_lists:
    for item in list:
        print(item)
...
hammerhead
great white
dogfish
0
1
2
9.9
8.8
7.7
```

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## References

A nice [digitalocean article](https://www.digitalocean.com/community/tutorials/how-to-construct-for-loops-in-python-3).
