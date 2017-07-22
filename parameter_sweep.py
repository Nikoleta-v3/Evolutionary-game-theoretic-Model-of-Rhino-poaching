"""
Parameter for different environments.
"""
import csv
import itertools
import multiprocessing
import sys

import numpy as np

import tools


def main(r, theta_r, H, F, gamma, alpha, beta, tol, epsilon, step):

    indiscriminate_evol_stable, selective_evol_stable = False, False
    mixed_evol_stable = False

    indiscriminate_stable = tools.stable_indiscriminate_condition(H=H, F=F, r=r,
                                                                  alpha=alpha,
                                                                  beta=beta,
                                                                theta_r=theta_r)

    selective_stable = tools.stable_selective_condition(H=H, F=F, r=r,
                                                        alpha=alpha, beta=beta,
                                                        gamma=gamma,
                                                        theta_r=theta_r)

    mixed_stable = tools.s_star_v_r(r_val=r, gamma_num=gamma, beta_num=beta,
                                    alpha_num=alpha, theta_r_num=theta_r,
                                    F_num=F, H_num=H)

    if indiscriminate_stable:
        indiscriminate_evol_stable = tools.evolutionary_stability(s=0, r_val=r,
                                gamma_num=gamma, beta_num=beta, alpha_num=alpha,
                                theta_r_num=theta_r, F_num=F,  H_num=H,
                                tol=tol, starting_epsilon=epsilon, step=step)[-1]

    if selective_stable:
        selective_evol_stable = tools.evolutionary_stability(s=1, r_val=r,
                                gamma_num=gamma, beta_num=beta, alpha_num=alpha,
                                theta_r_num=theta_r, F_num=F,  H_num=H,
                                tol=tol, starting_epsilon=epsilon, step=step)[-1]

    if not np.isnan(mixed_stable):
        mixed_evol_stable = tools.evolutionary_stability(s=mixed_stable, r_val=r,
                                gamma_num=gamma, beta_num=beta, alpha_num=alpha,
                                theta_r_num=theta_r, F_num=F, H_num=H,
                                tol=tol, starting_epsilon=epsilon, step=step)[-1]


    # Write data to file
    key = "-".join(map(str, [r, theta_r, H, F, gamma, alpha, beta]))
    key = key.replace(".", "_")
    filename = "./data/{}.csv".format(key)
    header = ["r", "theta_r", "H", "F", "gamma", "alpha", "beta",
              "indiscriminate_stable", "selective_stable", "mixed_stable",
              "indiscriminate_evol_stable", "selective_evol_stable",
              "mixed_evol_stable"]
    row = [r, theta_r, H, F, gamma, alpha, beta, indiscriminate_stable,
           selective_stable, mixed_stable, indiscriminate_evol_stable,
           selective_evol_stable, mixed_evol_stable]

    with open(filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(row)

if __name__ == "__main__":

    number_steps = int(sys.argv[1])
    tol = float(sys.argv[2])
    epsilon = float(sys.argv[3])
    step = float(sys.argv[4])

    rs = np.linspace(0, 1, number_steps)
    theta_rs = np.linspace(0, 1, number_steps)
    Hs = np.linspace(1, 500, number_steps)
    Fs = np.linspace(1, 50, number_steps)
    gammas = np.linspace(1, 3, number_steps)
    alphas = np.linspace(0, 2, number_steps)
    betas = np.linspace(0, 2, number_steps)
    tols = itertools.repeat(tol, number_steps)
    epsilons = itertools.repeat(epsilon, number_steps)
    steps = itertools.repeat(step, number_steps)

    parameters = itertools.product(rs, theta_rs, Hs, Fs,
                                   gammas, alphas, betas, tols, epsilons, steps)

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    pool.starmap(main, parameters)
