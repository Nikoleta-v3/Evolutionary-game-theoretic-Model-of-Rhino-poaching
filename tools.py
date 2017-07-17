import sympy as sym
import numpy as np
from scipy.optimize import brentq

r, s, x, theta_r, = sym.symbols("r, s, x, theta_r", positive=True)

alpha, H, beta, gamma, F, epsilon = sym.symbols("alpha, H, beta, "
                                                "gamma, F, epsilon",
                                                positive=True)


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


def psi(r, s):
    """
    Returns the cost associated with finding a rhino
    """
    return 1 - r * s


def utility(s, x, H=H, r=r, theta_r=theta_r, F=F, alpha=alpha, beta=beta,
            gamma=gamma):
    """
    The total utility for a strategy 
    sigma=(s, 1-s) in a population chi=(x, 1-x)
    """
    selective_utility = theta(r, 1) * H * theta(r, x) ** (- alpha)
    selective_utility += - psi(r, 1) * F * psi(r, x) ** (- gamma) * (1 - r) ** (- beta)
    indiscriminate_utility = theta(r, 0) * H * theta(r, x) ** (- alpha)
    indiscriminate_utility += - psi(r, 0) * F * psi(r, x) ** (- gamma) * (1 - r) ** (- beta)

    return s * selective_utility + (1 - s) * indiscriminate_utility


def stable_mixed_condition():
    fraction_cost = F * r * (-r + 1) ** (- beta) * (-r * s + 1) ** (- gamma)
    fraction_gain = H * r * theta_r * (- r * s * theta_r + r * theta_r - r +
                                       1) ** (- alpha)
    return fraction_cost - fraction_gain


def s_star_v_r(r_val=0.6, gamma_num=0.95, beta_num=0.95, alpha_num=0.95,
               theta_r_num=0.2, F_num=10, H_num=100, stable_mixed_condition=stable_mixed_condition()):
    """
    Numerically solve the condition for mixed 
    strategy stability for a given value of r.
    """
    variables = {gamma: gamma_num, beta: beta_num, alpha: alpha_num,
                 theta_r: theta_r_num, F: F_num, H: H_num, r: r_val}
    condition = stable_mixed_condition.subs(variables)
    func = lambda x : condition.subs({s: x})

    try:
        return brentq(func, a=0, b=1)
    except ValueError:
        return np.nan


def evolutionary_stability(s, r_val=0.6, gamma_num=0.25, beta_num=0.25,
                           alpha_num=0.25, theta_r_num=0.2, F_num=10, H_num=100,
                           tol=0.000001, step=0.0000001,
                           starting_epsilon=0.00001):

    variables = {gamma: gamma_num, beta: beta_num, alpha: alpha_num,
                 theta_r: theta_r_num, F: F_num, H: H_num, r: r_val}

    epsilon = starting_epsilon

    evol_stable = []
    while epsilon > tol:
        up_s, down_s = min(s + epsilon, 1), max(s - epsilon, 0)
        delta_plus = (utility(s, up_s) - utility(up_s, up_s)).subs(variables)
        delta_minus = (utility(s, down_s) - utility(down_s, down_s)).subs(
                                                                      variables)

        evol_stable.append((delta_plus > tol) and (delta_minus > tol))
        epsilon -= step

    return evol_stable, evol_stable[-1]
