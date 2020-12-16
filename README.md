# Complex
Implementation of the complex number class along with the most important complex number oprations. Respective tests for the methods are also provided.

The library **complex.py** contains the definition of the complex number class `Complex`. The file **test_complex.py** contains the tests for the methods of the class `Complex` which can be run with [pytest](https://docs.pytest.org/en/stable/).

A single complex number is an instance of the class `Complex`. For example, ![equation](https://latex.codecogs.com/gif.latex?z%20%3D%201%20&plus;%20%5Cmathrm%7Bi%7D3) can be created as 

```
import complex as C
z = C.Complex(1.,3.)
```

where `1` and `3` are assigned to the two attributes of the class `R` and `I`, which respectively corresponds to the real and the imaginary part of the resulting number.

The class `Complex` has five methods, four of which overload the operators ![equation](https://latex.codecogs.com/gif.latex?&plus;%2C-%2C*%2C/) and the fifth one `.mod()` returns the module of the complex number.

You can find a working example of the library usage in the python script **example_complex.py**. The syntax is compatible with [Python3](https://www.python.org/downloads/).
