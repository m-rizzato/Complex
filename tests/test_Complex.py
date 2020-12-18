from Complex import MyComplex
from math import isclose
import pytest

toll = 1e-6

a1 = MyComplex(2.0, 1.0)
b1 = MyComplex(5.0, 0.0)

a2 = MyComplex(-2.0, 0.0)
b2 = MyComplex(5.0, -6.0)

a3 = MyComplex(0.0, 1.0)
b3 = MyComplex(1.0, 0.0)

a4 = MyComplex(5.0, 1.0)
b4 = MyComplex(-5.0, -1.0)

a5 = MyComplex(2.0, 1.0)
b5 = MyComplex(2.0, 1.0)

a6 = MyComplex(10.0, -10.0)
b6 = MyComplex(15.0, -15.0)


def compare_complex(re, im, true_re, true_im):

    if not isclose(re, true_re, rel_tol=toll):
        return False

    if not isclose(im, true_im, rel_tol=toll):
        return False

    return True


@pytest.mark.parametrize(
    "c, re, im",
    [
        (a1 + b1, 7.0, 1.0),
        (a2 + b2, 3.0, -6.0),
        (a3 + b3, 1.0, 1.0),
        (a4 + b4, 0.0, 0.0),
        (a5 + b5, 4.0, 2.0),
        (a6 + b6, 25.0, -25.0),
    ],
)
def test_sum(c, re, im):
    assert compare_complex(c.re, c.im, re, im)


@pytest.mark.parametrize(
    "c, re, im",
    [
        (a1 - b1, -3.0, 1.0),
        (a2 - b2, -7.0, 6.0),
        (a3 - b3, -1.0, 1.0),
        (a4 - b4, 10.0, 2.0),
        (a5 - b5, 0.0, 0.0),
        (a6 - b6, -5.0, 5.0),
    ],
)
def test_sub(c, re, im):
    assert compare_complex(c.re, c.im, re, im)


@pytest.mark.parametrize(
    "c, re, im",
    [
        (a1 * b1, 10.0, 5.0),
        (a2 * b2, -10.0, 12.0),
        (a3 * b3, 0.0, 1.0),
        (a4 * b4, -24.0, -10.0),
        (a5 * b5, 3.0, 4.0),
        (a6 * b6, 0.0, -300.0),
    ],
)
def test_prod(c, re, im):
    assert compare_complex(c.re, c.im, re, im)


@pytest.mark.parametrize(
    "c, re, im",
    [
        (a1 / b1, 0.4, 0.2),
        (a2 / b2, -0.1639344262, -0.1967213114754098),
        (a3 / b3, 0.0, 1.0),
        (a4 / b4, -1.0, 0.0),
        (a5 / b5, 1.0, 0.0),
        (a6 / b6, 0.6666666667, 0.0),
    ],
)
def test_divid(c, re, im):
    assert compare_complex(c.re, c.im, re, im)


@pytest.mark.parametrize(
    "mod, mod_exp",
    [
        (a1.mod(), 2.236067977),
        (a2.mod(), 2.0),
        (a3.mod(), 1.0),
        (a4.mod(), 5.0990195147),
        (a5.mod(), 2.236067977),
        (a6.mod(), 14.14213562),
        (b1.mod(), 5.0),
        (b2.mod(), 7.810249676),
        (b3.mod(), 1.0),
        (b4.mod(), 5.09901951),
        (b5.mod(), 2.236067977),
        (b6.mod(), 21.21320344),
    ],
)
def test_mod(mod, mod_exp):
    assert isclose(mod, mod_exp, rel_tol=toll)
