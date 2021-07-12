# [Python daily pills] Day 026 - While loops

Python has two primitive loop commands:

- `while` loops
- [`for`](../day-027) loops

This pill will be about while loops, a structure that allows executing a set of instructions as long as a condition is true. Let's dive in some examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Print `i` as long as `i` is less than 6:

```python
>>> i = 1
>>> while i < 6:
  print(i)
  i += 1

1
2
3
4
5
```

With the `break` statement we can stop the loop even if the while condition is true:

```python
>>> i = 1
>>> while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

1
2
3
```

With the `continue` statement we can stop the current iteration, and continue with the next:

```python
>>> i = 0
>>> while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

1
2
4
5
6
```

With the `else` statement we can run a block of code once when the condition no longer is true:

```python
>>> i = 1
>>> while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

1
2
3
4
5
i is no longer less than 6
```

## References

- A [w3schools tutorial](https://www.w3schools.com/python/python_while_loops.asp).
- A [realpython tutorial](https://realpython.com/python-while-loop/).
