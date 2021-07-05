# [Python daily pills] Day 021 - Python slice notation 101

Python supports slice notation for any sequential data type like [lists](../day-013), strings, [tuples](../day-016), bytes, bytearrays, and ranges.

Slice notation it's pretty simple:

```shell
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
```

There is also the `step` value, which can be used with any of the above:

```shell
a[start:stop:step] # start through not past stop, by step
```

`start` or `stop` may be a negative number, which means it counts from the end of the array instead of the beginning. So:

```shell
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items
```

Similarly, step may be a negative number:

```shell
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```

> Note: Python is kind to the programmer if there are fewer items than you ask for. For example, if you ask for `a[:-2]` and a only contains one element, you get an `empty list` instead of an `error`. Sometimes you would prefer the `error`, so you have to be aware that this may happen.

In the next pill we are going to show some examples.

## References

From this nice [stackoverflow thread](https://stackoverflow.com/questions/509211/understanding-slice-notation?page=1&tab=votes#tab-top).
