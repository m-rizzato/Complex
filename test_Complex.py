import Complex as C
from math import isclose 

tollerance = 1e-6

a1 = C.Complex( 2., 1.)
b1 = C.Complex( 5., 0.) 	

a2 = C.Complex(-2., 0.)
b2 = C.Complex( 5.,-6.)

a3 = C.Complex( 0., 1.)
b3 = C.Complex( 1., 0.)

a4 = C.Complex( 5., 1.)
b4 = C.Complex(-5.,-1.)

a5 = C.Complex( 2., 1.)
b5 = C.Complex( 2., 1.)

a6 = C.Complex( 10.,-10.)
b6 = C.Complex( 15.,-15.)

def compare_complex(re,im,true_re,true_im):

    if not isclose(re, true_re, rel_tol=tollerance):
        return False

    if not isclose(im, true_im, rel_tol=tollerance):
        return False

    return True

def test_sum( ):
    c1 = a1+b1
    assert compare_complex(c1.R,c1.I, 7., 1.)
    c2 = a2+b2	
    assert compare_complex(c2.R,c2.I, 3., -6.)
    c3 = a3+b3
    assert compare_complex(c3.R,c3.I, 1., 1.)
    c4 = a4+b4
    assert compare_complex(c4.R,c4.I, 0., 0.)
    c5 = a5+b5
    assert compare_complex(c5.R,c5.I, 4., 2.)
    c6 = a6+b6
    assert compare_complex(c6.R,c6.I, 25., -25.)

def test_sub( ):
    c1 = a1-b1      
    assert compare_complex(c1.R,c1.I,-3.,1.)
    c2 = a2-b2
    assert compare_complex(c2.R,c2.I, -7., 6.)
    c3 = a3-b3
    assert compare_complex(c3.R,c3.I, -1., 1.)
    c4 = a4-b4
    assert compare_complex(c4.R,c4.I, 10., 2.)
    c5 = a5-b5
    assert compare_complex(c5.R,c5.I, 0., 0.)
    c6 = a6-b6
    assert compare_complex(c6.R,c6.I, -5., 5.)

def test_prod( ):
    c1 = a1*b1      
    assert compare_complex(c1.R,c1.I, 10., 5.)
    c2 = a2*b2
    assert compare_complex(c2.R,c2.I, -10., 12.)
    c3 = a3*b3
    assert compare_complex(c3.R,c3.I, 0., 1.)
    c4 = a4*b4
    assert compare_complex(c4.R,c4.I, -24., -10.)
    c5 = a5*b5
    assert compare_complex(c5.R,c5.I, 3., 4.)
    c6 = a6*b6
    assert compare_complex(c6.R,c6.I, 0., -300.)

def test_divid( ):
    c1 = a1/b1      
    assert compare_complex(c1.R,c1.I, 0.4, 0.2)
    c2 = a2/b2
    assert compare_complex(c2.R,c2.I, -0.1639344262, -0.1967213114754098 )
    c3 = a3/b3
    assert compare_complex(c3.R,c3.I, 0., 1.)
    c4 = a4/b4
    assert compare_complex(c4.R,c4.I, -1., 0.)
    c5 = a5/b5
    assert compare_complex(c5.R,c5.I, 1., 0.)
    c6 = a6/b6
    assert compare_complex(c6.R,c6.I, 0.6666666667, 0.)

def test_mod( ):
    assert isclose(a1.mod(), 2.236067977, rel_tol=tollerance) 
    assert isclose(a2.mod(), 2., rel_tol=tollerance)
    assert isclose(a3.mod(), 1., rel_tol=tollerance)
    assert isclose(a4.mod(), 5.099019514, rel_tol=tollerance)
    assert isclose(a5.mod(), 2.236067977, rel_tol=tollerance)
    assert isclose(a6.mod(), 14.14213562, rel_tol=tollerance)

    assert isclose(b1.mod(), 5., rel_tol=tollerance)
    assert isclose(b2.mod(), 7.810249676, rel_tol=tollerance)
    assert isclose(b3.mod(), 1., rel_tol=tollerance)
    assert isclose(b4.mod(), 5.09901951, rel_tol=tollerance)
    assert isclose(b5.mod(), 2.236067977, rel_tol=tollerance)
    assert isclose(b6.mod(), 21.21320344, rel_tol=tollerance)
