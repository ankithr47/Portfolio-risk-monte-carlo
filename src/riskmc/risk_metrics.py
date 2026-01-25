#Var and CVaR

import numpy as np

def var(sim_returns, alpha=0.99):
    losses = -sim_returns
    return np.quantile(losses, alpha)

def cvar(sim_returns, alpha=0.99):
    losses = -sim_returns
    var_level = np.quantile(losses, alpha)
    return losses[losses >= var_level].mean()


from scipy.stats import chi2
import numpy as np

def kupiec_test(breaches, alpha=0.99):
    """
    Kupiec unconditional coverage test for VaR.
    breaches: array of True/False
    alpha: VaR confidence level (e.g. 0.99)
    """
    breaches = np.asarray(breaches)
    x = breaches.sum()
    N = len(breaches)

    p = 1 - alpha
    phat = x / N

    # Avoid log(0)
    if phat in [0, 1]:
        return np.inf, 0.0

    LR = -2 * (
        (N - x) * np.log((1 - p) / (1 - phat))
        + x * np.log(p / phat)
    )

    p_value = 1 - chi2.cdf(LR, df=1)
    return LR, p_value

