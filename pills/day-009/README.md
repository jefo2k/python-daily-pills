# Python daily pills - Day 009: Python Data Types

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Type | Python data type constructor | Example
--- | --- | ---
Text | `str` | `"Hello World"`
Numeric | `int, float, complex` | `2013`, `20.5`, `1j`
Sequence | `list, tuple, range` | `["apple", "banana", "cherry"]`, `("apple", "banana", "cherry")`, `range(6)`
Mapping | `dict` | `{"name" : "John", "age" : 36}`
Set | `set, frozenset` | `{"apple", "banana", "cherry"}`, `frozenset({"apple", "banana", "cherry"})`
Boolean | `bool` | `True`
Binary | `bytes, bytearray, memoryview` | `b"Hello"`, `bytearray(5)`, `memoryview(bytes(5))`

Examples:

```python
# Data type is set when you assign a value to a variable
>>> x = "Hello World"						      # str
>>> x = 2013								      # int
>>> x = 20.5								      # float
>>> x = 1j								          # complex
>>> x = ["apple", "banana", "cherry"]			  # list
>>> x = ("apple", "banana", "cherry")			  # tuple
>>> x = range(6)							      # range
>>> x = {"name" : "John", "age" : 36}			  # dict
>>> x = {"apple", "banana", "cherry"}			  # set
>>> x = frozenset({"apple", "banana", "cherry"})  # frozenset
>>> x = True								      # bool
>>> x = b"Hello"							      # bytes
>>> x = bytearray(5)						      # bytearray
>>> x = memoryview(bytes(5))				      # memoryview

# To specify the data type, you can use constructor functions
>>> x = str("Hello World")					      # str
>>> x = int(20)							          # int
>>> x = float(20.5)						          # float
>>> x = complex(1j)						          # complex
>>> x = list(("apple", "banana", "cherry"))		  # list
>>> x = tuple(("apple", "banana", "cherry"))      # tuple
>>> x = range(6)							      # range
>>> x = dict(name="John", age=36)			      # dict
>>> x = set(("apple", "banana", "cherry"))		  # set
>>> x = frozenset(("apple", "banana", "cherry"))  # frozenset
>>> x = bool(5)							          # bool
>>> x = bytes(5)							      # bytes
>>> x = bytearray(5)						      # bytearray
>>> x = memoryview(bytes(5))				      # memoryview

# To get the datatype use the type function
>>> x = 5
print(type(x))
<class 'int'>
```

## References

More information about Python data types [in this link](https://www.w3schools.com/python/python_datatypes.asp).