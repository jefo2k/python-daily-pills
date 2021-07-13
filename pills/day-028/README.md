# [Python daily pills] Day 028 - The `range()` function

The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

It is a built-in function that returns a `range` object which we can iterate using a [`for`](../day-027) loop.

## Syntax

```python
range(start, stop[, step])
```

## `range(stop)`

When you pass only one argument to the range(), it will generate a sequence of integers starting from 0 to stop -1.

```python
# stop = 6
>>> for i in range(6):
    print(i)

0
1
2
3
4
5
```

> Note: As you can see in the output, We got six integers starting from 0 to 5. If you notice, `range()` didn’t include 6 in its result because it generates numbers up to the stop number but never includes the stop number in its result.

## `range(start, stop)`

When you pass two arguments to the range(), it will generate integers starting from the start number to stop -1.

```python
# start = 10
# stop = 16
>>> for i in range(10, 16):
    print(i)

10
11
12
13
14
15
```

## `range(start, stop, step)`

When you pass all three arguments to the range(), it will return a sequence of numbers, starting from the start number, increments by step number, and stops before a stop number.

```python
# start = 10
# stop = 50
# step = 5
>>> for i in range(10, 40, 5):
    print(i)

10
15
20
25
30
35
```

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## References

- A [pynative tutorial](https://pynative.com/python-range-function/).
- A [w3schools tutorial](https://www.w3schools.com/python/ref_func_range.asp).
