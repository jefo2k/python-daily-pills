# [Python daily pills] Day 020 - Sort a Dictionary by Value

To sort a dictionary by value in Python you can use the `sorted()` function.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

## Sort in Ascending Order

```python
>>> orders = {
        'cappuccino': 54,
        'latte': 56,
        'espresso': 72,
        'americano': 48,
        'cortado': 41
}
>>> sort_orders = sorted(orders.items(), key=lambda x: x[1])
>>> sort_orders
[('cortado', 41), ('americano', 48), ('cappuccino', 54), ('latte', 56), ('espresso', 72)]
```

## Sort in Descending Order

```python
>>> orders = {
        'cappuccino': 54,
        'latte': 56,
        'espresso': 72,
        'americano': 48,
        'cortado': 41
}
>>> sort_orders = sorted(orders.items(), key=lambda x: x[1], reverse=True)
>>> sort_orders
[('espresso', 72), ('latte', 56), ('cappuccino', 54), ('americano', 48), ('cortado', 41)]
```

> If you don't know what a Python dictionary is please check out [this pill](../day-014).

## References

From [careerkarma](https://careerkarma.com/blog/python-sort-a-dictionary-by-value/).
