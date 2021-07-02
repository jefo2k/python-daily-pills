# [Python daily pills] Day 014 - Built-in Data Structures (Part 2): Dictionaries

Dictionaries are one of 4 built-in data types in Python used to store collections of data, the other 3 are [Tuples](../day-016), [Sets](../day-017), and [Lists](../day-013), all with different qualities and usage.

Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

> \* As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Create Dictionaries:

```python
>>> my_dict = {} #empty dictionary
>>> my_dict
{}

>>> my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
>>> my_dict
{1: 'Python', 2: 'Java'}
```

Changing and Adding key, value pairs:

```python
>>> my_dict = {'First': 'Python', 'Second': 'Java'}
>>> my_dict
{'First': 'Python', 'Second': 'Java'}

>>> my_dict['Second'] = 'C++' #changing element
>>> my_dict
{'First': 'Python', 'Second': 'C++'}

>>> my_dict['Third'] = 'Ruby' #adding key-value pair
>>> my_dict
{'First': 'Python', 'Second': 'C++', 'Third': 'Ruby'}
```

Deleting key, value pairs:

```python
>>> my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
>>> a = my_dict.pop('Third') #pop element (value)
>>> print('Value:', a)
Value: Ruby
>>> my_dict
{'First': 'Python', 'Second': 'Java'}

>>> b = my_dict.popitem() #pop the key-value pair
>>> print('Key, value pair:', b)
Key, value pair: ('Second', 'Java')
>>> my_dict
{'First': 'Python'}

>>> my_dict.clear() #empty dictionary
>>> my_dict
{}
```

Access Elements:

```python
>>> my_dict = {'First': 'Python', 'Second': 'Java'}
>>> my_dict['First'] #access elements using keys option 1
'Python'

>>> my_dict.get('Second') #access elements using keys option 2
'Java'
```

Other Functions:

```python
>>> my_dict = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
>>> my_dict.keys() #get keys
dict_keys(['First', 'Second', 'Third'])

>>> my_dict.values() #get values
dict_values(['Python', 'Java', 'Ruby'])

>>> my_dict.items() #get key-value pairs
dict_items([('First', 'Python'), ('Second', 'Java'), ('Third', 'Ruby')])
```

## References

Check out this [link](https://www.w3schools.com/python/python_dictionaries.asp) for more details in Python Dictionaries.
