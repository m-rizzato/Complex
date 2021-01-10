# Complex

## Repository presentation
Library implementing the notion of complex number along with the most important complex number operations. 

The complex number class `MyComplex` is defined within the module **complex.py**, which is compatible with [Python3](https://www.python.org/downloads/).

The file **test_complex.py** contains the tests for the methods of the class `MyComplex` and it can be run with [pytest](https://docs.pytest.org/en/stable/). Tests are compatible with Python 3.5 at least.

The script **example_complex.py** provides a working example of the library.

## How to install this class
```
git clone https://github.com/m-rizzato/Complex.git
cd Complex
python setup.py install
```

## How to use this class
A single complex number is an instance of the class `MyComplex`. It can be defined either in terms of its Cartesian components (real and imaginary part) or by provding its polar coordinate (modulus and argument, in radiant). An example of the former is ![equation](https://latex.codecogs.com/gif.latex?z%20%3D%201%20&plus;%20%5Cmathrm%7Bi%7D3) which can be created as 
```
from Complex import MyComplex
z = MyComplex(re=1., im=3.)
```
Instead, an example of the latter is ![equation](https://latex.codecogs.com/gif.latex?z%20%3D%205%20e%5E%7Bi%20%5Cpi%7D) which is created via
```
from Complex import MyComplex
z = MyComplex(r=5., theta=3.14)
```

The class `MyComplex` has six methods. Four of them overload the operators ![equation](https://latex.codecogs.com/gif.latex?&plus;%2C-%2C*%2C/), the fifth one `.mod()` returns the module of the complex number and the sixth provides an pictorial representation of the number in the complex plane. The **\*.png** files in this repository can be created as
```
from Complex import MyComplex
z =  MyComplex(re=1., im=3.)
filename = "number.png"
z.visualization("single").savefig(filename)
```
The non-optional argument passed to the method `visualization` helps optimising the final layout of the saved image, depending if it is meant to appear within a `single` column or in `double` column of a standard a4 page. In this first version of the library, the visualisation method relies on the assumption that the argument ![equation](https://latex.codecogs.com/gif.latex?%5Ctheta%20%5Cin%20%5Cleft%5B0%2C2%5Cpi%5Cright%5D). In different situation, the argument is added with multiples of the periodicity ![equation](https://latex.codecogs.com/gif.latex?2%5Cpi) to meet this condition.

You can find a working example of the library in the python script **example_complex.py**.
