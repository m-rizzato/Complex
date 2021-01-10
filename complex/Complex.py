from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from copy import deepcopy
from typing import Tuple
import math as m
import numpy as np

from matplotlib import rcParams, rc

rc("text", usetex=True)
params = {
    "backend": "pdf",
    "savefig.dpi": 300,
    "axes.labelsize": 10,
    "legend.fontsize": 10,
    "xtick.labelsize": 10,
    "ytick.major.pad": 6,
    "xtick.major.pad": 6,
    "ytick.labelsize": 10,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "FreeSans",
}
rcParams.update(params)


def from_cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    radius = m.sqrt(x ** 2 + y ** 2)
    if radius > 0:
        if y > 0:
            angle = m.acos(x / radius)
        else:
            angle = -m.acos(x / radius)
    else:
        print("From cartesian to polar conversion: radius = 0, argument set to 0.")
        angle = 0.0

    return radius, angle


def cm2inch(cm):
    """Centimeters to inches"""
    return cm * 0.393701


def from_polar_to_cartesian(radius: float, angle: float) -> Tuple[float, float]:
    x = radius * m.cos(angle)
    y = radius * m.sin(angle)
    return x, y


class MyComplex(object):
    def __init__(
        self, re: float = None, im: float = None, r: float = None, theta: float = None
    ) -> None:

        is_cartesian = re is not None and im is not None
        is_polar = r is not None and theta is not None

        if is_cartesian and is_polar:
            raise ValueError("Too many arguments for object definition.")

        elif is_cartesian and not is_polar:
            self.__re = re
            self.__im = im
            self.__r, self.__theta = from_cartesian_to_polar(re, im)

        elif is_polar and not is_cartesian:
            self.__r = r
            self.__theta = theta
            self.__re, self.__im = from_polar_to_cartesian(r, theta)

        else:
            raise ValueError("Wrong arguments for object definition.")

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, value):
        self.__re = value
        self.__theta, self.__r = from_cartesian_to_polar(self.__re, self.__im)

    @property
    def im(self):
        return self.__im

    @im.setter
    def im(self, value):
        self.__im = value
        self.__theta, self.__r = from_cartesian_to_polar(self.__re, self.__im)

    @property
    def theta(self):
        return self.__theta

    @theta.setter
    def theta(self, value):
        self.__theta = value
        self.__re, self.__im = from_polar_to_cartesian(self.__r, self.__theta)

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        self.__r = value
        self.__re, self.__im = from_polar_to_cartesian(self.__r, self.__theta)

    # class members

    def __str__(self) -> str:
        return (
            f"Real part :{self.re:.2f}\nImaginary part: {self.im:.2f}\n"
            f"Magnitude: {self.r:.2f}\nPhase: {self.theta:.2f}"
        )

    def __repr__(self) -> Tuple[float, float, float, float]:
        return self.re, self.im, self.r, self.theta

    def __add__(self, no: "MyComplex") -> "MyComplex":
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
        return MyComplex(self.re + no.re, self.im + no.im)

    def __sub__(self, no: "MyComplex") -> "MyComplex":
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
        return MyComplex(self.re - no.re, self.im - no.im)

    def __mul__(self, no: "MyComplex") -> "MyComplex":
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
        return MyComplex(
            self.re * no.re - self.im * no.im,
            self.im * no.re + no.im * self.re,
        )

    def __truediv__(self, no: "MyComplex") -> "MyComplex":
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
        result_re = (self.re * no.re + self.im * no.im) / (
            no.re * no.re + no.im * no.im
        )
        result_im = (self.im * no.re - self.re * no.im) / (
            no.re * no.re + no.im * no.im
        )
        return MyComplex(result_re, result_im)

    def __copy__(self):
        cls = self.__class__
        result = cls.__new__(cls)
        result.__dict__.update(self.__dict__)
        return result

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            setattr(result, k, deepcopy(v, memo))
        return result

    def mod(self) -> float:
        """
        Computes the module |a| of the complex number
            a = real_a + i im_a ('i' being the Imaginary unit)
        as

            |a| = sqrt( real_a*real_a + im_a*im_a )
        """
        return self.r

    def visualization(self, type_width: str, ratio: float = 1.0) -> figure:

        width = inspect_input_visualization(type_width)

        angle = self.theta
        angle = angle % (m.pi * 2.0)
        if angle < 0.0:
            angle = angle + m.pi * 2.0

        ha, va, hat, vat, rlabel_angle = determine_quad(angle)

        fig = plt.figure(figsize=(cm2inch(width), cm2inch(width * ratio)))
        ax = fig.add_subplot(111, projection="polar")
        ax.set_rlabel_position(rlabel_angle)
        if self.r == 0.0:
            ax.set_ylim(0.0, 1.0)
        rlabels = ax.get_ymajorticklabels()
        for label in rlabels:
            label.set_color("red")

        ax.plot([0, angle], [0, self.r], marker="o")

        rads = np.arange(0, angle, 0.03)
        rs = np.full(rads.shape[0], self.r * 0.5)
        ax.scatter(rads, rs, c="red", s=0.2)

        option_plus = f"$z={self.re:.2f}+i {self.im:.2f}$"
        option_mins = f"$z={self.re:.2f}-i {abs(self.im):.2f}$"
        if self.im >= 0.0:
            label_ann = option_plus
        else:
            label_ann = option_mins

        ax.annotate(
            label_ann,
            xy=(angle, self.r * (1.0 + 0.05)),  # theta, radius
            color="dodgerblue",
            ha=ha,
            va=va,
            bbox=dict(
                facecolor="white",
                edgecolor="dodgerblue",
                lw=0.1,
                boxstyle="square,pad=0.1",
            ),
        )
        ax.annotate(
            f"$\Theta= {angle:.2f}$",
            xy=(angle * 0.5, self.r * 0.6),  # theta, radius
            color="red",
            ha=hat,
            va=vat,
            bbox=dict(
                facecolor="white", edgecolor="red", lw=0.1, boxstyle="square,pad=0.1"
            ),
        )

        return fig


def determine_quad(angle: float) -> Tuple[str, str, str, str, float]:
    first_q = 0 <= angle <= m.pi / 2.0
    second_q = m.pi / 2.0 < angle <= m.pi
    third_q = m.pi < angle <= 3.0 * m.pi / 2.0
    fourth_q = 3.0 * m.pi / 2.0 < angle <= m.pi * 2.0

    if first_q:
        ha = "right"
        va = "bottom"
        hat = "left"
        vat = va
        rlabel_angle = -80.0
    elif second_q:
        ha = "left"
        va = "bottom"
        hat = "right"
        vat = va
        rlabel_angle = -80.0
    elif third_q:
        ha = "left"
        va = "top"
        hat = "right"
        vat = va
        rlabel_angle = 100.0
    elif fourth_q:
        ha = "right"
        va = "top"
        hat = "right"
        vat = va
        rlabel_angle = 100.0
    else:
        raise ValueError("Wired value for number phase")

    return ha, va, hat, vat, rlabel_angle


def inspect_input_visualization(type_width: str) -> float:
    if type_width == "single":
        width = 8.8
    elif type_width == "double":
        width = 18.0
    else:
        raise ValueError(
            "Please select either 'single' or 'double' (column) for width."
        )

    return width
