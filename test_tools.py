import unittest
import tools

import sympy as sym


class TestCostFunctions(unittest.TestCase):
    r, s, x, theta_r= sym.symbols("r, s, x, theta_r", positive=True)

    def test_theta(self):
        self.assertEqual(tools.theta(self.r, self.s, self.theta_r) - (self.s *
                         (1 - self.r) + (1 - self.s) * ((self.theta_r - 1) *
                                                        self.r + 1)), 0)

    def test_psi(self):
        self.assertEqual(tools.psi(r=self.r, s=self.s), 1 - self.r * self.s)


class TestUtility(unittest.TestCase):
    r, s, x, theta_r, alpha, H, beta, gamma, F = sym.symbols("""r, s, x, 
                                                                theta_r, alpha,
                                                                H, beta, gamma,
                                                                F""", positive=True)

    def test_utility(self):
        selective_gain = (1 - self.r) * self.H * (self.x * (1 - self.r) +
                         (1 - self.x) * ((self.theta_r - 1) * self.r + 1)) \
                                                                ** (-self.alpha)

        selective_cost = (1 - self.r) * self.F * (1 - self.r * self.x) ** (- self.gamma) \
                                                 * (1 - self.r) ** (- self.beta)

        indiscriminate_gain = ((self.theta_r - 1) * self.r + 1) * self.H / \
                              ((self.x * (1 - self.r) + (1 - self.x) *
                                ((self.theta_r - 1) * self.r + 1))) ** self.alpha

        indiscriminate_cost = self.F * (1 - self.r * self.x) ** (- self.gamma) \
                                                 * (1 - self.r) ** (- self.beta)

        u = self.s * (selective_gain - selective_cost) + \
            (1 - self.s) * (indiscriminate_gain - indiscriminate_cost)

        difference = (tools.utility(s=self.s, x=self.x) - u).simplify()
        self.assertEqual(difference, 0)


class TestStabilityFunctions(unittest.TestCase):
    s = sym.symbols("s", positive=True)

    def test_stable_mixed_condition(self):
        condition = tools.utility(1, self.s) - tools.utility(0, self.s)
        self.assertEqual(tools.stable_mixed_condition(), condition.simplify())

    def test_s_star_v_r(self):
        # test default values
        self.assertEqual(tools.s_star_v_r(), 0.8197348311021695)
