from Complex import MyComplex

# creating two complex number
a = MyComplex(2., 1.)
b = MyComplex(5., 0.)
print('The complex number \'a\' has real and imaginary part (resp.): ', a.Re, a.Im)
print('The complex number \'b\' has real and imaginary part (resp.): ', b.Re, b.Im)

# we can determine their complex sum c = a+b via the overloaded operator '+'
c = a+b
# we print the result and verify that the resulting variable 'c' is indeed an instance of the class 'Complex'
print('\nTheir sum \'c\' has real and imaginary part (resp.): ', c.Re, c.Im)
print('The variable \'c\' has type: ', type(c))


# similarly, we can compute other basic complex operations between the complex number 'a' and 'b'
c = a-b
print('\nTheir difference has real and imaginary part (resp.): ', c.Re, c.Im)

c = a*b
print('\nTheir product has real and imaginary part (resp.): ', c.Re, c.Im)

c = a/b
print('\nTheir ratio has real and imaginary part (resp.): ', c.Re, c.Im)

print('\nTheir respective modules are: ', a.mod(), b.mod())
