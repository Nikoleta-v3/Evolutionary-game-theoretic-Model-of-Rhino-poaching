import unittest
import tools

import sympy as sym


class TestCostFunctions(unittest.TestCase):
    r, s, x, theta_r, R, a1 = sym.symbols("""r, s, x, theta_r, R, a1""",
                                                                  positive=True)

    def test_theta(self):
        self.assertEqual(tools.theta(self.r, self.s, self.theta_r) - (self.s *
                         (1 - self.r) + (1 - self.s) * ((self.theta_r - 1) *
                                                        self.r + 1)), 0)

    def test_phi(self):
        self.assertEqual(tools.phi(r=self.r, s=self.s, R=self.R, a1=self.a1),
                         self.R * self.s + self.a1 * self.R * (1 - self.s))

    def test_psi(self):
        self.assertEqual(tools.psi(r=self.r, s=self.s), 1 - self.r * self.s)


class TestUtility(unittest.TestCase):
    r, s, x, theta_r, alpha, H, R, a1, beta, gamma, F = sym.symbols("""r, s, x,
                                                                    theta_r, alpha,
                                                                    H, R, a1, beta, 
                                                                    gamma, F""",
                                                                    positive=True)

    def test_utility(self):
        selective_gain = (1 - self.r) * self.H * (self.x * (1 - self.r) +
                         (1 - self.x) * ((self.theta_r - 1) * self.r + 1)) \
                                                                ** (-self.alpha)

        selective_cost = self.R * (1 - self.r) ** (-self.beta) + (1 - self.r) \
                                * self.F * (1 - self.r * self.x) ** (- self.gamma)

        indiscriminate_gain = ((self.theta_r - 1) * self.r + 1) * self.H / \
                              ((self.x * (1 - self.r) + (1 - self.x) *
                                ((self.theta_r - 1) * self.r + 1))) ** self.alpha

        indiscriminate_cost = self.a1 * self.R * (1 - self.r) ** (-self.beta) \
                              + self.F / (1 - self.r * self.x) ** self.gamma

        u = self.s * (selective_gain - selective_cost) + \
            (1 - self.s) * (indiscriminate_gain - indiscriminate_cost)

        difference = (tools.utility(s=self.s, x=self.x) - u).simplify()
        self.assertEqual(difference, 0)
