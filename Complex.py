import math 

class Complex(object):
    def __init__(self, real, imaginary):
        self.R = real
        self.I = imaginary
        
    def __add__(self, no):
        '''
        Overloads the operator + to perform the sum of two complex numbers.
         
        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b
           
        the result of this operation will be the complex number c obtained as  
            c = real_c + i im_c
            
        where 
            real_c = real_a + real_b
            im_c   = im_a + im_b
        '''
        return Complex(self.R+no.R,self.I+no.I)
        
    def __sub__(self, no):
        '''
        Overloads the operator - to compute the difference between two complex numbers.
         
        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b
           
        the result of this operation will be the complex number c obtained as  
            c = real_c + i im_c
            
        where 
            real_c = real_a - real_b
            im_c   = im_a - im_b
        '''
        return Complex(self.R-no.R,self.I-no.I)
        
    def __mul__(self, no):
        '''
        Overloads the operator * to perform the multiplication between two complex numbers.
         
        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b
           
        the result of this operation will be the complex number c obtained as  
            c = real_c + i im_c
            
        where 
            real_c = real_a*real_b - im_a*im_b
            im_c   = im_a*real_b + im_b*real_a
        '''
        return Complex(self.R*no.R-self.I*no.I , self.I*no.R + no.I*self.R)

    def __truediv__(self, no):
        '''
        Overloads the operator / to perform the division between two complex numbers.
         
        Given two complex numbers ('i' being the Imaginary unit)
            a = real_a + i im_a
            b = real_b + i im_b
           
        the result of this operation will be the complex number c obtained as  
            c = real_c + i im_c
            
        where 
            real_c = (real_a*real_b + im_a*im_b) / (real_a*real_a + im_a*im_a)
            im_c   = (im_a*real_b - real_a*im_b) / (real_a*real_a + im_a*im_a)
        '''
        resultRe = (self.R*no.R+self.I*no.I) / (no.R*no.R + no.I*no.I)
        resultIm = (self.I*no.R-self.R*no.I) / (no.R*no.R + no.I*no.I)
        return Complex(resultRe,resultIm)
        
    def mod(self):
        '''
        Computes the module |a| of the complex number 
            a = real_a + i im_a ('i' being the Imaginary unit) 
        as
        
            |a| = sqrt( real_a*real_a + im_a*im_a )
        '''
        return math.sqrt(self.R*self.R + self.I*self.I)
