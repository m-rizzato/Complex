import math
#test

class MyComplex(object):

    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary

    def __add__(self, no):
        """
        Overloads the operator + to perform the sum of two complex numbers.

        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b

        the result of this operation will be the complex number c obtained as
            c = real_c + i im_c

        where
            real_c = real_a + real_b
            im_c   = im_a + im_b
        """
        return MyComplex(self.re+no.re, self.im+no.im)
        
    def __sub__(self, no):
        """
        Overloads the operator - to compute the difference between two complex numbers.

        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b

        the result of this operation will be the complex number c obtained as
            c = real_c + i im_c

        where
            real_c = real_a - real_b
            im_c   = im_a - im_b
        """
        return MyComplex(self.re-no.re, self.im-no.im)
        
    def __mul__(self, no):
        """
        Overloads the operator * to perform the multiplication between two complex numbers.

        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b

        the result of this operation will be the complex number c obtained as
            c = real_c + i im_c

        where
            real_c = real_a*real_b - im_a*im_b
            im_c   = im_a*real_b + im_b*real_a
        """
        return MyComplex(self.re*no.re-self.im*no.im, self.im*no.re + no.im*self.re)

    def __truediv__(self, no):
        """
        Overloads the operator / to perform the division between two complex numbers.

        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b

        the result of this operation will be the complex number c obtained as
            c = real_c + i im_c

        where
            real_c = (real_a*real_b + im_a*im_b) / (real_a*real_a + im_a*im_a)
            im_c   = (im_a*real_b - real_a*im_b) / (real_a*real_a + im_a*im_a)
        """
        result_re = (self.re*no.re+self.im*no.im) / (no.re*no.re + no.im*no.im)
        result_im = (self.im*no.re-self.re*no.im) / (no.re*no.re + no.im*no.im)
        return MyComplex(result_re, result_im)
        
    def mod(self):
        """
        Computes the module |a| of the complex number
            a = real_a + i im_a ('i' being the Imaginary unit)
        as

            |a| = sqrt( real_a*real_a + im_a*im_a )
        """
        return math.sqrt(self.re*self.re + self.im*self.im)
