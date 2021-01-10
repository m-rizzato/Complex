# Complex

## Repository presentation
This library implements the notion of complex number along with the most important complex number operations. 

The complex number class `MyComplex` is defined within the module **complex/Complex.py**, which is compatible with [Python3](https://www.python.org/downloads/).

The folder **tests** contains the tests for the methods of the class `MyComplex` and it can be run with [pytest](https://docs.pytest.org/en/stable/). Tests are compatible with Python 3.5 at least.

The script **example_complex.py** provides a working example of the library.

## How to install this library
```
git clone https://github.com/m-rizzato/Complex.git
cd Complex
python setup.py install
```

## How to use this library
A single complex number is an instance of the class `MyComplex`. It can be defined either in terms of its Cartesian components (real and imaginary parts) or by provding its polar coordinates (modulus and argument, in radiant). An example of the former is ![equation](https://latex.codecogs.com/gif.latex?z%20%3D%201%20&plus;%20%5Cmathrm%7Bi%7D3) which can be created as 
```
from Complex import MyComplex
z = MyComplex(re=1., im=3.)
```
Instead, an example of the latter is ![equation](https://latex.codecogs.com/gif.latex?z%20%3D%205%20e%5E%7Bi%20%5Cpi%7D) which is created via
```
from Complex import MyComplex
from math import pi
z = MyComplex(r=5., theta=pi)
```

The class `MyComplex` has six methods. Four of them overload the operators ![equation](https://latex.codecogs.com/gif.latex?&plus;%2C-%2C*%2C/), the fifth one `.mod` returns the module of the complex number and the sixth one `.visualization` provides a pictorial representation of the number in the complex plane. The **\*.png** files in this repository are few examples of possible outcomes. They can be generated as
```
from Complex import MyComplex
z =  MyComplex(re=1., im=3.)
filename = "number.png"
z.visualization("single").savefig(filename)
```
The non-optional argument passed to the method `.visualization` helps improving the final layout of the saved image. The desired image can then either be optimised for `single` column or `double` column. In this first version of the library, such visualisation method relies on the assumption that the argument ![equation](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cin%20%5Cleft%5B0%2C2%5Cpi%5Cright%5D). For complex numbers not satisfying the above condition, their arguments are added with multiples of the periodicity ![equation](https://latex.codecogs.com/gif.latex?2%5Cpi) in order to meet this condition.

You can find a working example of the library in the python script **example_complex.py**.
