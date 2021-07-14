# [Python daily pills] Day 029 - Iterate over two lists or more

The Pythonic style for iterating through a pair of lists, or more, is to use the function `zip`.

## Iterate over two lists of same size

```python
>>> l1 = ['a','b','c']
>>> l2 = [1,2,3]
>>> for x,y in zip(l1,l2):
     print(x,y)

a 1
b 2
c 3
```

## Iterate over three lists of same size

```python
>>> l1 = ['a','b','c']
>>> l2 = [1,2,3]
>>> l3 = ['hello','hi','bye']
>>> for x,y,z in zip(l1,l2,l3):
     print(x,y,z)

a 1 hello
b 2 hi
c 3 bye
```

## Iterate over lists of different sizes

```python
>>> l1 = ['a','b','c','d','e','f']
>>> l2 = [1,2,3]
>>> for x,y in zip(l1,l2):
        print(x,y)

a 1
b 2
c 3
```

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## References

A great [moonbooks article](https://moonbooks.org/Articles/How-to-iterate-over-two-lists-or-more-in-python-/).
