# [Python daily pills] Day 023 - Conditions and `if..elif..else` statements

Python supports the usual logical conditions from mathematics:

- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

Conditions can be combined with the logical operators `and` and `or`:

- `a < b and b > 0`: The two conditions must be `True`
- `a < b or b > 0`: At least one condition must be `True`

Conditions can be used in several ways, most commonly in `if` statements and loops. Let's jump to some examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## The `if` statement

The `if` statement will execute a subsequent code, or code block, when the condition is `True`.

```python
>>> a = 33
>>> b = 200
>>> if b > a:
  print("b is greater than a")

b is greater than a
```

> Note: Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

## `elif` statement

If the previous conditions were not true, the `elif` condition will be evaluated. The subsequent code will be executed if these condition is `True`.

```python
>>> a = 33
>>> b = 33
>>> if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a and b are equal
```

## `else` statement

`else` catches anything which isn't caught by the preceding conditions.

```python
>>> a = 200
>>> b = 33
>>> if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
...
a is greater than b
```

## Short Hands

If you have only one statement to execute, you can put it on the same line as the `if` and `else` statements.

```python
>>> a = 2
>>> b = 330
>>> if a < b: print("a is greater than b")
a is greater than b

>>> print("A") if a > b else print("B")
B
```

> Note: The last short hand example shows a technique known as Ternary Operators, or Conditional Expressions.

## References

 [w3schools](https://www.w3schools.com/python/python_conditions.asp).