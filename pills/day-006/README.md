# [Python daily pills] Day 006 -  Python Indentation

Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

```python
if 5 > 2:
  print("Five is greater than two!")
```

Python will give you an error if you skip the indentation

```python
if 5 > 2:
print("Five is greater than two!") # Syntax Error
```

The number of spaces is up to you, but it has to be at least one.

```python
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
```

You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:

```python
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!") # Syntax Error
```

## References

More information about identation [check this link out](https://pythonexamples.org/python-indentation).
