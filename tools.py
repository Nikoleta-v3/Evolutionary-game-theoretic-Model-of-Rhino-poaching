import sympy as sym

r, s, x, theta_r, = sym.symbols("r, s, x, theta_r", positive=True)

alpha, H, R, a1, beta, gamma, F, epsilon = sym.symbols("alpha, H, R, a1, beta, "
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


def phi(r, s, R=R, a1=a1):
    """
    Returns the risk associated with poaching:

    Parameters
    ----------

    R < a1*R : constants associated with poaching
    """
    return R * s + (a1 * R * (1 - s))


def psi(r, s):
    """
    Returns the cost associated with finding a rhino
    """
    return 1 - r * s


def utility(s, x, H=H, r=r, theta_r=theta_r, R=R, a1=a1, F=F, alpha=alpha,
            beta=beta, gamma=gamma):
    """
    The total utility for a strategy 
    sigma=(s, 1-s) in a population chi=(x, 1-x)
    """
    selective_utility = theta(r, 1) * H * theta(r, x) ** (- alpha)
    selective_utility += - phi(r, 1) * (1 - r) ** (- beta)
    selective_utility += - psi(r, 1) * F * psi(r, x) ** (- gamma)

    indiscriminate_utility = theta(r, 0) * H * theta(r, x) ** (- alpha)
    indiscriminate_utility += - phi(r, 0) * (1 - r) ** (- beta)
    indiscriminate_utility += - psi(r, 0) * F * psi(r, x) ** (- gamma)

    return s * selective_utility + (1 - s) * indiscriminate_utility

