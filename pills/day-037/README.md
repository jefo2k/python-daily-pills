# [Python daily pills] Day 037 - Shrink your code with lambdas

For programmers who are skilled at reducing their codes into simple logical statements, [Lambda](../day-035) functions help shrink the number of lines dramatically.

Lets see some examples:

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Take a look of this function:

```python
>>> def mult_int(original, multiplier):
    return original * multiplier

>>> mult_int(5, 11)
55
```

The condensed version, with a lambda function, will be like that:

```python
>>> mult_int = lambda i, j : i * j
>>> mult_int(5, 11)
55
```

A more complicated one:

```python
>>> def complicated_function(a, b, c, d, e):
    return ((a+b) / (c+d)) * e

>>> complicated_function(1, 2, 3, 4, 5)
2.142857142857143
```

Again we can condense this entire function into a lambda function:

```python
>>> complicated_function = lambda i,j,k,l,m : ((i + j) / (k + l)) * m
>>> complicated_function(1, 2, 3, 4, 5)
2.142857142857143
```

Lets dig in a example using `If-Else` statements to create much more interesting function:

```python
>>> def odd_even(figure):
    if figure % 2 == 0:
        return 'Number is Even'
    else:
        return 'Number is Odd'

>>> odd_even(2)
'Number is Even'
```

This too can be collapsed into a one-line lambda function:

```python
>>> odd_even_lambda = lambda i: 'Number is Even' if i % 2 ==0 else 'Number is Odd'
>>> odd_even_lambda(3)
'Number is Odd'
```

## References

A great [towardsdatascience article](https://towardsdatascience.com/pythonic-tips-tricks-working-with-lambda-987444d80517).
