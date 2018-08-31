import math
import random

import sympy as sym
import numpy as np
from scipy.optimize import brentq

r, s, x, theta_r, tau = sym.symbols("r, s, x, theta_r, tau", positive=True)

alpha, H, beta, Gamma, F, epsilon = sym.symbols(
    "alpha, H, beta, Gamma, F, epsilon", positive=True
)


def theta(r, s, theta_r=theta_r):
    """
    Return the quantity of horn gained:

    Parameters
    ----------

    s: float between 0 and 1 - the proportion of poachers acting selectively
    r: float between 0 and 1 - the proportion of horns devalued
    theta_r: float between 0 and 1 - the value of dehorned horn
    """
    return s * (1 - r) + (1 - s) * ((theta_r - 1) * r + 1)


def selective_time(r, tau):
    """
    Expected time spent in park by a selective poacher

    Parameters
    ----------

    r: float between 0 and 1 - the proportion of horns devalued
    tau: float between       - the time taken to kill a horn
    """
    return (r + tau * (1 - r)) / (1 - r)


def indiscriminate_time(r, tau, N_r):
    """
    Expected time spent in park by an indiscriminate poacher

    Parameters
    ----------

    r: float between 0 and 1       - the proportion of horns devalued
    tau: float                     - the time taken to kill a horn
    N_r: int                       - number of devalued rhinos that correspond
                                     to a single valued rhino
    """
    return tau * (1 - r ** N_r) / (1 - r)


def gain(s=s, x=x, H=H, r=r, theta_r=theta_r, alpha=alpha):
    """
    Return the total gain of the poachers based on their behaviour.
    """
    return theta(r, s, theta_r) * H * theta(r, x, theta_r) ** (-alpha)


def cost(s=s, tau=tau, x=x, r=r, F=F, beta=beta, theta_r=theta_r):

    N_r = sym.ceiling(1 / theta_r)
    return (
        F
        * (1 - r) ** beta
        * (
            s * selective_time(r=r, tau=tau)
            + (1 - s) * indiscriminate_time(r=r, tau=tau, N_r=N_r)
        )
    )


def utility(
    s=s, x=x, F=F, H=H, r=r, alpha=alpha, beta=beta, tau=tau, theta_r=theta_r,
    Gamma=Gamma
):
    """
    The total utility for a strategy
    sigma=(s, 1-s) in a population chi=(x, 1-x)
    """
    return gain(s=s, x=x, H=H, r=r, theta_r=theta_r, alpha=alpha) - cost(
        s=s, tau=tau, x=x, r=r, F=F, beta=beta, theta_r=theta_r
    ) - (1 - s) * Gamma
