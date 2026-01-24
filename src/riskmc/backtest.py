from riskmc.simulation import mc_gaussian_returns
from riskmc.simulation import mc_student_t_returns

import numpy as np

def backtest_var(returns, weights, var_level=0.99, window=60, model='gaussian', n_sims=50_000):
    breaches = []
    var_forecasts = []

    for t in range(window, len(returns)-1):
        window_returns = returns.iloc[t-window: t]

        #simulate returns
        if model == 'gaussian':
            sims = mc_gaussian_returns(window_returns, n_sims=n_sims)
        elif model == 'student-t':
            sims = mc_student_t_returns(window_returns, n_sims=n_sims)

        portfolio_returns = sims @ weights
        losses = -portfolio_returns

        var_t = np.quantile(losses, var_level)
        var_forecasts.append(var_t)

        #realised next day loss
        realised_return = returns.iloc[t+1] @ weights
        realised_loss = -realised_return

        breaches.append(realised_loss > var_t)
    
    return np.array(breaches), np.array(var_forecasts)