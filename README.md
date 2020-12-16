# Complex
Implementation of the complex number class containing the most important methods for complex number oprations. Respective tests for the methods are also provided.

The library **complex.py** contains the definition for the complex number class `Complex`. The file **test_complex.py** contains the tests for the methods of the class `Complex` which can be run with [pytest] (https://docs.pytest.org/en/stable/).

A single complex number is an instance of the class `Complex`. For example, <img src="https://latex.codecogs.com/gif.latex?z=1.+\text{i}3." /> can be created as 

```
import complex as C
z = C.Complex(1.,3.)
```

where `1.` and `3.` are assigned to the two attributes of the class `R` and `I` which respectively corresponds to the real and the imaginary part of the resulting number.

The class `Complex` has 5 methods, four of which overload the operators <img src="https://latex.codecogs.com/gif.latex?+,-,*,\/" /> and the fifth one `.mod()` allows returns the module of the complex number.

You can find a functioning example of the library in the python script **example_complex.py**.
