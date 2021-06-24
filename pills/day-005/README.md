# Python daily pills - Day 005: The Python Command Line (REPL)

To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be used as a command line in an environment called REPL.

REPL stands for Read, Evaluate, Print, Loop. The REPL is how you interact with the Python Interpreter.

With Python installed, type the following on the Windows, Mac or Linux command line:

```python
> python
```

Or, if the "python" command did not work, you can try "py":

```python
> py
```

The result must be something like that:

```python
Python 3.7.2 (default, Apr  6 2020, 14:21:53)
[Clang 11.0.3 (clang-1103.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

> Note, in the REPL three arrows >>> indicate a line of input given at the prompt. If you see these arrows in example code, don’t copy them into your own REPL. Later, when we run out Python code from files, you will no longer see the triple arrows.

From there you can try some Python commands:

```python
# My REPL. Don't copy the >>> symbols, that means the code was entered
# into the prompt.
#
# If the line does not start with >>>, that means it is output,
# not input
>>> message = "Hello!"
>>> message
'Hello!'
>>> x = 5
>>> y = 3
>>> x + y
8
>>> x - y
2
>>> x * y
15
>>> x / y
1.6666666666666667
>>>
```

To quit REPL:

```python
>>> quit()
```

## References

For more info about Python interpreter (REPL) [click here](https://www.tutorialsteacher.com/python/python-interective-shell).
