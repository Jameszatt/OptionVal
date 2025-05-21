import numpy as np

def compute_portfolio_greeks(positions: list) -> dict:
    # positions: list of {'option': OptionBase, 'quantity': float}
    # return aggregated delta, vega, etc.
    greeks = {'delta': 0.0, 'vega': 0.0}
    for pos in positions:
        greeks['delta'] += pos['quantity'] * pos['option'].delta()
        # similarly vega, gamma
    return greeks