# C1 Building Abstractions with Functions

## 1.1 get started

### 理解一些核心概念的关系

In the end, we will find that all of these core concepts are closely related: **functions** are **objects**, **objects** are **functions**, and **interpreters** are instances of both. However, developing a clear understanding of each of these concepts and their role in organizing code is critical to mastering the art of programming.

### 关于计算机的本质

> The fundamental equation of computers is:
>
> **computer = powerful + stupid**
>
> Computers are very powerful, looking at volumes of data very quickly. Computers can perform billions of operations per second, where each operation is pretty simple.
>
> Computers are also shockingly stupid and fragile. The operations that they can do are extremely rigid, simple, and mechanical. The computer lacks anything like real insight ... it's nothing like the HAL 9000 from the movies. If nothing else, you should not be intimidated by the computer as if it's some sort of brain. It's very mechanical underneath it all.
>
> Programming is about a person using their real insight to build something useful, constructed out of these teeny, simple little operations that the computer can do.
>
> —Francisco Cai and Nick Parlante, Stanford CS101

### 关于debug的一些建议

Learning to interpret errors and diagnose the cause of unexpected errors is called debugging. Some guiding principles of debugging are:

1. **Test incrementally:** Every well-written program is composed of small, modular components that can be tested individually. Try out everything you write as soon as possible to identify problems early and gain confidence in your components.
2. **Isolate errors:** An error in the output of a statement can typically be attributed to a particular modular component. When trying to diagnose a problem, trace the error to the smallest fragment of code you can before trying to correct it.
3. **Check your assumptions:** Interpreters do carry out your instructions to the letter — no more and no less. Their output is unexpected when the behavior of some code does not match what the programmer believes (or assumes) that behavior to be. Know your assumptions, then focus your debugging effort on verifying that your assumptions actually hold.
4. **Consult others:** You are not alone! If you don't understand an error message, ask a friend, instructor, or search engine. If you have isolated an error, but can't figure out how to correct it, ask someone else to take a look. A lot of valuable programming knowledge is shared in the process of group problem solving.

## 1.2 elements of progrmaing

### 关于编程语言本质的理解

Every powerful language has <u>**three such mechanisms**</u>:

1. **primitive expressions and statements,** which represent the simplest building blocks that the language provides, 
2. **means of combination,** by which compound elements are built from simpler ones, 
3. **means of abstraction,** by which compound elements can be named and manipulated as units.

In programming, we deal with <u>**two kinds of elements**</u>: functions and data. (Soon we will discover that they are really not so distinct.) 

Informally, **data** is stuff that we want to manipulate, and **functions** describe the rules for manipulating the data. 

Thus, any powerful programming language should be able to describe primitive data and primitive functions, as well as have some methods for combining and abstracting both functions and data.

### call expressions

The most important kind of compound expression is a call expression, which applies a function to some arguments.

```python
>>> max(7.5, 9.5)
9.5
```

### name and environment

使用`=`进行赋值之后，会把相应的`value`和`name`连在一起，为了在之后进行调用，需要将这些信息存储在内存中，即`environment`。`name`不仅可以和`value`连在一起，也可以和`function`连在一起，比如上面的`name: max`就是和`max function`连在了一起。

### pure and non-pure functions

简单来说，**pure function**指的是函数在返回特定的返回值之外，不进行其他操作。

![pure function](http://composingprograms.com/img/function_abs.png)

而**non-pure function**除了返回特定的返回值，还会产生一些副作用，可能会对计算机和解释器进行一些改变，例如`print`函数。

![non-pure function](http://composingprograms.com/img/function_print.png)

## 1.3 defining new functions

How to define a function. Function definitions consist of a def statement that indicates a  **name** and a comma-separated list of named **formal parameters**, then a return statement, called the function body, that specifies the **return expression** of the function, which is an expression to be evaluated whenever the function is applied:

```python
def <name>(<formal parameters>):
    return <return expression>
```

### Function Signature

简单来说就是函数的注释，用来解释函数的作用以及其所需要的参数的意义。

关于函数设计的一些准则，遵守这些准则会让你编写的代码拥有更好的一致性，也能帮助别人更好地理解你的代码。详细的说明可以参考官方撰写的代码风格指南PEP-8：[style guide for python code](https://www.python.org/dev/peps/pep-0008/)。

- **Function names** are lowercase, with words separated by underscores`_`. **Descriptive names** are encouraged.
- **Function names** typically **evoke operations** applied to arguments by the interpreter (e.g., print, add, square) or the name of the quantity that results (e.g., max, abs, sum).
- **Parameter names** are lowercase, with words separated by underscores. **Single-word names** are preferred.
- **Parameter names** should **evoke the role** of the parameter in the function, not just the kind of argument that is allowed.
- Single letter parameter names are acceptable when their role is obvious, but avoid "l" (lowercase ell), "O" (capital oh), or "I" (capital i) to avoid confusion with numerals.

函数的3个核心属性：参数的取值范围**domain**、返回值的取值范围**range**、输入和输出的关系**intent**。

## 1.4 designing functions

一些函数设计准则：

- Each function should have exactly **one job**. That job should be identifiable with **a short name** and characterizable in **a single line of text**. Functions that perform multiple jobs in sequence should be divided into multiple functions.
- **Don't repeat yourself** is a central tenet of software engineering. The so-called **DRY principle** states that multiple fragments of code should not describe redundant logic. Instead, that logic should be implemented once, given a name, and applied multiple times. If you find yourself copying and pasting a block of code, you have probably found an opportunity for functional abstraction.
- **Functions should be defined generally**. Squaring is not in the Python Library precisely because it is a special case of the pow function, which raises numbers to arbitrary powers.

### 函数的说明文档：docstring

通常被三个引号所包围，第一行用来描述函数的功能，剩余内容用来解释各个参数的意义。更详细的有关docstring的设计规范可以参考官方指南PEP-257：[Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)，在设计一个函数时，推荐为每个函数附上说明文档，一个函数可能只会被编写一次，但是会被阅读很多次，良好的编程习惯必不可少。

在Python中，可以随时通过调用**help()**来查看函数的说明文档，按`q`可以退出帮助界面。

## 1.5 control

目前已经遇到的3种`statement`：赋值语句`=`，函数定义语句`def`，函数返回语句`return`。每个`statement`描述了`interpreter`的状态改变，因此，**Rather than being evaluated, statements are executed**。

Functions that perform comparisons and return boolean values typically begin with is, not followed by an underscore (e.g., `isfinite`, `isdigit`, `isinstance`, etc.).

### test function

验证函数的输出是否满足预期。

- **Assertions**：一般可以使用`Assertion`语句去验证函数输出结果是否正确，例如：

  ```python
  >>> assert fib(8) == 13, 'The 8th Fibonacci number should be 13'
  ```

  When writing Python in files, rather than directly into the interpreter, tests are typically written in the same file or a neighboring file with the suffix **_test.py**.

  ```python
  >>> def fib_test():
          assert fib(2) == 1, 'The 2nd Fibonacci number should be 1'
          assert fib(3) == 1, 'The 3rd Fibonacci number should be 1'
          assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'
  ```

- **Doctest**：直接在**docstring**中编写函数测试方法。

  ```python
  >>> def sum_naturals(n):
          """Return the sum of the first n natural numbers.
  
          >>> sum_naturals(10)
          55
          >>> sum_naturals(100)
          5050
          """
          total, k = 0, 1
          while k <= n:
              total, k = total + k, k + 1
          return total
  ```

  Then, the interaction can be verified via the **doctest module**. Below, the globals function returns a representation of the global environment, which the interpreter needs in order to evaluate expressions.

  ```python
  >>> from doctest import testmod
  >>> testmod()
  TestResults(failed=0, attempted=2)
  ```

  To verify the doctest interactions for only a single function, we use a **doctest function** called `run_docstring_examples`. This function is (unfortunately) a bit complicated to call. Its first argument is the function to test. The second should always be the result of the expression `globals()`, a built-in function that returns the global environment. The third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.

  ```python
  >>> from doctest import run_docstring_examples
  >>> run_docstring_examples(sum_naturals, globals(), True)
  Finding tests in NoName
  Trying:
      sum_naturals(10)
  Expecting:
      55
  ok
  Trying:
      sum_naturals(100)
  Expecting:
      5050
  ok
  ```

  When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

  ```python
  python3 -m doctest <python_source_file>
  ```

  The key to effective testing is t**o write (and run) tests immediately after implementing new functions**. It is even good practice to write some tests before you implement, in order to have some example inputs and outputs in your mind. A test that applies a single function is called a unit test. **Exhaustive unit testing is a hallmark of good program design.**

### 1.6 high-order functions

To express certain general patterns as named concepts, we will need to construct functions that can accept other functions as arguments or return functions as values. **Functions that manipulate functions are called higher-order functions.**

使用**high-order function**最主要的目的是让代码变得简洁，但是多个函数之间的关系会变得很抽象进而难以理解，需要在实践中多加练习。

### 把函数作为参数

考虑下面两个例子：

```python
>>> def sum_naturals(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k, k + 1
        return total
```

```python
>>> def sum_cubes(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + k*k*k, k + 1
        return total
```

仔细观察这两个例子会发现，函数内部有一些相同的部分，两个函数都是在执行累加算法，只不过累加因子的计算方式不一样，如果对这两个函数进行推广，可以得到下面这种一般形式：

```python
def <name>(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
```

不同函数中存在一些**common pattern**通常意味着这些函数可以进行一般化，即设计合理的`high-order function`。

```python
def summation(n, term):
	  total, k = 0, 1
	  while k <= n:
	      total, k = total + term(k), k + 1
	  return total

def cube(x):
	  return x*x*x

def identity(x):
    return x

>>> summation(10, cube)
385
>>> summation(10, identity)
385
```

合理的使用高阶函数可以帮我们有效的降低代码的复杂程度，尤其是在运行复杂的计算时。其次，高阶函数的使用也非常符合Python语言的设计理念，即**small components can be composed into complex processes**。

### nested function definitions

在某些情况下，我们需要使用多个函数作为参数，如果讲这些函数都放在`global environment`中，一方面导致`global environment`变得比较臃肿，另一方面函数调用也会很麻烦。因此可以考虑在定义高阶函数时将这些子函数一并放在高阶函数的`local environment`中，例如下面计算平方根的函数。

```python
>>> def sqrt(a):
        def sqrt_update(x):
            return average(x, a/x)
        def sqrt_close(x):
            return approx_eq(x * x, a)
        return improve(sqrt_update, sqrt_close)
```

值得注意的是，上面的例子中`sqrt_update`函数内部可以直接使用母函数的参数`a`，这被称作**Lexical scope**。

函数作为返回值：把两个函数组合在一起构成复合函数：

```python
>>> def compose1(f, g):
        def h(x):
            return f(g(x))
        return h
```

### curring

通过使用高阶函数，我们可以把一个需要多个参数的函数转换为一系列函数且每个函数只需要一个参数，如下所示：

```python
>>> def curried_pow(x):
        def h(y):
            return pow(x, y)
        return h
>>> curried_pow(2)(3)
8
```

### lambda expression

evaluates to a function that has a single return expression as its body. 赋值语句和控制语句无法在lambda中使用，下面是一个对于lambda的简单解释：

```python
     lambda            x            :          f(g(x))
"A function that    takes x    and returns     f(g(x))"
```

关于lambda函数的起源还有一个有意思的小故事：

> It may seem perverse to use lambda to introduce a procedure/function. The notation goes back to Alonzo Church, who in the 1930's started with a "hat" symbol; he wrote the square function as "ŷ . y × y". But frustrated typographers moved the hat to the left of the parameter and changed it to a capital lambda: "Λy . y × y"; from there the capital lambda was changed to lowercase, and now we see "λy . y × y" in math books and `(lambda (y) (* y y))` in Lisp.

### function decorators

Python provides special syntax to apply higher-order functions as part of executing a `def` statement, called a decorator.

简单来说，当一个函数被添加一个`decorator`时，这个函数在被调用的时候会执行`decorator`中的代码，即可以实现在函数调用之前和调用之后对其对进行一些修饰性的操作。

```python
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
>>> @trace
    def triple(x):
        return 3 * x
>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
36
```

**trace**函数使用一个函数作为输入参数并输出该函数的类型以及参数值，其效果等同于：

```python
>>> def triple(x):
        return 3 * x
>>> triple = trace(triple)
```

In the projects associated with this text, decorators are used for tracing, as well as selecting which functions to call when a program is run from the command line.

## 1.7 Recursive functions

A function is called recursive if **the body of the function calls the function itself**, either directly or indirectly. That is, the process of executing the body of a recursive function may in turn require applying that function again.

举一个简单的例子，比如计算一个正整数各个位数数字的和：

```python
>>> def sum_digits(n):
        """Return the sum of the digits of positive integer n."""
        if n < 10:
            return n
        else:
            all_but_last, last = n // 10, n % 10
            return sum_digits(all_but_last) + last
```

使用递归，简单的函数体也可以完成复杂的计算过程。

### 迭代与递归的区别 

递归（recursion）：在函数定义中使用函数自身的方法。（A调用A）递归是一个树结构，从字面可以其理解为重复“递推”和“回归”的过程，当“递推”到达底部时就会开始“回归”，其过程相当于树的深度优先遍历。以计算的阶乘的算法为例：

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
```

迭代（iteration）：重复反馈过程的活动，每一次迭代的结果会作为下一次迭代的初始值。（A重复调用B）迭代是一个环结构，从初始状态开始，每次迭代都遍历这个环，并更新状态，多次迭代直到到达结束状态。同样以计算阶乘的算法为例：

```python
def factorial(n):
    product = 1
    for i in range(2,n):
        product *= i
    return product
```

### 递归函数的结构

- **base case**：The body begins with a base case, a conditional statement that defines the behavior of the function for the inputs that are simplest to process. Some recursive functions will have multiple base cases.
- **recursive calls***：Recursive calls always have a certain character: they simplify the original problem. Recursive functions express computation by simplifying problems incrementally. For each subsequent call, there is less work left to be done.

### tree recursion

函数内部不止一次调用自身，考虑下面的斐波那契数列计算：

```python
def fib(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  else:
    return fib(n-2) + fib(n-1)
```

