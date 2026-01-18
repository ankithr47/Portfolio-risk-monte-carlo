#Monte Carlo engine

import numpy as np

def mc_gaussian_returns(returns, n_sims=100_000, horizon_days=1, seed=42):
    #simulates correlated asset returns using multivariate normal
    rng = np.random.default_rng(seed)
    mu = returns.mean().values
    cov = returns.cov().values

    sims = rng.multivariate_normal(mean=mu, cov=cov, size=(n_sims, horizon_days))
    return sims.sum(axis=1)
