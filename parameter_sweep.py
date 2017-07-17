"""
Parameter for different environments.
"""
import csv
import itertools
import multiprocessing
import sys

import numpy as np

import tools

def main(r, theta_r, H, F, gamma, alpha, beta, tol):
    indiscriminate_stable = H * theta_r * (theta_r - r + 1) ** (-alpha) > F * (1 - r) ** (-beta)
    selective_stable = H * theta_r * (1 - r) ** (-alpha) > F * (1 - r) ** (- gamma - beta)
    # INCLUDE This mixed_stable = tools.
    # Evolutionary_stability
    return r, theta_r, H, F, gamma, alpha, beta, indiscriminate_stable, selective_stable

if __name__ == "__main__":


    number_steps = int(sys.argv[1])
    tol = float(sys.argv[2])

    rs = np.linspace(0, 1, number_steps)
    theta_rs = np.linspace(0, 1, number_steps)
    Hs = np.linspace(0, 500, number_steps)
    Fs = np.linspace(0, 50, number_steps)
    gammas = np.linspace(0, 2, number_steps)
    alphas = np.linspace(0, 2, number_steps)
    betas = np.linspace(0, 2, number_steps)
    tols = itertools.repeat(tol, number_steps)

    parameters = itertools.product(rs, theta_rs, Hs, Fs,
                                   gammas, alphas, betas, tols)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    data = pool.starmap(main, parameters)

    filename = "./data/data_{}_{}.csv".format(number_steps, tol)
    with open(filename, "w") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
