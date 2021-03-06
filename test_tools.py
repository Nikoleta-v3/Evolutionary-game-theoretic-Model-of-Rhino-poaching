import unittest
import tools

import sympy as sym
import numpy as np


class TestUtilityFunctions(unittest.TestCase):
    r, s, x, tau, theta_r = sym.symbols("r, s, x, tau, theta_r", positive=True)
    alpha, H, beta, gamma, F = sym.symbols(
        "alpha, H, beta, gamma, F", positive=True
    )

    def test_theta(self):
        self.assertEqual(
            tools.theta(self.r, self.s, self.theta_r)
            - (
                self.s * (1 - self.r)
                + (1 - self.s) * ((self.theta_r - 1) * self.r + 1)
            ),
            0,
        )

    def test_gain(self):
        selective_gain = (
            tools.theta(self.r, 1)
            * self.H
            * tools.theta(self.r, self.x) ** (-self.alpha)
        )

        indiscriminate_gain = (
            tools.theta(self.r, 0)
            * self.H
            * tools.theta(self.r, self.x) ** (-self.alpha)
        )

        self.assertEqual(selective_gain, tools.gain(1))
        self.assertEqual(indiscriminate_gain, tools.gain(0))

    def test_selective_time(self):
        selective_time = tools.selective_time(r=self.r, tau=self.tau)
        i = sym.Symbol("i")
        series = sym.summation(
            self.r ** i * (i + self.tau), (i, 0, sym.oo)
        ).simplify()
        expected = (series.args[0][0] * (1 - self.r)).simplify()
        self.assertEqual((expected - selective_time).simplify(), 0)

    def test_indiscriminate_time(self):
        for N_r in (1, 3, 10, 20):
            indiscriminate_time = tools.indiscriminate_time(
                r=self.r, tau=self.tau, N_r=N_r
            )
            i = sym.Symbol("i")
            series = sym.summation(
                self.r ** (i - 1) * i, (i, 1, N_r - 1)
            ).simplify()
            expected = (
                series * (1 - self.r) * self.tau
                + self.r ** (N_r - 1) * N_r * self.tau
            ).simplify()
            self.assertEqual((expected - indiscriminate_time).simplify(), 0)

    def test_cost(self):
        selective_cost = (
            self.F
            * (1 - self.r) ** self.beta
            * tools.selective_time(r=self.r, tau=self.tau)
        )

        N_r = sym.ceiling(1 / self.theta_r)
        indiscriminate_cost = (
            self.F
            * (1 - self.r) ** self.beta
            * tools.indiscriminate_time(r=self.r, tau=self.tau, N_r=N_r)
        )

        self.assertEqual(
            selective_cost.simplify(), tools.cost(s=1, tau=self.tau).simplify()
        )
        self.assertEqual(
            indiscriminate_cost.simplify(), tools.cost(s=0, tau=self.tau).simplify()
        )


class TestUtility(unittest.TestCase):
    r, s, x, theta_r, alpha, H, beta, Gamma, F, tau = sym.symbols(
        "r, s, x, theta_r, alpha, H, beta, Gamma, F, tau", positive=True
    )

    def test_utility(self):
        selective = self.H * (1 - self.r) ** (1 - self.alpha) - self.F * (
            self.r + self.tau * (1 - self.r)
        ) * (1 - self.r) ** (self.beta - 1)

        N_r = sym.ceiling(1 / self.theta_r)
        indiscriminate = self.H * (self.theta_r * self.r + 1 - self.r) * (
            self.theta_r * self.r + 1 - self.r
        ) ** -self.alpha - self.F * (1 - self.r ** N_r) * self.tau * (
            1 - self.r
        ) ** (
            self.beta - 1
        ) - self.Gamma

        self.assertEqual((tools.utility(s=1, x=1) - selective).simplify(), 0)
        self.assertEqual(
            (tools.utility(s=0, x=0) - indiscriminate).simplify(), 0
        )
