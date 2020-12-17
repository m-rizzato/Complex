import math

# test change

class MyComplex(object):

    def __init__(self, real, imaginary):
        self.Re = real
        self.Im = imaginary
        
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
        return MyComplex(self.Re+no.Re, self.Im+no.Im)
        
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
        return MyComplex(self.Re-no.Re, self.Im-no.Im)
        
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
        return MyComplex(self.Re*no.Re-self.Im*no.Im, self.Im*no.Re + no.Im*self.Re)

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
        result_re = (self.Re*no.Re+self.Im*no.Im) / (no.Re*no.Re + no.Im*no.Im)
        result_im = (self.Im*no.Re-self.Re*no.Im) / (no.Re*no.Re + no.Im*no.Im)
        return MyComplex(result_re, result_im)
        
    def mod(self):
        """
        Computes the module |a| of the complex number
            a = real_a + i im_a ('i' being the Imaginary unit)
        as

            |a| = sqrt( real_a*real_a + im_a*im_a )
        """
        return math.sqrt(self.Re*self.Re + self.Im*self.Im)
    
