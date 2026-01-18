#Var and CVaR

import numpy as np

def var(sim_returns, alpha=0.99):
    losses = -sim_returns
    return np.quantile(losses, alpha)

def cvar(sim_returns, alpha=0.99):
    losses = -sim_returns
    var_level = np.quantile(losses, alpha)
    return losses[losses >= var_level].mean()

