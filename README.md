# Portfolio Risk Forecasting (Monte Carlo MVP)

This project forecasts the forward PnL distribution of a multi-asset portfolio
using Monte Carlo simulation and estimates tail risk via VaR and CVaR.

## MVP Features
- Correlated Monte Carlo simulation (Gaussian)
- Portfolio-level PnL distribution
- VaR(95%, 99%) and CVaR(99%)
- Reproducible research notebook

## Methodology
1. Compute daily log returns
2. Estimate mean and covariance
3. Simulate correlated returns
4. Aggregate to portfolio PnL
5. Compute VaR / CVaR

## Next Steps
- Heavy-tailed distributions (Student-t)
- Rolling backtests and VaR validation
- Stress testing and scenario analysis
- add rebalancing logic 
- extend this to multi-day horizons

