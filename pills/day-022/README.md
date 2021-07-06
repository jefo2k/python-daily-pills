# [Python daily pills] Day 022 - Python slice notation examples

In the previous [pill](../day-021) we discussed what slice notation is all about. Now it's time to see some examples.

Basic usage helper, `a[start:stop:step]`, so:

> Note: Indexing in most of the programming languages, including Python, starts from 0.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

```python
>>> sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
>>> sea_creatures[1:4]  # from start (1) through stop-1 (4 - 1 = 3)
['cuttlefish', 'squid', 'mantis shrimp']

>>> sea_creatures[1:]   # from start (1) through the rest of the list
['cuttlefish', 'squid', 'mantis shrimp', 'anemone']

>>> sea_creatures[:4]   # from the beginning (0) through stop-1 (4 - 1 = 3)
['shark', 'cuttlefish', 'squid', 'mantis shrimp']

>>> sea_creatures[:]    # a copy of the whole list, same as sea_creatures[::1]
['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']

>>> sea_creatures[::2]  # from the beginning to the end using step 2
['shark', 'squid', 'anemone']
```

Using negative numbers in `start` or `stop`, which means it counts from the end of the list instead of the beginning:

```python
>>> sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
>>> sea_creatures[-1]     # last item in the list
'anemone'

>>> sea_creatures[-2:]    # last two items in the list
['mantis shrimp', 'anemone']

>>> sea_creatures[:-2]    # everything except the last two items
['shark', 'cuttlefish', 'squid']

>>> sea_creatures[::-1]   # all items in the list, reversed
['anemone', 'mantis shrimp', 'squid', 'cuttlefish', 'shark']

>>> sea_creatures[1::-1]  # the first two items, reversed
['cuttlefish', 'shark']

>>> sea_creatures[:-3:-1] # the last two items, reversed
['anemone', 'mantis shrimp']

>>> sea_creatures[-3::-1] # everything except the last two items, reversed
['squid', 'cuttlefish', 'shark']
```

> Reminder: If you ask for `a[:-2]` and `a` only contains one element, you get an `empty list` instead of an `error`. Sometimes you would prefer the `error`, so you have to be aware that this may happen.

## References

- A nice [stackoverflow thread](https://stackoverflow.com/questions/509211/understanding-slice-notation?page=1&tab=votes#tab-top).
- This awesome [railsware blog post](https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/).
