# [Python daily pills] Day 017 - Built-in Data Structures (Part 3): Sets

Sets are one of 4 built-in data types in Python used to store collections of data, the other 3 are [Tuples](../day-016), [Dictionaries](../day-014), and [Lists](../day-013), all with different qualities and usage.

Sets are defined within curly brackets

Sets are collections that are both unordered and unindexed

> As a result of this, we can't access the elements of a set the way we would a list or a tuple

Sets don't hold duplicate values

> Elaborated below

Creating Sets:

```python
>>> my_set = {5,3,9,7}
>>> my_set #Observe below how the elements are in a different order than initialized
{9, 3, 5, 7}
>>> my_set = set((1,4,6,8)) #Other ways to create a set
>>> my_set
{8, 1, 4, 6}
>>> my_set = set([5,3,9,8]) #Lists, tuples and dictionaries can also be created this way
>>> my_set
{8, 9, 3, 5}
```
Set Functions:

```python
>>> dir(set) #Lists all the set functions (It isn't as scary as it looks, trust me :D)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
```

Example functions:

```python
>>> my_set.add('another element') #adds an element to the set
>>> my_set
{1, 4, 6, 'another element', 8}
>>> my_set.remove('another element')#removes the specified element
>>> my_set
{1, 4, 6, 8}
>>> my_set.pop() #removes a random element
1
>>> my_set
{4, 6, 8}
```

Duplicate elements:

```python
>>> my_set = {1,1,2,3,4,5,6,6,7,7,7,8}
>>> my_set #Observe that only a single occurance of an element is stored
{1, 2, 3, 4, 5, 6, 7, 8}
```
> If you want to remove duplicate elements in a list or a tuple, a neat trick is to convert them into a set first and then back to either a list or tuple :D

## References

Check out this [link](https://www.w3schools.com/python/python_sets.asp) for more details in Python Sets.
