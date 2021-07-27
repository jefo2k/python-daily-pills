# [Python daily pills] Day 042 - List Comprehensions

Python is famous for allowing you to write code that’s elegant, easy to write, and almost as easy to read as plain English. One of the language’s most distinctive features is the list comprehension, which you can use to create powerful functionality within a single line of code.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
# Iterating through a string
>>> h_letters = [ letter for letter in 'human' ]
>>> h_letters
['h', 'u', 'm', 'a', 'n']

# if with List Comprehension
>>> even_list = [ x for x in range(20) if x % 2 == 0 ]
>>> even_list
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# if...else With List Comprehension
>>> obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
>>> obj
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

## References

A [programiz tutorial](https://www.programiz.com/python-programming/list-comprehension).
