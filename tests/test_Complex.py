from complex.Complex import MyComplex
import math as m
import pytest
from typing import Tuple


def from_cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    radius = m.sqrt(x ** 2 + y ** 2)
    if radius > 0:
        if y > 0:
            angle = m.acos(x / radius)
        else:
            angle = -m.acos(x / radius)
    else:
        angle = 0.0

    return radius, angle


toll = 1e-6

# cartesian initialisation
a1 = MyComplex(re=2.0, im=1.0)
b1 = MyComplex(re=5.0, im=0.0)

a2 = MyComplex(re=-2.0, im=0.0)
b2 = MyComplex(re=5.0, im=-6.0)

a3 = MyComplex(re=0.0, im=1.0)
b3 = MyComplex(re=1.0, im=0.0)

# polar initialisation
a4 = MyComplex(r=5.0, theta=0.20)
b4 = MyComplex(r=5.0, theta=0.20 + m.pi)

a5 = MyComplex(r=2.23, theta=0.46)
b5 = MyComplex(r=2.23, theta=0.46)

a6 = MyComplex(r=14.0, theta=-m.pi / 4.0)
b6 = MyComplex(r=21.0, theta=-m.pi / 4.0)


def isclose(a: float, b: float, rel_tol: float) -> bool:
    if a == 0 or b == 0:
        return abs(a - b) < rel_tol
    else:
        return abs(a - b) / b < rel_tol


def compare_complex(re: float, im: float, true_re: float, true_im: float) -> bool:

    if not isclose(re, true_re, toll):
        return False

    if not isclose(im, true_im, toll):
        return False

    return True


@pytest.mark.parametrize(
    "c, re, im",
    [
        (a1 + b1, 7.0, 1.0),
        (a2 + b2, 3.0, -6.0),
        (a3 + b3, 1.0, 1.0),
        (a4 + b4, 0.0, 0.0),
        (a5 + b5, 3.9963941, 1.9800085),
        (a6 + b6, 24.74873734, -24.74873734),
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
        (a4 - b4, 9.800666, 1.986693),
        (a5 - b5, 0.0, 0.0),
        (a6 - b6, -4.9497474, 4.9497474),
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
        (a4 * b4, -23.0265, -9.73546),
        (a5 * b5, 3.0126830, 3.9564472),
        (a6 * b6, 0.0, -294.0),
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
        (a4.mod(), 5.0),
        (a5.mod(), 2.23),
        (a6.mod(), 14.0),
        (b1.mod(), 5.0),
        (b2.mod(), 7.810249676),
        (b3.mod(), 1.0),
        (b4.mod(), 5.0),
        (b5.mod(), 2.23),
        (b6.mod(), 21.0),
    ],
)
def test_mod(mod, mod_exp):
    assert isclose(mod, mod_exp, toll)
