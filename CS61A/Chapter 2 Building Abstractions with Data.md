# Chapter 2: Building Abstractions with Data

## 2.1 native data types

Every value in Python has a *class* that determines what type of value it is. Values that share a class also share behavior.

Python includes three native numeric types: integers (`int`), real numbers (`float`), and complex numbers (`complex`).

## 2.2 data abstraction

The general technique of isolating the parts of a program that deal with how data are represented from the parts that deal with how data are manipulated is a powerful design methodology called **data abstraction**. Data abstraction makes programs much easier to design, maintain, and modify.

### rational numbers

- `rational(n, d)` returns the rational number with numerator `n` and denominator `d`.

  ```python
  >>> def rational(n, d):
          return [n, d]
  ```

- `numer(x)` returns the numerator of the rational number `x`.

  ```python
  >>> def numer(x):
          return x[0]
  ```

- `denom(x)` returns the denominator of the rational number `x`.

  ```python
  >>> def denom(x):
          return x[1]
  ```

### abstraction barriers

Maybe the most important idea that software designers and programmers must understand is the abstraction barrier. Instead of doing some complex operations inline, you extract them out into a function, you name that function. Now you have a **barrier**, where you don’t really have to think about the internals of how this thing gets calculated, you have an operation that’s got a nice, clear, meaningful name that you’re working on. 

Every piece of software has, or should have, an abstraction barrier that divides the world into two parts: clients and implementors. The clients are those who use the software. The implementors are those who build it.

For rational numbers, different parts of the program manipulate rational numbers using different operations, as described in this table.

| **Parts of the program that...**                  | **Treat rationals as...**   | **Using only...**                                            |
| :------------------------------------------------ | :-------------------------- | :----------------------------------------------------------- |
| Use rational numbers to perform computation       | whole data values           | `add_rational, mul_rational, rationals_are_equal, print_rational` |
| Create rationals or implement rational operations | numerators and denominators | `rational, numer, denom`                                     |
| Implement selectors and constructor for rationals | two-element lists           | list literals and element selection                          |

In each layer above, the functions in the final column enforce an abstraction barrier. These functions are called by a higher level and implemented using a lower level of abstraction.

## 2.3 sequences

序列类型包括`list`和`string`等，所有序列类型的数据都满足以下两个共同特征：

- **Length.** A sequence has a finite length. An empty sequence has length 0.

- **Element selection.** A sequence has an element corresponding to any non-negative integer index less than its length, starting at 0 for the first element.

### list

采用`for`语句对`list`中的元素进行迭代。关于数据能行能否被迭代(iterable)将在第4章被详细介绍。

**Sequence unpacking**：如果一个list中的每个元素都有固定的长度，那么可以使用`for`语句进行unpacking。如下所示，判断数列中每个数值对中的两个数是否相等：

```python
>>> pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]

>>> for x, y in pairs:
        if x == y:
            same_count = same_count + 1
>>> same_count
2
```

**Ranges**：A range is another built-in type of sequence in Python, which represents a range of integers. Ranges are created with range, which takes **two integer arguments**: the first number and one beyond the last number in the desired range.

```python
>>> range(1, 10)  # Includes 1, but not 10
range(1, 10)
```

**List Comprehensions**

- 许多对数列的处理操作可以表示为对数列中每个元素进行操作，并将得到的结果保存在一个结果数列中，就像下面所表示的一样：

  ```python
  >>> odds = [1, 3, 5, 7, 9]
  >>> [x+1 for x in odds]
  [2, 4, 6, 8, 10]
  ```

- 除此之外，还有一种常见操作是从数列中挑选满足一定条件的值，并将这些特定值组成一个新的数列，如下所示：

  ```
  >>> [x for x in odds if 25 % x == 0]
  [1, 5]
  ```

下面给出了**List Comprehensions**的一般形式：

```
[<map expression> for <name> in <sequence expression> if <filter expression>]
```

**Aggregation**：第3种对于序列的常见操作是将序列中的所有值聚合成一个值，例如对数列进行`max`操作等。

**Membership**：检查一个值是否存在于某个序列中：

```python
>>> digits
[1, 8, 2, 8]
>>> 2 in digits
True
>>> 1828 not in digits
True
```

**Slicing**：对序列中特定的片段进行选取。

```python
>>> digits[0:2]
[1, 8]
>>> digits[1:]
[8, 2, 8]
```

序列之所以有这么多内置的`abstraction`是因为其使用非常普遍，虽然内置的`abstraction`会增加学习成本。不过对于自定义的`abstraction`而言，保持尽可能的简单是很有必要的。

### trees

A tree has a **root** label and a sequence of branches. Each **branch** of a tree is a tree. A tree with no branches is called a **leaf**. Any tree contained within a tree is called a sub-tree of that tree (such as a branch of a branch). The root of each sub-tree of a tree is called a **node** in that tree.

## 2.4 mutable data

We have seen how abstraction is vital in helping us to cope with the complexity of large systems. Effective programming also requires **organizational principles** that can guide us in formulating the overall design of a program. In particular, we need strategies to help us **structure large systems to be modular**, meaning that they divide naturally into coherent parts that can be separately developed and maintained.

One powerful technique for creating modular programs is to **incorporate data that may change state over time**. In this way, a single data object can represent something that evolves independently of the rest of the program. The behavior of a changing object may be influenced by its history, just like an entity in the world. **Adding state to data is a central ingredient of a paradigm called object-oriented programming**.

### object metaphor【重要内容】

In the beginning of this text, we distinguished between functions and data: functions performed operations and data were operated upon.

Objects combine data values with behavior. Objects represent information, but also behave like the things that they represent. Objects are both information and processes, bundled together to represent the properties, interactions, and behaviors of complex things.

A date is a kind of object.

```python
>>> from datetime import date
```

The name `date` is bound to a *class*. As we have seen, a class represents a kind of value. Individual dates are called **instances** of that class. Instances can be *constructed* by calling the class on arguments that characterize the instance.

```python
>>> tues = date(2014, 5, 13)
```

**Objects have *attributes***, which are named values that are part of the object. In Python, like many other programming languages, we use dot notation to designate an attribute of an object.

```python
>>> tues.year
2014
```

**Objects also have *methods*,** which are function-valued attributes. Metaphorically, we say that the object "knows" how to carry out those methods. By implementation, methods are functions that compute their results from both their arguments and their object.

```python
>>> tues.strftime('%A, %B %d')
'Tuesday, May 13'
```

Computing the return value of `strftime` requires two inputs: the string that describes the format of the output and the date information bundled into `tues`.

Dates are objects, but **numbers, strings, lists, and ranges are all objects as well**. They represent values, but also behave in a manner that befits the values they represent. They also have attributes and methods.

```python
>>> '1234'.isnumeric()
True
>>> 'rOBERT dE nIRO'.swapcase()
'Robert De Niro'
>>> 'eyes'.upper().endswith('YES')
True
```

**In fact, all values in Python are objects.** That is, all values have behavior and attributes. They act like the values they represent.

### sequence objects

Instances of primitive built-in values such as numbers are immutable. The values themselves cannot change over the course of program execution. **Lists on the other hand are mutable.**也正因为数组的可变性，在对数组进行操作时要十分小心。

```python
>>> chinese = ['coin', 'string', 'myriad']
>>> suits = chinese
>>> suits.pop()
'myriad'
>>> chinese
['coin', 'string']
```

从上面的例子可以看出，改变`suits`的值，`chinese`中的值也会发生改变。如果想要维持原有数组中的值不变，可以在赋值给新变量的时候对数组进行复制。

```python
>>> chinese = ['coin', 'string', 'myriad']
>>> chinese_copy = list(chinese)
>>> chinese.pop()
'myriad'
>>> chinese_copy
['coin', 'string', 'myriad']
```

Because two lists may have the same contents but in fact be different lists, we require a means to test whether two objects are the same. Python includes two comparison operators, called **is** and **is not**, that test whether two expressions in fact evaluate to the identical object. Two objects are identical if they are equal in their current value, and any change to one will always be reflected in the other. **Identity is a stronger condition than equality**.

```python
>>> suits is chinese
True
>>> suits is ['coin', 'string']
False
>>> suits == ['coin', 'string']
True
```

The final two comparisons illustrate the difference between `is` and `==`. The former checks for identity, while the latter checks for the equality of contents.

### **list manipulation**

对数组进行操作时有可能会改变原有数组中的值，因此需要多加注意，下面介绍了一些常用的数组操作方法，关于这些方法的演示可以参考教材中的[在线示例](http://composingprograms.com/pages/24-mutable-data.html)。

**slice**：对数组进行切片操作时会创建一个新的数组。但是虽然数组被复制，数组中的值并没有被复制，因此如果原数组中嵌套着另一个数组的话，在切片后的数组中改变这个数组的值依然会使原数组发生改变。

**add**：Adding two lists together creates a new list that contains the values of the first list, followed by the values in the second list. Therefore, a+b and b+a can result in different values for two lists a and b. However, the += operator behaves differently for lists, and its behavior is described below along with the `extend` method.

**append**：The append method of a list takes one value as an argument and adds it to the end of the list. The argument can be any value, such as a number or another list. If the argument is a list, then that list (and not a copy) is added as an item in the list. The method always returns None, and it mutates the list by increasing its length by one.

**extend**：The extend method of a list takes an iterable value as an argument and adds each of its elements to the end of the list. It mutates the list by increasing its length by the length of the iterable argument. The statement `x += y` for a list x and iterable y is equivalent to `x.extend(y)`, aside from some obscure and minor differences beyond the scope of this text. Passing any argument to extend that is not iterable will cause a TypeError. The method does not return anything, and it mutates the list.

**pop**：The pop method removes and returns the last element of the list. When given an integer argument i, it removes and returns the element at index i of the list. This method mutates the list, reducing its length by one. Attempting to pop from an empty list causes an IndexError.

**remove**：The remove method takes one argument that must be equal to a value in the list. It removes the first item in the list that is equal to its argument. Calling remove on a value that is not equal to any item in the list causes a ValueError.

**index**：The index method takes one argument that must be equal to a value in the list. It returns the index in the list of the first item that is equal to the argument. Calling index on a value that is not equal to any item in the list causes a ValueError.

**insert**：The insert method takes two arguments: an index and a value to be inserted. The value is added to the list at the given index. All elements before the given index stay the same, but all elements after the index have their indices increased by one. This method mutates the list by increasing its size by one, then returns None.

**count**：The count method of a list takes in an item as an argument and returns how many times an equal item apears in the list. If the argument is not equal to any element of the list, then count returns 0.

**list comprehensions**：A list comprehension always creates a new list.

### tuple

A tuple, an instance of the built-in `tuple` type, is an **immutable sequence**. Tuples are created using a tuple literal that separates element expressions by commas. Parentheses are optional but used commonly in practice. Any objects can be placed within tuples.

Like lists, tuples have a finite length and support element selection. They also have a few methods that are also available for lists, such as `count` and `index`.

However, the methods for manipulating the contents of a list are not available for tuples because tuples are immutable.

While it is not possible to change which elements are in a tuple, it is possible to change the value of a mutable element like a `list` contained within a tuple.

### dictionary

Dictionaries are Python's built-in data type for storing and manipulating correspondence relationships. A dictionary contains **key-value pairs**, where both the keys and values are objects. The purpose of a dictionary is to provide an abstraction for storing and retrieving values that are indexed not by consecutive integers, but by descriptive keys.

```python
>>> numerals = {'I': 1.0, 'V': 5, 'X': 10}
```

The dictionary type also supports various methods of iterating over the contents of the dictionary as a whole. The methods `keys`, `values`, and `items` all return iterable values.

A list of key-value pairs can be converted into a dictionary by calling the `dict` constructor function.

```python
>>> dict([(3, 9), (4, 16), (5, 25)])
{3: 9, 4: 16, 5: 25}
```

Dictionaries do have some restrictions:

- A key of a dictionary cannot be or contain a mutable value.
- There can be at most one value for a given key.

A useful method implemented by dictionaries is `get`, which returns either the value for a key, if the key is present, or a default value. The arguments to `get` are the key and the default value.

```python
>>> numerals.get('A', 0)
0
>>> numerals.get('V', 0)
5
```

### local state【重要内容】

Lists and dictionaries have *local state*: they are changing values that have some particular contents at any point in the execution of a program. The word "state" implies an evolving process in which that state may change. 

Functions can also have local state.

```python
>>> def make_withdraw(balance):
        """Return a withdraw function that draws down balance with each call."""
        def withdraw(amount):
            nonlocal balance                 # Declare the name "balance" nonlocal
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount       # Re-bind the existing balance name
            return balance
        return withdraw
>>> wd = make_withdraw(100)
>>> wd(25)
75
>>> wd(25)
50
```

The `nonlocal` statement declares that whenever we change the binding of the name `balance`, the binding is changed in the first frame in which `balance` is already bound. The `nonlocal` statement indicates that the name appears somewhere in the environment other than the first (local) frame or the last (global) frame.

By introducing `nonlocal` statements, we have created a dual role for assignment statements. Either they change local bindings, or they change nonlocal bindings. In fact, assignment statements already had a dual role: they either created new bindings or re-bound existing names.

**The many roles of Python assignment can obscure the effects of executing an assignment statement. It is up to you as a programmer to document your code clearly so that the effects of assignment can be understood by others.**

Python also has an unusual restriction regarding the lookup of names: within the body of a function, all instances of a name must refer to the same frame. As a result, Python cannot look up the value of a name in a non-local frame, then bind that same name in the local frame, because the same name would be accessed in two different frames in the same function. This restriction allows Python to pre-compute which frame contains each name before executing the body of a function. When this restriction is violated, a confusing error message results. To demonstrate, the make_withdraw example is repeated below with the nonlocal statement removed.

```python
UnboundLocalError: local variable 'balance' referenced before assignment
```

This error occurs before line 5 `balance = balance - amount` is ever executed, implying that Python has considered line 5 in some way before executing line 3 `if amount > balance`. As we study interpreter design, we will see that pre-computing facts about a function body before executing it is quite common.

### the benefits of non-local assignment

Non-local assignment is an important step on our path to viewing a program as a collection of independent and autonomous objects, which interact with each other but each manage their own internal state.

**Non-local assignment**让我们意识到，程序是由一系列独立且自治的对象组合成的一个集合，这些对象可以互相交流但又同时管理着属于自己的内部领地，就像一个国家和其所属的地方政府一样。就像下面的例子一样，如果再次创建一个`wd2`，则两个取款记录`wd`和`wd2`之间互不干涉。

```python
>>> wd = make_withdraw(20)
>>> wd2 = make_withdraw(7)
>>> wd2(6)
1
>>> wd(8)
12
```

In this way, each instance of `withdraw` maintains its own balance state, but that state is inaccessible to any other function in the program.

### The Cost of Non-Local Assignment

**The key to correctly analyzing code with non-local assignment is to remember that only function calls can introduce new frames. Assignment statements always change bindings in existing frames.**

**Sameness and change.** These subtleties arise because, by introducing non-pure functions that change the non-local environment, we have changed the nature of expressions. An expression that contains only pure function calls is *referentially transparent*; its value does not change if we substitute one of its subexpression with the value of that subexpression.

Re-binding operations violate the conditions of referential transparency because they do more than return a value; they change the environment. When we introduce arbitrary re-binding, we encounter a thorny epistemological issue: **what it means for two values to be the same.** In our environment model of computation, two separately defined functions are not the same, because changes to one may not be reflected in the other.

In general, so long as we never modify data objects, we can regard a compound data object to be precisely the totality of its pieces. For example, a rational number is determined by giving its numerator and its denominator. But this view is no longer valid in the presence of change, where a compound data object has an "identity" that is something different from the pieces of which it is composed. A bank account is still "the same" bank account even if we change the balance by making a withdrawal; conversely, we could have two bank accounts that happen to have the same balance, but are different objects.

Despite the complications it introduces, non-local assignment is a powerful tool for creating modular programs. Different parts of a program, which correspond to different environment frames, can evolve **separately** throughout program execution. Moreover, using functions with local state, we are able to implement mutable data types. In fact, we can implement abstract data types that are equivalent to the built-in `list` and `dict` types introduced above.

### iterators

Python and many other programming languages provide a unified way to **process elements of a container value sequentially**, called an iterator. An *iterator* is an object that provides sequential access to values, one by one.

The iterator abstraction has two components: 

- a mechanism for **retrieving the next element in the sequence** being processed
- a mechanism for **signaling that the end of the sequence has been reached** and no further elements remain

For any container, such as a list or range, an iterator can be obtained by calling the built-in `iter` function. The contents of the iterator can be accessed by calling the built-in `next` function.

```python
>>> primes = [2, 3, 5, 7]
>>> iterator = iter(primes)
>>> type(iterator)
<class 'list_iterator'>
>>> next(iterator)
2
>>> next(iterator)
3
>>> next(iterator)
5
```

Python signals that there are no more values available by raising a `StopIteration` exception when `next`is called. This exception can be handled using a `try` statement.

```python
>>> next(iterator)
7
>>> next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

An iterator maintains local state to represent its position in a sequence. Each time `next` is called, that position advances. Two separate iterators can track two different positions in the same sequence. However, two names for the same iterator will share a position because they share the same value.

```python
>>> r = range(3, 13)
>>> s = iter(r)  # 1st iterator over r
>>> next(s)
3
>>> next(s)
4
>>> t = iter(r)  # 2nd iterator over r
>>> next(t)
3
>>> next(t)
4
>>> u = t        # Alternate name for the 2nd iterator
>>> next(u)
5
>>> next(u)
6
```

Advancing the second iterator does not affect the first. Since the last value returned from the first iterator was 4, it is positioned to return 5 next. On the other hand, the second iterator is positioned to return 7 next.

**Calling `iter` on an iterator will return that iterator**, not a copy. This behavior is included in Python so that a programmer can call `iter` on a value to get an iterator without having to worry about whether it is an iterator or a container.

```python
>>> v = iter(t)  # Another alterante name for the 2nd iterator
>>> next(v)
8
>>> next(u)
9
>>> next(t)
10
```

**The usefulness of iterators is derived from the fact that the underlying series of data for an iterator may not be represented explicitly in memory.** An iterator provides a mechanism for considering each of a series of values in turn, but all of those elements do not need to be stored simultaneously. Instead, **when the next element is requested from an iterator, that element may be computed on demand instead of being retrieved from an existing memory source.**

**因此说python是一种动态编程语言。**

### iterables

**Any value that can produce iterators is called an *iterable* value.** 

In Python, an iterable value is anything that can be passed to the built-in `iter` function. Iterables include sequence values such as **strings** and **tuples**, as well as other containers such as **sets** and **dictionaries**. Iterators are also iterables because they can be passed to the `iter` function.

Dictionaries and sets are unordered because the programmer has no control over the order of iteration, but Python does guarantee certain properties about their order in its specification.

```python
>>> d = {'one': 1, 'two': 2, 'three': 3}
>>> d
{'one': 1, 'three': 3, 'two': 2}
>>> k = iter(d)
>>> next(k)
'one'
>>> next(k)
'three'
>>> v = iter(d.values())
>>> next(v)
1
>>> next(v)
3
```

**If a dictionary changes in structure because a key is added or removed, then all iterators become invalid**, and future iterators may exhibit changes to the order of their contents. On the other hand, changing the value of an existing key does not invalidate iterators or change the order of their contents.

```python
>>> d.pop('two')
2
>>> next(k)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration
```

A `for` statement can be used to iterate over the contents of any iterable or iterator.

```python
>>> r = range(3, 6)
>>> s = iter(r)
>>> next(s)
3
>>> for x in s:
        print(x)
4
5
>>> list(s)
[]
>>> for x in r:
        print(x)
3
4
5
```

### built-in iterators

Several built-in functions take as arguments iterable values and return iterators. These functions are used extensively for **lazy sequence processing.**

**Lazy sequences** are regular **sequences** where each item is computed on demand rather than up front. 

The `map` function is lazy: calling it does not perform the computation required to compute elements of its result. Instead, an iterator object is created that can return results if queried using `next`. We can observe this fact in the following example, in which the call to `print` is delayed until the corresponding element is requested from the `doubled` iterator.

```python
>>> def double_and_print(x):
        print('***', x, '=>', 2*x, '***')
        return 2*x
>>> s = range(3, 7)
>>> doubled = map(double_and_print, s)  # double_and_print not yet called
>>> next(doubled)                       # double_and_print called once
*** 3 => 6 ***
6
>>> next(doubled)                       # double_and_print called again
*** 4 => 8 ***
8
>>> list(doubled)                       # double_and_print called twice more
*** 5 => 10 ***
*** 6 => 12 ***
[10, 12]
```

The `filter` function returns an iterator over **a subset of the values** in another iterable. The `zip` function returns an iterator over **tuples of values** that combine one value from each of multiple iterables.

- return all even values in a list by using `filter`

  ```python
  >>> list = [4, 7, 9, 1]
  >>> even_vals = filter(lambda x: x % 2 == 0, list)
  >>> list(even_vals)
  [4]
  ```

- map players names to their scores in the last two games by using `zip`

  ```python
  >>> names = ['Ja', 'Beel', 'Madison']
  >>> last_game = [1, 4, 9]
  >>> previous_game = [3, 4, 5]
  >>> scores = list(zip(names, last_game, previous_game))
  ('Ja', 1, 3), ('Beel", 4, 4), ('Madison', 9, 5)
  ```

### generators

Generators allow us to define iterations over arbitrary sequences, even infinite sequences, by leveraging the features of the Python interpreter.

**A *generator* is an iterator returned by a special class of function called a *generator function*.** Generator functions are distinguished from regular functions in that rather than containing `return` statements in their body, they use `yield` statements to return elements of a series.

Generators do not use attributes of an object to track their progress through a series. Instead, they control the execution of the generator function, which runs until the next `yield` statement is executed each time `next` is called on the generator. 

For example, the `letters_generator` function below returns a generator over the letters a, b, c, and then d.

```python
>>> def letters_generator():
        current = 'a'
        while current <= 'd':
            yield current
            current = chr(ord(current)+1)
>>> for letter in letters_generator():
        print(letter)
a
b
c
d
```

The `yield` statement indicates that we are defining a generator function, rather than a regular function. When called, a generator function doesn't return a particular yielded value, but instead a `generator`(which is a type of iterator) that itself can return the yielded values. Calling `next` on the generator continues execution of the generator function from wherever it left off previously until another `yield`statement is executed.

The first time `next` is called, the program executes statements from the body of the `letters_generator`function until it encounters the `yield` statement. Then, it pauses and returns the value of `current`. `yield`statements do not destroy the newly created environment; they preserve it for later. When `next` is called again, execution resumes where it left off. The values of `current` and of any other bound names in the scope of `letters_generator` are preserved across subsequent calls to `next`.

简单来说，**generator**并不是靠函数调而是靠调用**next**来运行的。每次调用**next**，**generator**开始执行，直到遇到**yield**语句，之后返回**yield**产生的值，函数暂停。等到下一次**next**被调用时，**generator**从上次停下来的地方继续开始运行，直到遇到下一个**yield**语句。

```python
>>> letters = letters_generator()
>>> type(letters)
<class 'generator'>
>>> next(letters)
'a'
>>> next(letters)
'b'
>>> next(letters)
'c'
>>> next(letters)
'd'
>>> next(letters)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

The generator does not start executing any of the body statements of its generator function until the first time `next` is called. The generator raises a `StopIteration` exception whenever its generator function returns.

### Implementing Lists and Dictionaries

**1. implementing lists**

We will represent a mutable linked list by a function that has a linked list as its local state. Lists need to have an identity, like any mutable value. In particular, we cannot use `None` to represent an empty mutable list, because two empty lists are not identical values (e.g., appending to one does not append to the other), but `None is None`. On the other hand, two different functions that each have `empty` as their local state will suffice to distinguish two empty lists.

If a mutable linked list is a function, what arguments does it take? The answer exhibits a general pattern in programming: **the function is a dispatch function and its arguments are first a message, followed by additional arguments to parameterize that method.** This message is a string naming what the function should do. Dispatch functions are effectively many functions in one: the message determines the behavior of the function, and the additional arguments are used in that behavior.

Our mutable list will respond to five different messages: `len`, `getitem`, `push_first`, `pop_first`, and `str`. The first two implement the behaviors of the sequence abstraction. The next two add or remove the first element of the list. The final message returns a string representation of the whole linked list.

```python
>>> def mutable_link():
        """Return a functional implementation of a mutable linked list."""
        contents = empty
        def dispatch(message, value=None):
            nonlocal contents
            if message == 'len':
                return len_link(contents)
            elif message == 'getitem':
                return getitem_link(contents, value)
            elif message == 'push_first':
                contents = link(value, contents)
            elif message == 'pop_first':
                f = first(contents)
                contents = rest(contents)
                return f
            elif message == 'str':
                return join_link(contents, ", ")
        return dispatch
```

We can also add a convenience function to construct a functionally implemented linked list from any built-in sequence, simply by adding each element in reverse order.

```python
>>> def to_mutable_link(source):
        """Return a functional list with the same contents as source."""
        s = mutable_link()
        for element in reversed(source):
            s('push_first', element)
        return s
```

At this point, we can construct a functionally implemented mutable linked lists. Note that the linked list itself is a function.

```python
>>> s = to_mutable_link(suits)
>>> type(s)
<class 'function'>
>>> print(s('str'))
heart, diamond, spade, club
```

In addition, we can pass messages to the list `s` that change its contents, for instance removing the first element.

```python
>>> s('pop_first')
'heart'
>>> print(s('str'))
diamond, spade, club
```

**massage passing**

Given some time, we could implement the many useful mutation operations of Python lists, such as `extend` and `insert`. We would have a choice: we could implement them all as functions, which use the existing messages `pop_first` and `push_first` to make all changes. Alternatively, we could add additional `elif` clauses to the body of `dispatch`, each checking for a message (e.g., `'extend'`) and applying the appropriate change to `contents` directly.

**This second approach, which encapsulates the logic for all operations on a data value within one function that responds to different messages, is a discipline called message passing.** A program that uses message passing defines dispatch functions, each of which may have local state, and organizes computation by passing "messages" as the first argument to those functions. The messages are strings that correspond to particular behaviors.

**2. implementing dictionaries**

we use a list of key-value pairs to store the contents of the dictionary. Each pair is a two-element list.

```python
>>> def dictionary():
        """Return a functional implementation of a dictionary."""
        records = []
        def getitem(key):
            matches = [r for r in records if r[0] == key]
            if len(matches) == 1:
                key, value = matches[0]
                return value
        def setitem(key, value):
            nonlocal records
            non_matches = [r for r in records if r[0] != key]
            records = non_matches + [[key, value]]
        def dispatch(message, key=None, value=None):
            if message == 'getitem':
                return getitem(key)
            elif message == 'setitem':
                setitem(key, value)
        return dispatch
```

Again, we use the **message passing** method to organize our implementation. We have supported two messages: `getitem` and `setitem`.

```python
>>> d = dictionary()
>>> d('setitem', 3, 9)
>>> d('setitem', 4, 16)
>>> d('getitem', 3)
9
>>> d('getitem', 4)
16
```

This implementation of a dictionary is *not* optimized for fast record lookup, because each call must filter through all records. The built-in dictionary type is considerably more efficient. The way in which it is implemented is beyond the scope of this text.

### dispatch dictionaries

The dispatch function is a general method for implementing a message passing interface for abstract data. To implement message dispatch, we have thus far used conditional statements to compare the message string to a fixed set of known messages.

The built-in dictionary data type provides a general method for looking up a value for a key. **Instead of using conditionals to implement dispatching, we can use dictionaries with string keys.**

The mutable `account` data type below is implemented as a dictionary. It has a constructor `account` and selector `check_balance`, as well as functions to `deposit` or `withdraw` funds. Moreover, the local state of the account is stored in the dictionary alongside the functions that implement its behavior.

```python
1	def account(initial_balance):
2	    def deposit(amount):
3	        dispatch['balance'] += amount
4	        return dispatch['balance']
5	    def withdraw(amount):
6	        if amount > dispatch['balance']:
7	            return 'Insufficient funds'
8	        dispatch['balance'] -= amount
9	        return dispatch['balance']
10	    dispatch = {'deposit':   deposit,
11	                'withdraw':  withdraw,
12	                'balance':   initial_balance}
13	    return dispatch
14	
15	def withdraw(account, amount):
16	    return account['withdraw'](amount)
17	def deposit(account, amount):
18	    return account['deposit'](amount)
19	def check_balance(account):
20	    return account['balance']
21	
22	a = account(20)
23	deposit(a, 5)
24	withdraw(a, 17)
25	check_balance(a)
```

The name `dispatch` within the body of the `account` constructor is bound to a dictionary that contains the messages accepted by an account as keys. **The *balance* is a number, while the messages *deposit* and *withdraw* are bound to functions.** These functions have access to the `dispatch` dictionary, and so they can read and change the balance. By storing the balance in the dispatch dictionary rather than in the `account` frame directly, **we avoid the need for `nonlocal` statements in `deposit` and `withdraw`.**

### propagating constraints

Mutable data allows us to simulate systems with change, but also allows us to build new kinds of abstractions. In this extended example, we combine nonlocal assignment, lists, and dictionaries to build a *constraint-based system* that supports **computation in multiple directions**. Expressing programs as constraints is a type of ***declarative programming***, in which a programmer declares the structure of a problem to be solved, but abstracts away the details of exactly how the solution to the problem is computed.

Computer programs are traditionally organized as one-directional computations, which perform operations on pre-specified arguments to produce desired outputs. On the other hand, we often want to model systems in terms of relations among quantities. For example, we previously considered the ideal gas law, which relates the pressure (`p`), volume (`v`), quantity (`n`), and temperature (`t`) of an ideal gas via Boltzmann's constant (`k`):

```
p * v = n * k * t
```

Such an equation is not one-directional. Given any four of the quantities, we can use this equation to compute the fifth. Yet translating the equation into a traditional computer language would force us to choose one of the quantities to be computed in terms of the other four. Thus, a function for computing the pressure could not be used to compute the temperature, even though the computations of both quantities arise from the same equation.

In this section, we sketch the design of a general model of linear relationships. We define primitive constraints that hold between quantities, such as an `adder(a, b, c)` constraint that enforces the mathematical relationship `a + b = c`.

We also define a means of combination, so that primitive constraints can be combined to express more complex relations. In this way, our program resembles a programming language. We combine constraints by constructing a network in which constraints are joined by connectors. A connector is an object that "holds" a value and may participate in one or more constraints.

For example, we know that the relationship between Fahrenheit and Celsius temperatures is:

```
9 * c = 5 * (f - 32)
```

This equation is a complex constraint between `c` and `f`. Such a constraint can be thought of as a network consisting of primitive `adder`, `multiplier`, and `constant` constraints.

![network for temperature calculation](http://composingprograms.com/img/constraints.png)

In this figure, we see on the left a multiplier box with three terminals, labeled `a`, `b`, and `c`. These connect the multiplier to the rest of the network as follows: The `a` terminal is linked to a connector `celsius`, which will hold the Celsius temperature. The `b` terminal is linked to a connector `w`, which is also linked to a constant box that holds 9. The `c` terminal, which the multiplier box constrains to be the product of `a` and`b`, is linked to the `c` terminal of another multiplier box, whose `b` is connected to a constant 5 and whose `a`is connected to one of the terms in the sum constraint.

Computation by such a network proceeds as follows: When a connector is given a value (by the user or by a constraint box to which it is linked), it awakens all of its associated constraints (except for the constraint that just awakened it) to inform them that it has a value. Each awakened constraint box then polls its connectors to see if there is enough information to determine a value for a connector. If so, the box sets that connector, which then awakens all of its associated constraints, and so on. 

For instance, in conversion between Celsius and Fahrenheit, `w`, `x`, and `y` are immediately set by the constant boxes to 9, 5, and 32, respectively. The connectors awaken the multipliers and the adder, which determine that there is not enough information to proceed. If the user (or some other part of the network) sets the `celsius`connector to a value (say 25), the leftmost multiplier will be awakened, and it will set `u` to `25 * 9 = 225`. Then `u` awakens the second multiplier, which sets `v` to 45, and `v` awakens the adder, which sets the `fahrenheit` connector to 77.

```python
>>> celsius = connector('Celsius')
>>> fahrenheit = connector('Fahrenheit')
>>> def converter(c, f):
        """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
        u, v, w, x, y = [connector() for _ in range(5)]
        multiplier(c, w, u)
        multiplier(v, x, u)
        adder(v, y, f)
        constant(w, 9)
        constant(x, 5)
        constant(y, 32)
>>> converter(celsius, fahrenheit)
```

We will use a **message passing system** to coordinate constraints and connectors. **Constraints are dictionaries that do not hold local states themselves.** Their responses to messages are non-pure functions that change the connectors that they constrain.

**Connectors are dictionaries that hold a current value and respond to messages that manipulate that value.** Constraints will not change the value of connectors directly, but instead will do so by sending messages, so that the connector can notify other constraints in response to the change. In this way, a connector represents a number, but also encapsulates connector behavior.

One message we can send to a connector is to set its value. Here, we (the `'user'`) set the value of `celsius` to 25.

```python
>>> celsius['set_val']('user', 25)
Celsius = 25
Fahrenheit = 77.0

>>> fahrenheit['set_val']('user', 212)
Contradiction detected: 77.0 vs 212

>>> celsius['forget']('user')
Celsius is forgotten
Fahrenheit is forgotten

>>> fahrenheit['set_val']('user', 212)
Fahrenheit = 212
Celsius = 100.0
```

This non-directionality of computation is the distinguishing feature of **constraint-based systems**.

具体实现代码和解释可以参考[官方网站](http://composingprograms.com/pages/24-mutable-data.html#local-state)。

## 2.5 object-oriented programming

### objects and classes

A class serves as a template for all objects whose type is that class. Every object is an instance of some particular class. A class definition specifies the **attributes and methods** shared among objects of that class, which are accessible via dot notation.

简单来说，class就像是建造房子的蓝图，而object则是根据这个蓝图所制造出来的一栋栋具体的房屋。

 The act of creating a new object instance is known as *instantiating* the class. 

```python
>>> a = Account('Kirk')
```

An *attribute* of an object is a name-value pair associated with the object, which is accessible via dot notation. The attributes specific to a particular object, as opposed to all objects of a class, are called ***instance attributes***. In the broader programming community, instance attributes may also be called *fields*, *properties*, or *instance variables*.

```python
>>> a.holder
'Kirk'
>>> a.balance
0
```

Functions that operate on the object or perform object-specific computations are called methods. The return values and side effects of a method can depend upon and change other attributes of the object. We say that methods are *invoked* on a particular object.

```python
>>> a.deposit(15)
15
```

### defining classes

User-defined classes are created by `class` statements. The method that initializes objects has a special name in Python, `__init__`, and is called the ***constructor*** for the class.

```python
>>> class Account:
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
```

The `__init__` method for `Account` has two formal parameters. **The first one, `self`, is bound to the newly created `Account` object.** The second parameter, `account_holder`, is bound to the argument passed to the class when it is called to be instantiated.

```python
>>> a = Account('Kirk')
>>> a.balance
0
>>> a.holder
'Kirk'
```

**identity**：Each new account instance has its own balance attribute, the value of which is independent of other objects of the same class.

```python
>>> b = Account('Spock')
>>> b.balance = 200
>>> [acc.balance for acc in (a, b)]
[0, 200]
```

To enforce this separation, every object that is an instance of a user-defined class has a unique identity. Object identity is compared using the `is` and `is not` operators.

```python
>>> a is a
True
>>> a is not b
True
```

**methods**：Object methods are also defined by a `def` statement in the suite of a `class` statement. 

```python
>>> class Account:
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            self.balance = self.balance + amount
            return self.balance
        def withdraw(self, amount):
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance
```

Each method definition again includes a special first parameter `self`, which is bound to the object on which the method is invoked. All invoked methods have access to the object via the `self` parameter, and so they can all access and manipulate the object's state.

```python
>>> spock_account = Account('Spock')
>>> spock_account.deposit(100)
100
>>> spock_account.withdraw(90)
10
>>> spock_account.withdraw(90)
'Insufficient funds'
>>> spock_account.holder
'Spock'
```

### message passing and dot expression

**Methods**, which are defined in classes, and **instance attributes**, which are typically assigned in constructors, are the fundamental elements of object-oriented programming.

**dot expression**：A dot expression consists of an expression, a dot, and a name:

```python
<expression> . <name>
```

The `<expression>` can be any valid Python expression, but the `<name>` must be a simple name (not an expression that evaluates to a name). A dot expression evaluates to the value of the attribute with the given `<name>`, for the object that is the value of the `<expression>`.

The built-in function `getattr` also returns an attribute for an object by name. It is the function equivalent of dot notation. Using `getattr`, we can look up an attribute using a string, just as we did with a dispatch dictionary.

```python
>>> getattr(spock_account, 'balance')
10
```

We can also test whether an object has a named attribute with `hasattr`.

```python
>>> hasattr(spock_account, 'deposit')
True
```

**methods and functions**：When a method is invoked on an object, that object is implicitly passed as the first argument to the method. As a result, the object is bound to the parameter `self`.

To achieve automatic `self` binding, Python distinguishes between *functions* and *bound methods*. 

- Functions are that we have been creating since the beginning of the text
- Methods couple together a function and the object on which that method will be invoked

As an attribute of a class, a method is just a function, but as an attribute of an instance, it is a bound method:

```python
>>> type(Account.deposit)
<class 'function'>
>>> type(spock_account.deposit)
<class 'method'>
```

We can call `deposit` in two ways: **as a function and as a bound method**. In the former case, we must supply an argument for the `self` parameter explicitly. In the latter case, the `self` parameter is bound automatically.

```python
>>> Account.deposit(spock_account, 1001)  # The deposit function takes 2 arguments
1011
>>> spock_account.deposit(1000)           # The deposit method takes 1 argument
2011
```

**Naming Conventions.** 

- Class names are conventionally written using the CapWords convention. 
- Method names follow the standard convention of naming functions using lowercased words separated by underscores.
- In some cases, there are instance variables and methods that are related to the maintenance and consistency of an object that we don't want users of the object to see or use. Python's convention dictates that if **an attribute name starts with an underscore**, it should only be accessed within methods of the class itself, rather than by users of the class.

### class attributes

Some attribute values are shared across all objects of a given class. Such attributes are associated with the class itself, rather than any individual instance of the class. 

For instance, let us say that a bank pays interest on the balance of accounts at a fixed interest rate. That interest rate may change, but it is a single value shared across all accounts.

```python
>>> class Account:
        interest = 0.02            # A class attribute
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        # Additional methods would be defined here
```

Class attributes are created by assignment statements in the suite of a `class` statement, outside of any method definition. This attribute can still be accessed from any instance of the class.

```python
>>> spock_account = Account('Spock')
>>> kirk_account = Account('Kirk')
>>> spock_account.interest
0.02
>>> kirk_account.interest
0.02
```

However, a single assignment statement to a class attribute changes the value of the attribute for all instances of the class.

```python
>>> Account.interest = 0.04
>>> spock_account.interest
0.04
>>> kirk_account.interest
0.04
```

**Attribute names.** We have introduced enough complexity into our object system that we have to specify how names are resolved to particular attributes. After all, we could easily have a class attribute and an instance attribute with the same name.

As we have seen, a dot expression consists of an expression, a dot, and a name:

```
<expression> . <name>
```

To evaluate a dot expression:

1. Evaluate the `<expression>` to the left of the dot, which yields the *object* of the dot expression.
2. `<name>` is matched against the **instance attributes** of that object; if an attribute with that name exists, its value is returned.
3. If `<name>` does not appear among instance attributes, then `<name>` is looked up in the class, which yields a **class attribute** value.
4. That value is returned unless it is a function, in which case a **bound method** is returned instead.

**Attribute assignment.** All assignment statements that contain a dot expression on their left-hand side affect attributes for the object of that dot expression. If the object is an instance, then assignment sets an instance attribute. If the object is a class, then assignment sets a class attribute.

If we assign to the named attribute `interest` of an account instance, we create a new instance attribute that has the same name as the existing class attribute.

```
>>> kirk_account.interest = 0.08
```

and that attribute value will be returned from a dot expression.

```python
>>> kirk_account.interest
0.08
```

However, the class attribute `interest` still retains its original value, which is returned for all other accounts.

```python
>>> spock_account.interest
0.04
```

Changes to the class attribute `interest` will affect `spock_account`, but the instance attribute for `kirk_account` will be unaffected.

```python
>>> Account.interest = 0.05  # changing the class attribute
>>> spock_account.interest     # changes instances without like-named instance attributes
0.05
>>> kirk_account.interest     # but the existing instance attribute is unaffected
0.08
```

### inheritance

When working in the object-oriented programming paradigm, we often find that different types are related. In particular, we find that similar classes differ in their amount of specialization. Two classes may have similar attributes, but one represents a special case of the other.

A subclass *inherits* the attributes of its base class, but may *override* certain attributes, including certain methods. With inheritance, we only specify what is different between the subclass and the base class. Anything that we leave unspecified in the subclass is automatically assumed to behave just as it would for the base class.

### using inheritance

For example, we may want to implement a checking account, which is different from a standard account. A checking account charges an extra $1 for each withdrawal and has a lower interest rate. Here, we demonstrate the desired behavior.

First, we give a full implementation of the `Account` class, which includes docstrings for the class and its methods.

```python
>>> class Account:
        """A bank account that has a non-negative balance."""
        interest = 0.02
        def __init__(self, account_holder):
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            """Increase the account balance by amount and return the new balance."""
            self.balance = self.balance + amount
            return self.balance
        def withdraw(self, amount):
            """Decrease the account balance by amount and return the new balance."""
            if amount > self.balance:
                return 'Insufficient funds'
            self.balance = self.balance - amount
            return self.balance
```

A full implementation of `CheckingAccount` appears below. We specify inheritance by placing an expression that evaluates to the base class in parentheses after the class name.

```python
>>> class CheckingAccount(Account):
        """A bank account that charges for withdrawals."""
        withdraw_charge = 1
        interest = 0.01
        def withdraw(self, amount):
            return Account.withdraw(self, amount + self.withdraw_charge)
```

Here, we introduce a class attribute `withdraw_charge` that is specific to the `CheckingAccount` class. We assign a lower value to the `interest` attribute. We also define a new `withdraw` method to override the behavior defined in the `Account` class. With no further statements in the class suite, all other behavior is inherited from the base class `Account`.

```python
>>> checking = CheckingAccount('Sam')
>>> checking.deposit(10)
10
>>> checking.withdraw(5)
4
>>> checking.interest
0.01
```

To look up a name in a class.

1. If it names an attribute in the class, return the attribute value.
2. Otherwise, look up the name in the base class, if there is one.

In the case of `deposit`, Python would have looked for the name first on the instance, and then in the `CheckingAccount` class. Finally, it would look in the `Account` class, where `deposit` is defined.

According to our evaluation rule for dot expressions, since `deposit` is a function looked up in the class for the `checking` instance, the dot expression evaluates to a bound method value. That method is invoked with the argument 10, which calls the deposit method with `self` bound to the `checking` object and `amount`bound to 10. Even though the `deposit` method was found in the `Account` class, `deposit` is called with `self` bound to an instance of `CheckingAccount`, not of `Account`.

**Calling ancestors.** Attributes that have been overridden are still accessible via class objects. For instance, we implemented the `withdraw` method of `CheckingAccount` by calling the `withdraw` method of `Account` with an argument that included the `withdraw_charge`.

Notice that we called `self.withdraw_charge` rather than the equivalent `CheckingAccount.withdraw_charge`. The benefit of the former over the latter is that a class that inherits from `CheckingAccount` might override the withdrawal charge.

**Interfaces.** It is extremely common in object-oriented programs that different types of objects will share the same attribute names. An *object interface* is a collection of attributes and conditions on those attributes.

For example, all accounts must have `deposit` and `withdraw` methods that take numerical arguments, as well as a `balance` attribute. The classes `Account` and `CheckingAccount` both implement this interface. Inheritance specifically promotes name sharing in this way.

The parts of your program that use objects (rather than implementing them) are most robust to future changes if they do not make assumptions about object types, but instead only about their attribute names. That is, they use the object abstraction, rather than assuming anything about its implementation.

For example, let us say that we run a lottery, and we wish to deposit $5 into each of a list of accounts. The following implementation does not assume anything about the types of those accounts, and therefore works equally well with any type of object that has a `deposit` method:

```python
>>> def deposit_all(winners, amount=5):
        for account in winners:
            account.deposit(amount)
```

The function `deposit_all` above assumes only that each `account` satisfies the account object abstraction, and so it will work with any other account classes that also implement this interface. Assuming a particular class of account would violate the abstraction barrier of the account object abstraction. For example, the following implementation will not necessarily work with new kinds of accounts:

```python
>>> def deposit_all(winners, amount=5):
        for account in winners:
            Account.deposit(account, amount)
```

### multiple interitance

Python supports the concept of a subclass inheriting attributes from multiple base classes, a language feature called *multiple inheritance*.

Suppose that we have a `SavingsAccount` that inherits from `Account`, but charges customers a small fee every time they make a deposit.

```python
>>> class SavingsAccount(Account):
        deposit_charge = 2
        def deposit(self, amount):
            return Account.deposit(self, amount - self.deposit_charge)
```

Then, a clever executive conceives of an `AsSeenOnTVAccount` account with the best features of both `CheckingAccount` and `SavingsAccount`: withdrawal fees, deposit fees, and a low interest rate. It's both a checking and a savings account in one! "If we build it," the executive reasons, "someone will sign up and pay all those fees. We'll even give them a dollar."

```python
>>> class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
        def __init__(self, account_holder):
            self.holder = account_holder
            self.balance = 1           # A free dollar!
```

In fact, this implementation is complete. Both withdrawal and deposits will generate fees, using the function definitions in `CheckingAccount` and `SavingsAccount` respectively.

```python
>>> such_a_deal = AsSeenOnTVAccount("John")
>>> such_a_deal.balance
1
>>> such_a_deal.deposit(20)            # $2 fee from SavingsAccount.deposit
19
>>> such_a_deal.withdraw(5)            # $1 fee from CheckingAccount.withdraw
13
```

What about when the reference is ambiguous, such as the reference to the `withdraw` method that is defined in both `Account` and `CheckingAccount`? The figure below depicts an *inheritance graph* for the `AsSeenOnTVAccount` class. Each arrow points from a subclass to a base class.

![inheritance graph](http://composingprograms.com/img/multiple_inheritance.png)

For a simple "diamond" shape like this, Python resolves names from left to right, then upwards. In this example, Python checks for an attribute name in the following classes, in order, until an attribute with that name is found:

```
AsSeenOnTVAccount, CheckingAccount, SavingsAccount, Account, object
```

**Further reading.** Python resolves this name using a recursive algorithm called the C3 Method Resolution Ordering. The method resolution order of any class can be queried using the `mro` method on all classes.

```python
>>> [c.__name__ for c in AsSeenOnTVAccount.mro()]
['AsSeenOnTVAccount', 'CheckingAccount', 'SavingsAccount', 'Account', 'object']
```

### the role of objects

Object-oriented programming is particularly well-suited to programs that model systems that have separate but interacting parts.

Multi-paradigm languages such as Python allow programmers to match organizational paradigms to appropriate problems. Learning to identify when to introduce a new class, as opposed to a new function, in order to simplify or modularize a program, is an important design skill in software engineering that deserves careful attention.

## 2.6 implementing classes and objects

In this section, we see that classes and objects can themselves be represented using just functions and dictionaries. The purpose of implementing an object system in this way is to illustrate that using the object metaphor does not require a special programming language. Programs can be object-oriented, even in programming languages that do not have a built-in object system.

这部分内容留作之后再深入研究。

## 2.7 object abstraction

A central concept in object abstraction is a ***generic function***, which is a function that can accept values of multiple different types. We will consider three different techniques for implementing generic functions: shared interfaces, type dispatching, and type coercion. In the process of building up these concepts, we will also discover features of the Python object system that support the creation of generic functions.

### string conversion

Python stipulates that all objects should produce two different string representations: 

- one that is human-interpretable text: `str`
- one that is a Python-interpretable expression: `repr`

The constructor function for strings,`str`, returns a human-readable string. Where possible, the `repr` function returns a Python expression that evaluates to an equal object. The docstring for *repr* explains this property:

```python
Return the canonical string representation of the object.
For most object types, eval(repr(object)) == object.
```

The result of calling `repr` on the value of an expression is what Python prints in an interactive session.

```python
>>> 12e12
12000000000000.0
>>> print(repr(12e12))
12000000000000.0
```

In cases where no representation exists that evaluates to the original value, Python typically produces a description surrounded by angled brackets.

```python
>>> repr(min)
'<built-in function min>'
```

The `str` constructor often coincides with `repr`, but provides a more interpretable text representation in some cases. For instance, we see a difference between `str` and `repr` with dates.

```python
>>> from datetime import date
>>> tues = date(2011, 9, 12)
>>> repr(tues)
'datetime.date(2011, 9, 12)'
>>> str(tues)
'2011-09-12'
```

Defining the `repr` function presents a new challenge: we would like it to apply correctly to all data types, even those that did not exist when `repr` was implemented. We would like it to be a generic or *polymorphic function*, one that can be applied to many (*poly*) different forms (*morph*) of data.

The object system provides an elegant solution in this case: the `repr` function always invokes a method called `__repr__` on its argument.

```python
>>> tues.__repr__()
'datetime.date(2011, 9, 12)'
```

By implementing this same method in user-defined classes, we can extend the applicability of `repr` to any class we create in the future.

The `str` constructor is implemented in a similar manner: it invokes a method called `__str__` on its argument.

```
>>> tues.__str__()
'2011-09-12'
```

These polymorphic functions are examples of a more general principle: **certain functions should apply to multiple data types.** Moreover, one way to create such a function is to use a shared attribute name with a different definition in each class.

### special methods

In Python, certain *special names* are invoked by the Python interpreter in special circumstances. For instance, the `__init__` method of a class is automatically invoked whenever an object is constructed. The `__str__` method is invoked automatically when printing, and `__repr__` is invoked in an interactive session to display values.

**True and false values.** We saw previously that numbers in Python have a truth value; more specifically, 0 is a false value and all other numbers are true values. In fact, all objects in Python have a truth value. By default, objects of user-defined classes are considered to be true, but the special `__bool__` method can be used to override this behavior. If an object defines the `__bool__` method, then Python calls that method to determine its truth value.

As an example, suppose we want a bank account with 0 balance to be false. We can add a `__bool__`method to the `Account` class to create this behavior.

```
>>> Account.__bool__ = lambda self: self.balance != 0
```

We can call the `bool` constructor to see the truth value of an object, and we can use any object in a boolean context.

```python
>>> bool(Account('Jack'))
False
>>> if not Account('Jack'):
        print('Jack has nothing')
Jack has nothing
```

**Sequence operations.** We have seen that we can call the `len` function to determine the length of a sequence.

```
>>> len('Go Bears!')
9
```

The `len` function invokes the `__len__` method of its argument to determine its length. All built-in sequence types implement this method.

```python
>>> 'Go Bears!'.__len__()
9
```

Python uses a sequence's length to determine its truth value, if it does not provide a `__bool__` method. Empty sequences are false, while non-empty sequences are true.

```python
>>> bool('')
False
>>> bool([])
False
>>> bool('Go Bears!')
True
```

The `__getitem__` method is invoked by the element selection operator, but it can also be invoked directly.

```python
>>> 'Go Bears!'[3]
'B'
>>> 'Go Bears!'.__getitem__(3)
'B'
```

**Callable objects.** In Python, functions are first-class objects, so they can be passed around as data and have attributes like any other object. **Python also allows us to define objects that can be "called" like functions** by including a `__call__` method. With this method, we can define a class that behaves like a higher-order function.

As an example, consider the following higher-order function, which returns a function that adds a constant value to its argument.

```python
>>> def make_adder(n):
        def adder(k):
            return n + k
        return adder
>>> add_three = make_adder(3)
>>> add_three(4)
7
```

We can create an `Adder` class that defines a `__call__` method to provide the same functionality.

```python
>>> class Adder(object):
        def __init__(self, n):
            self.n = n
        def __call__(self, k):
            return self.n + k
>>> add_three_obj = Adder(3)
>>> add_three_obj(4)
7
```

**Arithmetic.** Special methods can also define the behavior of built-in operators applied to user-defined objects. 具体可以参考python官方文档：[method names for operators](http://docs.python.org/py3k/reference/datamodel.html#special-method-names)。

### multiple representations

Abstraction barriers allow us to separate the use and representation of data. However, in large programs, it may not always make sense to speak of "the underlying representation" for a data type in a program. For one thing, there might be more than one useful representation for a data object, and we might like to design systems that can deal with multiple representations.

To take a simple example, complex numbers may be represented in two almost equivalent ways: in rectangular form (real and imaginary parts) and in polar form (magnitude and angle). Sometimes the rectangular form is more appropriate and sometimes the polar form is more appropriate. Indeed, it is perfectly plausible to imagine a system in which complex numbers are represented in both ways, and in which the functions for manipulating complex numbers work with either representation.

具体实现代码如下，值得注意的是关于**@property**修饰器的使用：The `@property` decorator allows functions to be called without call expression syntax (parentheses following an expression).

```python
>>> class Number:
        def __add__(self, other):
            return self.add(other)
        def __mul__(self, other):
            return self.mul(other)

>>> class Complex(Number):
        def add(self, other):
            return ComplexRI(self.real + other.real, self.imag + other.imag)
        def mul(self, other):
            magnitude = self.magnitude * other.magnitude
            return ComplexMA(magnitude, self.angle + other.angle)

>>> from math import atan2
>>> class ComplexRI(Complex):
        def __init__(self, real, imag):
            self.real = real
            self.imag = imag
        @property
        def magnitude(self):
            return (self.real ** 2 + self.imag ** 2) ** 0.5
        @property
        def angle(self):
            return atan2(self.imag, self.real)
        def __repr__(self):
            return 'ComplexRI({0:g}, {1:g})'.format(self.real, self.imag)

>>> from math import sin, cos, pi
>>> class ComplexMA(Complex):
        def __init__(self, magnitude, angle):
            self.magnitude = magnitude
            self.angle = angle
        @property
        def real(self):
            return self.magnitude * cos(self.angle)
        @property
        def imag(self):
            return self.magnitude * sin(self.angle)
        def __repr__(self):
            return 'ComplexMA({0:g}, {1:g} * pi)'.format(self.magnitude, self.angle/pi)
```

使用实例：

```python
>>> from math import pi
>>> ComplexRI(1, 2) + ComplexMA(2, pi/2)
ComplexRI(1, 4)
>>> ComplexRI(0, 1) * ComplexRI(0, 1)
ComplexMA(1, 1 * pi)
```

The interface approach to encoding multiple representations has appealing properties. **The class for each representation can be developed separately**; they must only agree on the names of the attributes they share, as well as any behavior conditions for those attributes. The interface is also *additive*. If another programmer wanted to add a third representation of complex numbers to the same program, they would only have to create another class with the same attributes.

### generic function

Generic functions are methods or functions that apply to arguments of different types. We have seen many examples already. The `Complex.add` method is generic, because it can take either a `ComplexRI` or `ComplexMA` as the value for `other`. This flexibility was gained by ensuring that both `ComplexRI` and `ComplexMA` share an interface. Using interfaces and message passing is only one of several methods used to implement generic functions. We will consider two others in this section: **type dispatching** and **type coercion**.

Suppose that, in addition to our complex number classes, we implement a `Rational` class to represent fractions exactly. The `add` and `mul` methods express the same computations as the `add_rational` and`mul_rational` functions from earlier in the chapter.

```python
>>> from fractions import gcd
>>> class Rational(Number):
        def __init__(self, numer, denom):
            g = gcd(numer, denom)
            self.numer = numer // g
            self.denom = denom // g
        def __repr__(self):
            return 'Rational({0}, {1})'.format(self.numer, self.denom)
        def add(self, other):
            nx, dx = self.numer, self.denom
            ny, dy = other.numer, other.denom
            return Rational(nx * dy + ny * dx, dx * dy)
        def mul(self, other):
            numer = self.numer * other.numer
            denom = self.denom * other.denom
            return Rational(numer, denom)
```

However, we cannot yet add a rational number to a complex number, although in mathematics such a combination is well-defined. We would like to introduce this cross-type operation in some carefully controlled way, so that we can support it without seriously violating our abstraction barriers. There is a tension between the outcomes we desire: we would like to be able to add a complex number to a rational number, and we would like to do so using a generic `__add__` method that does the right thing with all numeric types. At the same time, we would like to separate the concerns of complex numbers and rational numbers whenever possible, in order to maintain a modular program.

**Type dispatching.** One way to implement **cross-type operations** is to select behavior based on the types of the arguments to a function or method. The idea of type dispatching is to write functions that inspect the type of arguments they receive, then execute code that is appropriate for those types.

The built-in function `isinstance` takes an object and a class. It returns true if the object has a class that either is or inherits from the given class.

```python
>>> c = ComplexRI(1, 1)
>>> isinstance(c, ComplexRI)
True
>>> isinstance(c, Complex)
True
>>> isinstance(c, ComplexMA)
False
```

A simple example of type dispatching is an `is_real` function that uses a different implementation for each type of complex number.

```python
>>> def is_real(c):
        """Return whether c is a real number with no imaginary part."""
        if isinstance(c, ComplexRI):
            return c.imag == 0
        elif isinstance(c, ComplexMA):
            return c.angle % pi == 0
>>> is_real(ComplexRI(1, 1))
False
>>> is_real(ComplexMA(2, pi))
True
```

The role of type dispatching is to ensure that these cross-type operations are used at appropriate times. Below, we rewrite the `Number` superclass to use type dispatching for its `__add__` and `__mul__` methods.

We use the `type_tag` attribute to distinguish types of arguments. One could directly use the built-in `isinstance` method as well, but tags simplify the implementation. Using type tags also illustrates that type dispatching is not necessarily linked to the Python object system, but instead a general technique for creating generic functions over heterogeneous domains.

The `__add__` method considers two cases. First, if two arguments have the same type tag, then it assumes that `add` method of the first can take the second as an argument. Otherwise, it checks whether a dictionary of cross-type implementations, called `adders`, contains a function that can add arguments of those type tags. If there is such a function, the `cross_apply` method finds and applies it. The `__mul__`method has a similar structure.

```python
>>> class Number:
        def __add__(self, other):
            if self.type_tag == other.type_tag:
                return self.add(other)
            elif (self.type_tag, other.type_tag) in self.adders:
                return self.cross_apply(other, self.adders)
        def __mul__(self, other):
            if self.type_tag == other.type_tag:
                return self.mul(other)
            elif (self.type_tag, other.type_tag) in self.multipliers:
                return self.cross_apply(other, self.multipliers)
        def cross_apply(self, other, cross_fns):
            cross_fn = cross_fns[(self.type_tag, other.type_tag)]
            return cross_fn(self, other)
        adders = {("com", "rat"): add_complex_and_rational,
                  ("rat", "com"): add_rational_and_complex}
        multipliers = {("com", "rat"): mul_complex_and_rational,
                       ("rat", "com"): mul_rational_and_complex}
```

In this new definition of the `Number` class, all cross-type implementations are indexed by pairs of type tags in the `adders` and `multipliers` dictionaries.

This dictionary-based approach to type dispatching is extensible. New subclasses of `Number` could install themselves into the system by declaring a type tag and adding cross-type operations to `Number.adders`and `Number.multipliers`. They could also define their own `adders` and `multipliers` in a subclass.

While we have introduced some complexity to the system, we can now mix types in addition and multiplication expressions.

```python
>>> ComplexRI(1.5, 0) + Rational(3, 2)
ComplexRI(3, 0)
>>> Rational(-1, 2) * ComplexMA(4, pi/2)
ComplexMA(2, 1.5 * pi)
```

**Coercion.** In the general situation of completely unrelated operations acting on completely unrelated types, implementing explicit cross-type operations, cumbersome though it may be, is the best that one can hope for. Fortunately, we can sometimes do better by taking advantage of additional structure that may be latent in our type system. Often the different data types are not completely independent, and there may be ways by which **objects of one type may be viewed as being of another type**. This process is called *coercion*. For example, if we are asked to arithmetically combine a rational number with a complex number, we can view the rational number as a complex number whose imaginary part is zero. After doing so, we can use `Complex.add` and `Complex.mul` to combine them.

In general, we can implement this idea by **designing coercion functions that transform an object of one type into an equivalent object of another type**. Here is a typical coercion function, which transforms a rational number to a complex number with zero imaginary part:

```python
>>> def rational_to_complex(r):
        return ComplexRI(r.numer/r.denom, 0)
```

The `coerce` method returns two values with the same type tag. It inspects the type tags of its arguments, compares them to entries in the `coercions` dictionary, and converts one argument to the type of the other using `coerce_to`. Only one entry in `coercions` is necessary to complete our cross-type arithmetic system, replacing the four cross-type functions in the type-dispatching version of `Number`.

```python
>>> class Number:
        def __add__(self, other):
            x, y = self.coerce(other)
            return x.add(y)
        def __mul__(self, other):
            x, y = self.coerce(other)
            return x.mul(y)
        def coerce(self, other):
            if self.type_tag == other.type_tag:
                return self, other
            elif (self.type_tag, other.type_tag) in self.coercions:
                return (self.coerce_to(other.type_tag), other)
            elif (other.type_tag, self.type_tag) in self.coercions:
                return (self, other.coerce_to(self.type_tag))
        def coerce_to(self, other_tag):
            coercion_fn = self.coercions[(self.type_tag, other_tag)]
            return coercion_fn(self)
        coercions = {('rat', 'com'): rational_to_complex}
```

Advantages of coercion:

- Although we still need to write coercion functions to relate the types, we need to write only one function for each pair of types rather than a different function for each set of types and each generic operation. 
- Further advantages come from extending coercion. Some more sophisticated coercion schemes do not just try to coerce one type into another, but instead may try to coerce two different types each into a third common type.

Disadvantages of coercion:

- Coercion functions can lose information when they are applied. In our example, rational numbers are exact representations, but become approximations when they are converted to complex numbers.

## 2.8 efficiency

Decisions of how to represent and process data are often influenced by the efficiency of alternatives. Efficiency refers to the **computational resources used by a representation or process**, such as how much time and memory are required to compute the result of a function or represent an object. These amounts can vary widely depending on the details of an implementation.

### measuring efficiency

Measuring exactly how long a program requires to run or how much memory it consumes is challenging, because the results depend upon many details of how a computer is configured. A more reliable way to characterize the efficiency of a program is to measure how many times some event occurs, such as a function call.

Let's return to our first tree-recursive function, the `fib` function for computing numbers in the Fibonacci sequence.

```python
>>> def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return fib(n-2) + fib(n-1)
```

Consider the pattern of computation that results from evaluating `fib(6)`, depicted below. To compute `fib(5)`, we compute `fib(3)` and `fib(4)`. To compute `fib(3)`, we compute `fib(1)` and `fib(2)`. In general, the evolved process looks like a tree. Each blue dot indicates a completed computation of a Fibonacci number in the traversal of this tree.

![fib calculation tree](http://composingprograms.com/img/fib.png)

This function is instructive as a prototypical tree recursion, but it is a terribly inefficient way to compute Fibonacci numbers because it does so much redundant computation. The entire computation of `fib(3)`is duplicated.

We can measure this inefficiency. The higher-order `count` function returns an equivalent function to its argument that also maintains a `call_count` attribute. In this way, we can inspect just how many times `fib` is called.

```python
>>> def count(f):
        def counted(*args):
            counted.call_count += 1
            return f(*args)
        counted.call_count = 0
        return counted
```

**Function attributes**：Everything in Python is an object, and almost everything has attributes and methods. In python, **functions too are objects**. So they have attributes like other objects. All functions have a built-in attribute `__doc__`, which returns the doc string defined in the function source code. We can also assign new attributes to them, as well as retrieve the values of those attributes.

By counting the number of calls to `fib`, we see that the calls required grows faster than the Fibonacci numbers themselves. This rapid expansion of calls is characteristic of tree-recursive functions.

```python
>>> fib = count(fib)
>>> fib(19)
4181
>>> fib.call_count
13529
```

**Space.** To understand the space requirements of a function, we must specify generally how memory is used, preserved, and reclaimed in our environment model of computation. In evaluating an expression, the interpreter preserves all *active* environments and all values and frames referenced by those environments.

In general, the space required for tree-recursive functions will be proportional to the **maximum depth of the tree.**

The higher-order `count_frames` function tracks `open_count`, the number of calls to the function `f` that have not yet returned. The `max_count` attribute is the maximum value ever attained by `open_count`, and it corresponds to the maximum number of frames that are ever simultaneously active during the course of computation.

```python
>>> def count_frames(f):
        def counted(*args):
            counted.open_count += 1
            counted.max_count = max(counted.max_count, counted.open_count)
            result = f(*args)
            counted.open_count -= 1
            return result
        counted.open_count = 0
        counted.max_count = 0
        return counted
>>> fib = count_frames(fib)
>>> fib(19)
4181
>>> fib.open_count
0
>>> fib.max_count
19
>>> fib(24)
46368
>>> fib.max_count
24
```

To summarize, the space requirement of the `fib` function, measured in active frames, is one less than the input, which tends to be small. The time requirement measured in total recursive calls is larger than the output, which tends to be huge.

### memoization

Tree-recursive computational processes can often be made more efficient through *memoization*, a powerful technique for increasing the efficiency of recursive functions that repeat computation. A memoized function will store the return value for any arguments it has previously received. A second call to `fib(25)` would not re-compute the return value recursively, but instead return the existing one that has already been constructed.

Memoization can be expressed naturally as a higher-order function, which can also be used as a decorator. The definition below creates a *cache* of previously computed results, indexed by the arguments from which they were computed. The use of a dictionary requires that the argument to the memoized function be immutable.

```python
>>> def memo(f):
        cache = {}
        def memoized(n):
            if n not in cache:
                cache[n] = f(n)
            return cache[n]
        return memoized
```

If we apply `memo` to the recursive computation of Fibonacci numbers, a new pattern of computation evolves, depicted below.

![memoization](http://composingprograms.com/img/fib_memo.png)

In this computation of `fib(5)`, the results for `fib(2)` and `fib(3)` are reused when computing `fib(4)` on the right branch of the tree. As a result, much of the tree-recursive computation is not required at all.

Using `count`, we can see that the `fib` function is actually only called once for each unique input to `fib`.

```python
>>> counted_fib = count(fib)
>>> fib  = memo(counted_fib)
>>> fib(19)
4181
>>> counted_fib.call_count
20
>>> fib(34)
5702887
>>> counted_fib.call_count
35
```

### orders of growth

Processes can differ massively in the rates at which they consume the computational resources of space and time, as the previous examples illustrate. However, exactly determining just how much space or time will be used when calling a function is a very difficult task that depends upon many factors. A useful way to analyze a process is to categorize it along with a group of processes that all have similar requirements. A useful categorization is the *order of growth* of a process, which expresses in simple terms how the resource requirements of a process grow as a function of the input.

As an introduction to orders of growth, we will analyze the function `count_factors` below, which counts the number of integers that evenly divide an input `n`. The function attempts to divide `n` by every integer less than or equal to its square root. The implementation takes advantage of the fact that if $k$ divides $n$ and $k<\sqrt{n}$ , then there is another factor $j=n/k$ such that $j>\sqrt{n}$.

```python
1	from math import sqrt
2	def count_factors(n):
3	    sqrt_n = sqrt(n)
4	    k, factors = 1, 0
5	    while k < sqrt_n:
6	        if n % k == 0:
7	            factors += 2
8	        k += 1
9	    if k * k == n:
10	        factors += 1
11	    return factors
12	
13	result = count_factors(576)
```

How much time is required to evaluate `count_factors`? The exact answer will vary on different machines, but we can make some useful general observations about the amount of computation involved. The total number of times this process executes the body of the `while` statement is the greatest integer less than $\sqrt{n}$. The statements before and after this `while` statement are executed exactly once. So, the total number of statements executed is $w\cdot\sqrt{n}+v$, where $w$ is the number of statements in the `while` body and $v$ is the number of statements outside of the `while` statement. Although it isn't exact, this formula generally characterizes how much time will be required to evaluate `count_factors` as a function of the input `n`.

A more exact description is difficult to obtain. The constants $w$ and $v$ are not constant at all, because the assignment statements to `factors` are sometimes executed but sometimes not. An order of growth analysis allows us to gloss over such details and instead focus on the general shape of growth. In particular, the order of growth for `count_factors` expresses in precise terms that the amount of time required to compute `count_factors(n)` scales at the rate $\sqrt{n}$, within a margin of some constant factors.

**Theta Notation.** Let $n$ be a parameter that measures the size of the input to some process, and let $R(n)$ be the amount of some resource that the process requires for an input of size $n$. In our previous examples we took $n$ to be the number for which a given function is to be computed, but there are other possibilities. For instance, if our goal is to compute an approximation to the square root of a number, we might take $n$ to be the number of digits of accuracy required.

$R(n)$ might measure the amount of memory used, the number of elementary machine steps performed, and so on. In computers that do only a fixed number of steps at a time, the time required to evaluate an expression will be proportional to the number of elementary steps performed in the process of evaluation.

We say that $R(n)$ has order of growth $Θ(f(n))$, written $R(n)=Θ(f(n))$ (pronounced "theta of $f(n)$"), if there are positive constants $k1$ and $k2$ independent of $n$ such that
$$
k_1⋅f(n)≤R(n)≤k_2⋅f(n)
$$
for any value of $n$ larger than some minimum $m$. In other words, for large $n$, the value $R(n)$ is always sandwiched between two values that both scale with $f(n)$.

### example: exponentiation

简单来说，通过改进算法，可以将指数运算的时间复杂度从$Θ(n)$降低至$Θ(log \ n)$

Consider the problem of computing the exponential of a given number. We would like a function that takes as arguments a base `b` and a positive integer exponent `n` and computes $b^n$. One way to do this is via the recursive definition
$$
b^n=b⋅b^{n-1}​and​b^0=1
$$


```python
>>> def exp(b, n):
        if n == 0:
            return 1
        return b * exp(b, n-1)
```

This is a linear recursive process that requires $Θ(n)$ steps and $Θ(n)$ space.

We can compute exponentials in fewer steps by using successive squaring. For instance, rather than computing $b^8$as 
$$
b⋅(b⋅(b⋅(b⋅(b⋅(b⋅(b⋅b))))))​
$$
we can compute it using three multiplications:
$$
b^2 = b\cdot b \\
b^4 = b^2 \cdot b^2 \\
b^8 = b^4 \cdot b^4
$$
This method works fine for exponents that are powers of 2. We can also take advantage of successive squaring in computing exponentials in general if we use the recursive rule
$$
b^n = 
\begin{cases}
(b^{\frac12n})^2 & if \ n \ is \ even  \\
b \cdot b^{n-1} & if \ n \ is \  odd \\
\end{cases}
$$
We can express this method as a recursive function as well:

```python
>>> def square(x):
        return x*x
>>> def fast_exp(b, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            return square(fast_exp(b, n//2))
        else:
            return b * fast_exp(b, n-1)
```

The process evolved by `fast_exp` grows logarithmically with `n` in both space and number of steps. The size of the exponent we can compute therefore doubles (approximately) with every new multiplication we are allowed. Thus, **the number of multiplications required for an exponent of `n` grows about as fast as the logarithm of `n` base 2.** The process has $Θ(logn)$ growth. The difference between $Θ(log⁡n)$ growth and $Θ(n) $growth becomes striking as $n$ becomes large. For example, `fast_exp` for `n` of 1000 requires only 14 multiplications instead of 1000.

### growth categories

Orders of growth are designed to simplify the analysis and comparison of computational processes. Many different processes can all have equivalent orders of growth, which indicates that they scale in similar ways. It is an essential skill of a computer scientist to know and recognize common orders of growth and identify processes of the same order.

**Constants.** Constant terms do not affect the order of growth of a process. For simplicity, constants are always omitted from orders of growth.

**Logarithms.** The base of a logarithm does not affect the order of growth of a process. For instance, $log_2⁡n$ and $log_{10}⁡n$ are the same order of growth. Changing the base of a logarithm is equivalent to multiplying by a constant factor.

**Nesting.** When an inner computational process is repeated for each step in an outer process, then the order of growth of the entire process is a product of the number of steps in the outer and inner processes.

For example, the function `overlap` below computes the number of elements in list `a` that also appear in list `b`.

```python
>>> def overlap(a, b):
        count = 0
        for item in a:
            if item in b:
                count += 1
        return count
>>> overlap([1, 3, 2, 2, 5, 1], [5, 4, 2])
3
```

The `in` operator for lists requires $Θ(n)$ time, where nn is the length of the list `b`. It is applied $Θ(m)$ times, where $m$ is the length of the list `a`. The `item in b` expression is the inner process, and the `for item in a` loop is the outer process. The total order of growth for this function is $Θ(m⋅n)$.

**Lower-order terms.** As the input to a process grows, the fastest growing part of a computation dominates the total resources used. Theta notation captures this intuition. In a sum, **all but the fastest growing term can be dropped without changing the order of growth.**

For instance, consider the `one_more` function that returns how many elements of a list `a` are one more than some other element of `a`. That is, in the list `[3, 14, 15, 9]`, the element 15 is one more than 14, so `one_more` will return 1.

```
>>> def one_more(a):
        return overlap([x-1 for x in a], a)
>>> one_more([3, 14, 15, 9])
1
```

There are two parts to this computation: the list comprehension and the call to `overlap`. For a list `a` of length nn, list comprehension requires $Θ(n)$ steps, while the call to `overlap` requires $Θ(n^2)$ steps. The sum of steps is $Θ(n+n^2)$, but this is not the simplest way of expressing the order of growth. For simplicity, lower-order terms are always omitted from orders of growth, i.e. $Θ(n^2)$, and so we will never see a sum within a theta expression.

**Common categories.** Given these equivalence properties, a small set of common categories emerge to describe most computational processes. The most common are listed below from slowest to fastest growth, along with descriptions of the growth as the input increases. Examples for each category follow.

| **Category** | **Theta Notation** | **Growth Description**                  | **Example** |
| :----------- | :----------------- | :-------------------------------------- | :---------- |
| Constant     | $Θ(1)$             | Growth is independent of the input      | `abs`       |
| Logarithmic  | $Θ(log⁡n)$          | Multiplying input increments resources  | `fast_exp`  |
| Linear       | $Θ(n)$             | Incrementing input increments resources | `exp`       |
| Quadratic    | $Θ(n^2)$           | Incrementing input adds n resources     | `one_more`  |
| Exponential  | $Θ(b^n)$           | Incrementing input multiplies resources | `fib`       |

Other categories exist, such as the $Θ(\sqrt{n})$ growth of `count_factors`. However, these categories are particularly common.

Exponential growth describes many different orders of growth, because changing the base bb does affect the order of growth.

## 2.9 Recursive Objects

Objects can have other objects as attribute values. When an object of some class has an attribute value of that same class, it is a recursive object.

### linked list class

A linked list, introduced earlier in this chapter, is composed of a first element and the rest of the list. The rest of a linked list is itself a linked list — a recursive definition. The empty list is a special case of a linked list that has no first element or rest. A linked list is a sequence: it has a finite length and supports element selection by index.

We can now implement a class with the same behavior. In this version, we will define its behavior using special method names that allow our class to work with the built-in `len` function and element selection operator (square brackets or `operator.getitem`) in Python. These built-in functions invoke special method names of a class: length is computed by `__len__` and element selection is computed by `__getitem__`. The empty linked list is represented by an empty tuple, which has length 0 and no elements.

```python
>>> class Link:
        """A linked list with a first element and the rest."""
        empty = ()
        def __init__(self, first, rest=empty):
            assert rest is Link.empty or isinstance(rest, Link)
            self.first = first
            self.rest = rest
        def __getitem__(self, i):
            if i == 0:
                return self.first
            else:
                return self.rest[i-1]
        def __len__(self):
            return 1 + len(self.rest)
>>> s = Link(3, Link(4, Link(5)))
>>> len(s)
3
>>> s[1]
4
```

The definitions of `__len__` and `__getitem__` are in fact recursive. The built-in Python function `len` invokes a method called `__len__` when applied to a user-defined object argument. Likewise, the element selection operator invokes a method called `__getitem__`. Thus, bodies of these two methods will call themselves indirectly. For `__len__`, the base case is reached when `self.rest` evaluates to the empty tuple, `Link.empty`, which has a length of 0.