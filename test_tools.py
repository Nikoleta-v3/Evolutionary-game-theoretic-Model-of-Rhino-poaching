import unittest
import tools

import sympy as sym
import numpy as np


class TestUtilityFunctions(unittest.TestCase):
    r, s, x, theta_r = sym.symbols("r, s, x, theta_r", positive=True)
    alpha, H, beta, gamma, F = sym.symbols("alpha, H, beta, gamma, F",
                                           positive=True)

    def test_theta(self):
        self.assertEqual(tools.theta(self.r, self.s, self.theta_r) - (self.s *
                         (1 - self.r) + (1 - self.s) * ((self.theta_r - 1) *
                                                        self.r + 1)), 0)

    def test_psi(self):
        self.assertEqual(tools.psi(r=self.r, s=self.s), 1 - self.r * self.s)

    def test_gain(self):
        selective_gain = tools.theta(self.r, 1) * self.H *\
                         tools.theta(self.r, self.x) ** (- self.alpha)

        indiscriminate_gain = tools.theta(self.r, 0) * self.H *\
                              tools.theta(self.r, self.x) ** (- self.alpha)

        self.assertEqual(selective_gain, tools.gain(1))
        self.assertEqual(indiscriminate_gain, tools.gain(0))

    def test_cost(self):
        selective_cost = (1 / tools.psi(self.r, 1)) * self.F *\
                         tools.psi(self.r, self.x) ** self.gamma * (1 -
                                                                    self.r) ** self.beta

        indiscriminate_cost = (1 / tools.psi(self.r, 0)) * self.F *\
                              tools.psi(self.r, self.x) ** self.gamma *\
                              (1 - self.r) ** self.beta

        self.assertEqual(selective_cost, tools.cost(1))
        self.assertEqual(indiscriminate_cost, tools.cost(0))


class TestUtility(unittest.TestCase):
    r, s, x, theta_r, alpha, H, beta, gamma, F = sym.symbols("""r, s, x,
                                                                theta_r, alpha,
                                                                H, beta, gamma,
                                                                F""",
                                                             positive=True)

    def test_utility(self):
        selective = self.H * (1 - self.r) ** (1 - self.alpha) - \
                    self.F * (1 - self.r) ** (self.gamma + self.beta - 1)

        indiscriminate = self.H * (self.theta_r * self.r + 1 - self.r) *\
                         (self.theta_r * self.r + 1 - self.r) ** -self.alpha \
                         - self.F *(1 - self.r) ** self.beta

        self.assertEqual((tools.utility(1, 1) - selective).simplify(), 0)
        self.assertEqual((tools.utility(0, 0) - indiscriminate).simplify(), 0)


class TestStabilityFunctions(unittest.TestCase):
    r, s, x, theta_r, alpha, H, beta, gamma, F = sym.symbols("""r, s, x,
                                                                theta_r, alpha,
                                                                H, beta, gamma,
                                                                F""",
                                                             positive=True)

    def test_stable_mixed_condition(self):
        condition = tools.utility(1, self.s) - tools.utility(0, self.s)
        self.assertEqual((tools.stable_mixed_condition() -
                          condition).simplify(), 0)

    def test_stable_selective_condition(self):
        condition = sym.lambdify([self.r, self.theta_r, self.H, self.F,
                                  self.gamma, self.alpha, self.beta],
                                 tools.stable_selective_condition())

        self.assertTrue(condition(0, 0, 1, 1, 0.166667, 0.666667, 0.666667))

    def test_stable_indiscriminate_condition(self):
        condition = sym.lambdify([self.r, self.theta_r, self.H, self.F,
                                  self.gamma, self.alpha, self.beta],
                                 tools.stable_indiscriminate_condition())

        self.assertTrue(condition(0.080808, 1.0, 1.0, 1.0, 0.5, 0.0, 0.5))

    def test_s_star_v_r(self):
        # test default values
        self.assertTrue(np.isnan(tools.s_star_v_r()))

