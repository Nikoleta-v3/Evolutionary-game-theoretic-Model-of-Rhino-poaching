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


def gain(s=s, x=x, H=H, r=r, theta_r=theta_r, alpha=alpha):
    """
    Return the total gain of the poachers based on their behaviour.
    """
    return theta(r, s, theta_r) * H * theta(r, x, theta_r) ** (- alpha)


def cost(s=s, x=x, r=r, F=F, beta=beta, gamma=gamma):

    return (1 / psi(r, s)) * F * psi(r, x) ** gamma * (1 - r) ** beta


def utility(s=s, x=x, H=H, r=r, theta_r=theta_r, F=F, alpha=alpha, beta=beta,
            gamma=gamma):
    """
    The total utility for a strategy 
    sigma=(s, 1-s) in a population chi=(x, 1-x)
    """
    selective_utility = gain(s=1, x=x, H=H, r=r, theta_r=theta_r, alpha=alpha)
    selective_utility += - cost(s=1, x=x, r=r, F=F, beta=beta, gamma=gamma)
    indiscriminate_utility = gain(s=0, x=x, H=H, r=r, theta_r=theta_r,
                                  alpha=alpha)
    indiscriminate_utility += - cost(s=0, x=x, r=r, F=F, beta=beta, gamma=gamma)

    return s * selective_utility + (1 - s) * indiscriminate_utility


def stable_mixed_condition():
    """
    Returns the stable condition for mixed strategies. 
    """
    numerator = -r * (-F * (-r + 1) ** beta * (-r * s + 1) ** gamma *
                      (-r * s * theta_r + r * theta_r - r + 1) ** alpha +
                      theta_r * (H * r - H)) * \
                (-r + theta_r * (-r * s + r) + 1) ** (-alpha)
    denominator = (r - 1)
    return numerator / denominator


def stable_selective_condition():
    """
    Returns the stable condition for selective strategies. 
    """
    lhs = (-r + 1) ** (-alpha) * (-F * (-r + 1) ** (alpha + beta + gamma)
                                  + H * (r * (theta_r - 1) + 1))
    rhs = (-r + 1) ** (-alpha - 1) * (-F * (-r + 1) ** (alpha + beta + gamma) +
                                      H * (r - 1) ** 2)

    return lhs <= rhs


def stable_indiscriminate_condition():
    """
    Returns the stable condition for indiscriminate strategies.  
    """
    lhs = (r * (theta_r - 1) + 1) ** (-alpha) * (F * (-r + 1) ** beta *
                                                 (r * (theta_r - 1) + 1) ** alpha
                                                 - H * (r - 1) ** 2)/(r - 1)
    rhs = (r * (theta_r - 1) + 1) ** (-alpha) * (-F * (-r + 1) ** beta *
                                                 (r*(theta_r - 1) + 1) ** alpha
                                                 + H * (r * (theta_r - 1) + 1))
    return lhs <= rhs


def s_star_v_r(r_val=0.6, gamma_num=0.95, beta_num=0.95, alpha_num=0.95,
               theta_r_num=0.2, F_num=10, H_num=100,
               stable_condition=stable_mixed_condition()):
    """
    Numerically solve the condition for mixed
    strategy stability for a given value of r.
    """
    variables = {gamma: gamma_num, beta: beta_num, alpha: alpha_num,
                 theta_r: theta_r_num, F: F_num, H: H_num, r: r_val}
    condition = stable_condition.subs(variables)
    func = lambda v: condition.subs({s: v})

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
