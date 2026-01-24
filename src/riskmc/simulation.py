#Monte Carlo engine

import numpy as np

def mc_gaussian_returns(returns, n_sims=100_000, horizon_days=1, seed=42):
    #simulates correlated asset returns using multivariate normal
    rng = np.random.default_rng(seed)
    mu = np.zeros(returns.shape[1])
    cov = returns.cov().values

    sims = rng.multivariate_normal(mean=mu, cov=cov, size=(n_sims, horizon_days))
    return sims.sum(axis=1)

def mc_student_t_returns(returns, n_sims=100_000, horizon_days=1, nu=5, seed=42):
    #simulates correlated asset returns using multivariate Student-t model
    rng = np.random.default_rng(seed)
    cov = returns.cov().values
    n_assets = cov.shape[0]

    #Gaussian shocks
    Z = rng.multivariate_normal(mean=np.zeros(n_assets), cov=cov, size=(n_sims, horizon_days))

    #Chi-square scaling (one scale per simulation per day)
    U = rng.chisquare(df=nu, size=(n_sims, horizon_days))
    scaling = np.sqrt(U / nu)

    #Student-t returns
    sims = Z / scaling[..., None]

    return sims.sum(axis=1)
