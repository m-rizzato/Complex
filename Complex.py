import math 

class Complex(object):
    def __init__(self, real, imaginary):
        self.R = real
        self.I = imaginary
        
    def __add__(self, no):
        return Complex(self.R+no.R,self.I+no.I)
        
    def __sub__(self, no):
        return Complex(self.R-no.R,self.I-no.I)
        
    def __mul__(self, no):
        return Complex(self.R*no.R-self.I*no.I , self.I*no.R + no.I*self.R)

    def __truediv__(self, no):
        resultRe = (self.R*no.R+self.I*no.I) / (no.R*no.R + no.I*no.I)
        resultIm = (self.I*no.R-self.R*no.I) / (no.R*no.R + no.I*no.I)
        return Complex(resultRe,resultIm)
        
    def mod(self):
        return math.sqrt(self.R*self.R + self.I*self.I)
