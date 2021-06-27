# Python daily pills - Day 012: Python primitive data types in-depth: string, int, float and boolean

Primitive data structures are the simplest forms of representing data.

Python has four primitive data types:

- Integer
- Float
- String
- Boolean

Lets deep dive into each one of them:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Integer

An integer is a whole number that could hold a zero, positive or negative value.

```python
# positive number
>>> number = 25

# negative number
>>> negative_number = -23

>>> zero = 0
```

In Python 3 there are no different integer types as in Python 2.7, which has `int` and `long int`. In Python 3 there is only one integer type, which can store very large numbers:

```python
>>> number = 100000000000000000000000
>>> print(type(number))
<type 'int'> # output
```

## Float

Float represents real numbers, a data type that is used to define floating decimal points.

```python
>>> decimal_number = 25.33
>>> decimal_number_two = 45.2424
```

To convert an `int` or a `string` to a `float` use the `float()` function:

```python
>>> number = 5
>>> print(float(number))
5.0

>>> address_number = "33"
>>> print(float(address_number))
33.0
```

## String

String represents a sequence of characters (text) inside double or single quotes. In Python, strings are immutable so once it's declared the value can't be changed, instead a new object is created:

```python
>>> first_string = "Hello"
>>> second_string = first_string
>>> print(first_string)
Hello
>>> print(second_string)
Hello

# let's change first_string
>>> first_string = "I have changed"
>>> print(first_string)
Hello
```

The string class has a lot of useful methods for string manipulation:

```python
>>> first_name = 'ana'
>>> print(first_name.capitalize())
Ana # First character capitalized

>>> print(first_name.upper())
ANA # All string capitalized

>>> age = 28
>>> "My name is {0} and I'm {1} years old.".format(first_name.capitalize(), age)
'My name is Ana and I'm 28 years old.'
```

> There are plenty of useful methods to check different things like: if the string `startswith()` or `endswith()` some word, or check if a string `isdigit()` or `isnumeric()` . You can refer to the [Python 3 documentation for a full list of string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) or use the `dir` function, as explained in [this pill](../day-002).

## Boolean

Booleans are used to represent truth values with two constant objects True and False.

```python
>>> num = 1
>>> print(bool(num))
True # since Boolean in numeric can be present as 0 or 1

```

## References

Check out the [official Python 3 docs](https://docs.python.org/3/library/stdtypes.html#built-in-typ) for more details.
