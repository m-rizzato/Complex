import Complex as C

#creating two complex number 
a = C.Complex( 2., 1.)
b = C.Complex( 5., 0.)
print('The complex number \'a\' has real and imaginary part (resp.): ' , a.R , a.I )
print('The complex number \'b\' has real and imaginary part (resp.): ' , b.R , b.I )
#we can determine their complex sum c = a+b via the overloaded operator '+'
c = a+b

#we print the result and verify that the resulting varialbe 'c' is indeed an instance of the class 'Complex'
print('\nTheir sum \'c\' has real and imaginary part (resp.): ' , c.R , c.I )
print('The varialbe \'c\' has type: ', type(c))


#similarly, we can compute other basic complex operations between the complex number 'a' and 'b'
c=a-b
print('\nTheir difference has real and imaginary part (resp.): ' , c.R , c.I )
c=a*b
print('\nTheir product has real and imaginary part (resp.): ' , c.R , c.I )
c=a/b
print('\nTheir ratio has real and imaginary part (resp.): ' , c.R , c.I )
print('\nTheir respective modules are: ' , a.mod() , b.mod() )


