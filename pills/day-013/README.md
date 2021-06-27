# [Python daily pills] Day 013 - Built-in Data Structures (Part 1): Lists

Lists in Python are used to store collection of heterogeneous items. These are mutable, which means that you can change their content without changing their identity. 

You can recognize lists by their square brackets `[` and `]` that hold elements, separated by a comma `,`. 

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

> Note: We have used the Python interpreter, also known as `REPL`, to run the examples. If you don't know what `REPL` is, please [take this pill](../day-005).

Create a List:

```python
# string list 
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits
['apple', 'banana', 'cherry']

# int list 
>>> calories = [52, 89, 50] # calories for each 100 grams
>>> calories
[52, 89, 50]

# list with strings, integers and boolean values
>>> list = ["abc", 34, True, 40, "male"]
>>> list
['abc', 34, True, 40, 'male']
```

Add Elements:

```python
>>> fruits = ["apple", "banana", "cherry"]
>>> fruits
['apple', 'banana', 'cherry']

# add as a single element
>>> fruits.append("watermelon")
>>> fruits
['apple', 'banana', 'cherry', 'watermelon']

# add another list as elements
>>> fruits.extend(["lemon", "orange"])
>>> fruits
['apple', 'banana', 'cherry', 'watermelon', 'lemon', 'orange']

>>> fruits.insert(0, 'pineapple') #add element at i-th position, 0 based index
>>> fruits
['pineapple', 'apple', 'banana', 'cherry', 'watermelon', 'lemon', 'orange']
```

Delete Elements:

```python
>>> my_list = [1, 2, 3, 'example', 3.132, 10, 30]
>>> del my_list[5] #delete element at index 5
>>> my_list
[1, 2, 3, 'example', 3.132, 30]

>>> my_list.remove('example') #remove element with value
>>> my_list
[1, 2, 3, 3.132, 30]

>>> a = my_list.pop(1) #pop element from list at i-th position, 0 based index
'Popped Element: ', a, ' List remaining: ', my_list
('Popped Element: ', 2, ' List remaining: ', [1, 3, 3.132, 30])

>>> my_list.clear() #empty the list
>>> my_list
[]
```

Access Elements:

```python
>>> my_list = [1, 2, 3, 'example', 3.132, 10, 30]
>>> for element in my_list: #access elements one by one
    print(element)
...
1
2
3
example
3.132
10
30
>>> print(my_list) #access all elements
[1, 2, 3, 'example', 3.132, 10, 30]
>>> print(my_list[3]) #access index 3 element
example
>>> print(my_list[0:2]) #access elements from 0 to 1 and exclude 2
[1, 2]
>>> print(my_list[::-1]) #access elements in reverse
[30, 10, 3.132, 'example', 3, 2, 1]
```

Other Functions:

```python
>>> my_list = [1, 2, 3, 10, 30, 10]
>>> len(my_list) #find length of list
6

>>> my_list.index(10) #find index of element that occurs first
3

>>> my_list.count(10) #find count of the element
2

>>> sorted(my_list) #print sorted list but not change original
[1, 2, 3, 10, 10, 30]

>>> my_list.sort(reverse=True) #sort original list
>>> my_list
[30, 10, 10, 3, 2, 1]
```

## References

Check out this [link](https://www.w3schools.com/python/python_lists.asp) for more details in Python Lists.
