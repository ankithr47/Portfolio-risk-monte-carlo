# Portfolio Risk Forecasting via Monte Carlo Simulation

This project implements and validates a **one-day portfolio risk forecasting framework** using Monte Carlo simulation. It compares **Gaussian and Student-t return models**, incorporates **time-varying volatility via EWMA covariance**, and evaluates model performance through **rolling VaR backtests and statistical coverage diagnostics**.

The goal is to demonstrate how distributional assumptions and volatility dynamics materially affect tail-risk estimates.

---

## Key Features

* Correlated Monte Carlo simulation of multi-asset portfolio returns
* Gaussian and Student-t return models for tail-risk comparison
* EWMA covariance to capture time-varying volatility
* One-day VaR (95%, 99%) and CVaR estimation
* Rolling VaR backtesting using historical returns
* Kupiec unconditional coverage tests for model validation
* Clean, modular Python implementation with reproducible notebook

---

## Portfolio & Data

* Assets: **SPY, TLT, GLD, QQQ**
* Frequency: Daily returns
* Horizon: **One trading day**
* Backtest period: Multi-year rolling window
* Portfolio weights: Fixed, exogenous (not optimized)

Expected returns are set to zero to focus on **short-horizon risk**, consistent with industry practice for VaR modeling.

---

## Methodology

### 1. Return Modeling

* Compute daily log returns from historical prices
* Estimate covariance using:

  * Sample covariance (baseline)
  * EWMA covariance (λ = 0.94)

### 2. Monte Carlo Simulation

* Generate correlated one-day return scenarios using:

  * Multivariate Gaussian
  * Multivariate Student-t (heavy-tailed)
* Aggregate simulated asset returns to portfolio PnL

### 3. Risk Metrics

* Compute portfolio loss distribution
* Estimate:

  * VaR at 95% and 99%
  * CVaR at 95% and 99%

### 4. Backtesting & Validation

* Rolling 60-day estimation window
* One-day-ahead VaR forecasts
* Compare realized losses against forecast VaR
* Evaluate coverage using Kupiec unconditional coverage tests

---

## Key Results

* **Gaussian Monte Carlo underestimates tail risk** when volatility is assumed constant.
* **EWMA covariance materially improves Gaussian VaR coverage** by capturing volatility clustering.
* **Student-t models produce heavier tails**, resulting in higher and more conservative CVaR estimates.
* In backtesting:

  * Gaussian + EWMA passes coverage but is less well calibrated.
  * Student-t + EWMA achieves stronger statistical consistency with nominal 99% VaR (higher Kupiec p-values).

Overall, **Student-t with EWMA covariance provides the most robust tail-risk calibration** in this framework.

---

## Interpretation

This project highlights two central lessons in risk modeling:

1. **Volatility dynamics matter** — static covariance leads to systematic under-coverage.
2. **Distributional assumptions matter** — Gaussian tails underestimate extreme losses even when volatility is modeled dynamically.

Monte Carlo simulation enables forward-looking risk forecasts that cannot be obtained directly from historical quantiles alone.

---

## Project Structure

```
src/riskmc/
├── data.py          # price loading & preprocessing
├── returns.py       # return calculations
├── simulation.py    # Gaussian & Student-t MC engines
├── risk_metrics.py  # VaR, CVaR, Kupiec test
├── backtest.py      # rolling VaR backtesting
├── covariance.py    # EWMA covariance
└── plots.py         # visualization utilities

notebooks/
└── portfolio_risk_forecasting.ipynb
```

---

## Future Extensions (Optional)

* Independence (Christoffersen) VaR tests
* Multi-day horizon risk forecasts
* Scenario-based stress testing
* Dynamic portfolio weights / rebalancing
* Comparison with historical simulation VaR

---

## Why This Project

This project is designed to mirror **real-world risk modeling workflows**, emphasizing:

* statistical analysis,
* model validation,
* clear economic interpretation.

It is intended as a practical demonstration of quantitative risk forecasting rather than a purely academic exercise.


