from Complex import MyComplex
from math import isclose
import pytest

toll = 1e-6

a1 = MyComplex(2., 1.)
b1 = MyComplex(5., 0.)

a2 = MyComplex(-2., 0.)
b2 = MyComplex(5., -6.)

a3 = MyComplex(0., 1.)
b3 = MyComplex(1., 0.)

a4 = MyComplex(5., 1.)
b4 = MyComplex(-5., -1.)

a5 = MyComplex(2., 1.)
b5 = MyComplex(2., 1.)

a6 = MyComplex(10., -10.)
b6 = MyComplex(15., -15.)


def compare_complex(re, im, true_re, true_im):

    if not isclose(re, true_re, rel_tol=toll):
        return False

    if not isclose(im, true_im, rel_tol=toll):
        return False

    return True


@pytest.mark.parametrize(
    "c, re, im", [
        (a1 + b1, 7., 1.),
        (a2 + b2, 3., -6.),
        (a3 + b3, 1., 1.),
        (a4 + b4, 0., 0.),
        (a5 + b5, 4., 2.),
        (a6 + b6, 25., -25.),
    ]
)
def test_sum(c, re, im):
    assert compare_complex(c.Re, c.Im, re, im)


def test_sub():
    c1 = a1-b1      
    assert compare_complex(c1.Re, c1.Im, -3., 1.)
    c2 = a2-b2
    assert compare_complex(c2.Re, c2.Im, -7., 6.)
    c3 = a3-b3
    assert compare_complex(c3.Re, c3.Im, -1., 1.)
    c4 = a4-b4
    assert compare_complex(c4.Re, c4.Im, 10., 2.)
    c5 = a5-b5
    assert compare_complex(c5.Re, c5.Im, 0., 0.)
    c6 = a6-b6
    assert compare_complex(c6.Re, c6.Im, -5., 5.)


def test_prod():
    c1 = a1*b1      
    assert compare_complex(c1.Re, c1.Im, 10., 5.)
    c2 = a2*b2
    assert compare_complex(c2.Re, c2.Im, -10., 12.)
    c3 = a3*b3
    assert compare_complex(c3.Re, c3.Im, 0., 1.)
    c4 = a4*b4
    assert compare_complex(c4.Re, c4.Im, -24., -10.)
    c5 = a5*b5
    assert compare_complex(c5.Re, c5.Im, 3., 4.)
    c6 = a6*b6
    assert compare_complex(c6.Re, c6.Im, 0., -300.)


def test_divid():
    c1 = a1/b1      
    assert compare_complex(c1.Re, c1.Im, 0.4, 0.2)
    c2 = a2/b2
    assert compare_complex(c2.Re, c2.Im, -0.1639344262, -0.1967213114754098)
    c3 = a3/b3
    assert compare_complex(c3.Re, c3.Im, 0., 1.)
    c4 = a4/b4
    assert compare_complex(c4.Re, c4.Im, -1., 0.)
    c5 = a5/b5
    assert compare_complex(c5.Re, c5.Im, 1., 0.)
    c6 = a6/b6
    assert compare_complex(c6.Re, c6.Im, 0.6666666667, 0.)


def test_mod():
    assert isclose(a1.mod(), 2.236067977, rel_tol=toll)
    assert isclose(a2.mod(), 2., rel_tol=toll)
    assert isclose(a3.mod(), 1., rel_tol=toll)
    assert isclose(a4.mod(), 5.099019514, rel_tol=toll)
    assert isclose(a5.mod(), 2.236067977, rel_tol=toll)
    assert isclose(a6.mod(), 14.14213562, rel_tol=toll)

    assert isclose(b1.mod(), 5., rel_tol=toll)
    assert isclose(b2.mod(), 7.810249676, rel_tol=toll)
    assert isclose(b3.mod(), 1., rel_tol=toll)
    assert isclose(b4.mod(), 5.09901951, rel_tol=toll)
    assert isclose(b5.mod(), 2.236067977, rel_tol=toll)
    assert isclose(b6.mod(), 21.21320344, rel_tol=toll)
