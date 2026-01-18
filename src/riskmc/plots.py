#visualisation

import matplotlib.pyplot as plt
import numpy as np

def plot_pnl_distribution(sim_returns, var_95, var_99):
    losses = -sim_returns

    plt.hist(losses, bins=100, density=True)
    plt.axvline(var_95)
    plt.axvline(var_99)
    plt.title('Simulated Portfolio Loss Distribution')
    plt.xlabel('Loss')
    plt.ylabel('Density')
    plt.show()