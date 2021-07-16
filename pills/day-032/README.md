# [Python daily pills] Day 032 - Function Parameters or Arguments?

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

- A parameter is the variable listed inside the parentheses in the function definition
- An argument is the value that is sent to the function when it is called

Now, lets see some examples.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

```python
>>> def my_function(fname, lname):
  print(fname + " " + lname)

>>> my_function("Spider", "Man")
Spider Man
```

> Note: If you try to call the function with 1 or 3 arguments, you will get an error.

## Arbitrary Arguments, `*args`

If you do not know how many arguments that will be passed into your function, add a `*` before the parameter name in the function definition.

```python
>>> def my_function(*avengers):
  print("The youngest avenger is " + avengers[0])

>>> my_function('Spider-Man', 'Thor', 'Hulk', 'Captain America', 'Black Panther', 'Iron Man')
The youngest avenger is Spider-Man
```

> Note: Arbitrary Arguments are often shortened to `*args` in Python documentations.

## Keyword Arguments

You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

```python
>>> def my_function(avenger3, avenger2, avenger1):
  print("The greenish avenger is " + avenger3)
...
>>> my_function(avenger1 = 'Spider-Man', avenger2 = 'Thor', avenger3 = 'Hulk')
The greenish avenger is Hulk
```

> Note: Keyword Arguments are often shortened to `kwargs` in Python documentations.

## Arbitrary Keyword Arguments, `**kwargs`

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.

```python
>>> def my_function(**avenger):
  print("The blondiest of the blondies is " + avenger["blondiest"])
...
>>> my_function(greenish = "Hulk", blondiest = "Thor")
The blondiest of the blondies is Thor
```

> Note: Arbitrary Kword Arguments are often shortened to `**kwargs` in Python documentations.

## References

A awesome [w3schools article](https://www.w3schools.com/python/python_functions.asp).
