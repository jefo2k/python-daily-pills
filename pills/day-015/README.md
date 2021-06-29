# [Python daily pills] Day 015 - Pretty Print a Dictionary in Python

As we just introduce dictionaries in the [last pill](../day-014), this one will cover ways to present them in a more readable style:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Using pprint()

[`pprint`](https://docs.python.org/3/library/pprint.html) is a Python module that provides the capability to pretty print Python data types to be more readable. This module also supports pretty-printing dictionary.

```python
>>> import pprint
>>> dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]
>>> pprint.pprint(dct_arr)
[{'Age': '23', 'Country': 'USA', 'Name': 'John'},
 {'Age': '44', 'Country': 'Spain', 'Name': 'Jose'},
 {'Age': '29', 'Country': 'UK', 'Name': 'Anne'},
 {'Age': '35', 'Country': 'Japan', 'Name': 'Lee'}]
```

To compare, below is the output of a normal `print()` statement:

```python
[{'Name': 'John', 'Age': '23', 'Country': 'USA'}, {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'}, {'Name': 'Anne', 'Age': '29', 'Country': 'UK'}, {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}]
```

> Note: `pprint` will not pretty print nested objects, including nested dictionaries. So if you expect your values to be nested, then this is not the solution for that as well.

## Using json.dumps()

The [`json`](https://docs.python.org/3/library/json.html) module has a function called `dumps()`, which  converts a Python object into a JSON string and also formats the dictionary into a pretty JSON format.

```python
>>> import json
>>> dct_arr = [
  {'Name': 'John', 'Age': '23', 'Country': 'USA'},
  {'Name': 'Jose', 'Age': '44', 'Country': 'Spain'},
  {'Name': 'Anne', 'Age': '29', 'Country': 'UK'},
  {'Name': 'Lee', 'Age': '35', 'Country': 'Japan'}
]
>>> print(json.dumps(dct_arr, sort_keys=False, indent=4))
[
    {
        "Name": "John",
        "Age": "23",
        "Country": "USA"
    },
    {
        "Name": "Jose",
        "Age": "44",
        "Country": "Spain"
    },
    {
        "Name": "Anne",
        "Age": "29",
        "Country": "UK"
    },
    {
        "Name": "Lee",
        "Age": "35",
        "Country": "Japan"
    }
]
```

What if the values given have a nested dictionary within them? Let’s edit the example a bit and take a look at the output.

```python
>>> import json
>>> dct_arr = [
  {'Name': 'John', 'Age': '23', 'Residence': {'Country':'USA', 'City': 'New York'}},
  {'Name': 'Jose', 'Age': '44', 'Residence': {'Country':'Spain', 'City': 'Madrid'}},
  {'Name': 'Anne', 'Age': '29', 'Residence': {'Country':'UK', 'City': 'England'}},
  {'Name': 'Lee', 'Age': '35', 'Residence': {'Country':'Japan', 'City': 'Osaka'}}
]
>>> print(json.dumps(dct_arr, sort_keys=False, indent=4))
[
    {
        "Name": "John",
        "Age": "23",
        "Residence": {
            "Country": "USA",
            "City": "New York"
        }
    },
    {
        "Name": "Jose",
        "Age": "44",
        "Residence": {
            "Country": "Spain",
            "City": "Madrid"
        }
    },
    {
        "Name": "Anne",
        "Age": "29",
        "Residence": {
            "Country": "UK",
            "City": "England"
        }
    },
    {
        "Name": "Lee",
        "Age": "35",
        "Residence": {
            "Country": "Japan",
            "City": "Osaka"
        }
    }
]
```

> The `dumps()` function accepts 3 parameters used for pretty printing: the object for conversion, a boolean value sort_keys, which determines whether the entries should be sorted by key, and indent, which specifies the number of spaces for indentation.

## References

Check out this [link](https://www.delftstack.com/howto/python/python-pretty-print-dictionary/) for more details about pretty print a dictionary in Python.
