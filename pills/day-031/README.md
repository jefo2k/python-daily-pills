# [Python daily pills] Day 031 - Intro to Python Functions

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

## Creating a Function

In Python a function is defined using the def keyword:

```python
>>> def my_function(fname): ## function definition
  print("Hello " + fname)
```

## Calling a Function

To call a function, use the function name followed by parenthesis:

```python
>>> def my_function(fname):
  print("Hello " + fname)

>>> my_function("World!")   ## function call
Hello World!
```

## Arguments

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma:

```python
>>> def my_function(fname): ## function argument: fname
  print("Hello " + fname)

>>> my_function("Jefo")
Hello Jefo
>>> my_function("Ana")
Hello Ana
>>> my_function("World!")
Hello World!
```

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## References

A awesome [w3schools article](https://www.w3schools.com/python/python_functions.asp).
