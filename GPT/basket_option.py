import numpy as np
from .base_option import OptionBase

class BasketCall:
    def __init__(self, spots, weights, strike, expiry_date, risk_free_curve, vol_surface, corr_matrix):
        self.spots = spots
        self.weights = weights
        self.strike = strike
        self.expiry_date = expiry_date
        self.risk_free_curve = risk_free_curve
        self.vol_surface = vol_surface
        self.corr_matrix = corr_matrix

    def price(self):
        # implement basket pricing (e.g. approximated as single lognormal)
        pass

    def delta(self):
        # compute portfolio deltas per underlying
        pass