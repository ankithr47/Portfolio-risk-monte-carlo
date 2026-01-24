#visualisation

import matplotlib.pyplot as plt
import numpy as np

def plot_t_pnl_distribution(sim_returns1, sim_returns2, var_95, var_99, cvar_95, cvar_99):
    losses1 = -sim_returns1
    losses2 = -sim_returns2

    plt.hist(losses1, bins=300, density=True)
    plt.axvline(var_95)
    plt.axvline(var_99)
    plt.axvline(cvar_95, color='red')
    plt.axvline(cvar_99, color='red')
    plt.title('Simulated Portfolio Loss Distribution: Student-t')
    plt.xlabel('Loss')
    plt.ylabel('Density')
    left, right = np.percentile(np.concatenate([losses1, losses2]), [1, 99.9])
    plt.xlim(left, right)
    plt.show()

def plot_gaussian_pnl_distribution(sim_returns1, sim_returns2, var_95, var_99, cvar_95, cvar_99):
    losses1 = -sim_returns1
    losses2 = -sim_returns2

    plt.hist(losses1, bins=100, density=True)
    plt.axvline(var_95)
    plt.axvline(var_99)
    plt.axvline(cvar_95, color='red')
    plt.axvline(cvar_99, color='red')
    plt.title('Simulated Portfolio Loss Distribution: Gaussian')
    plt.xlabel('Loss')
    plt.ylabel('Density')
    left, right = np.percentile(np.concatenate([losses1, losses2]), [1, 99.9])
    plt.xlim(left, right)
    plt.show()