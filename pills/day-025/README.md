# [Python daily pills] Day 025 - Short-circuit evaluation

One more about conditionals! Now it's time to understand what short-circuit evaluation is all about.

Its simple! If you call a function or method on the right side of `and` and `or`, they may not be executed depending on the result on the left side.

Examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> def test():
    print('function is called')
    return True

>>> True and test()
function is called
True

>>> False and test()
False

>>> True or test()
True

>>> False or test()
function is called
True
```

## References

Another great [nkmk blog post](https://note.nkmk.me/en/python-boolean-operation/#:~:text=y-,Short,--circuit%20evaluation).
