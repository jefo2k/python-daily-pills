# [Python daily pills] Day 024 - Chain of multiple comparisons

Continuing in the conditionals topic, an interesting Python's feature is that comparisons can be chained. 

You can write `a < x and x < b` as `a < x < b` like in mathematics.

Formally, if `a,b, c, ..., y, z` are expressions and `op1, op2, ..., opN` are comparison operator (such as `<` or `>`), the following two are equivalent:

```python
a op1 b op2 c ... y opN z
a op1 b and b op2 c and ... y opN z
```

Examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> x = 15
>>> 10 < x and x < 20
True
>>> 10 < x < 20   # equivalent to: 10 < x and x < 20
True

>>> y = 25
>>> 0 < x and x < 20 and 20 < y and y < 30
True
>>> 10 < x < 20 < y < 30   # equivalent to: 0 < x and x < 20 and 20 < y and y < 30
True
```

## Most common uses

When a range of numbers is used as a condition, chained comparisons is useful:

```python
>>> x = 15
>>> if 10 < x < 20:
    print('result: 10 < x < 20')
else:
    print('result: x <= 10 or 20 <= x')

result: 10 < x < 20

```

Check if multiple values are all equal is another case where chaining comes in handy:

```python
>>> a = 10
>>> b = 10
>>> c = 10
>>> if a == b == c:
    print('all equal')
else:
    print('not all equal')

all equal
```

## References

A great [nkmk blog post](https://note.nkmk.me/en/python-chain-comparisons/).
