# HiddenPrints

![workflow](https://github.com/AdmiralLuke/HiddenPrints/actions/workflows/python-package.yml/badge.svg)

Sick of unnecessary prints from other libraries? Simply block them of with this small package

## Install

### via pip

```bash
pip install hiddenprint
```

## Usage

### 1) ``with``-Wrapper
To use the blocking mechanisms inside of methods for one or more lines of code, just wrap it in a ``with``-statement

```py
from hiddenprint import *

with HiddenPrints():
    # code where prints should not be visible in the console
    print("This won't be printed")

# code where prints should be visible in the console
print("Hello World!")
```

### 2) Function Decorator Flag

To block prints right up for a self defined function, decorator annotations can be used to block all prints within the function.

```py
from hiddenprint import *

@hide
def print_nothing_and_sum(a: int, b: int):
    print("something nobody can see")
    return a + b

result = print_nothing_and_sum(4, 3) 
print(result) # prints 7
```

## Contribution

This is only a very small package and project. If you have some ideas to improve the quality of life, feel free to make a pull request.
