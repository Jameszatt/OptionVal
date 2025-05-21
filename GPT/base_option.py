import numpy as np
import QuantLib as ql

class OptionBase:
    def __init__(self, spot, strike, expiry_date, risk_free_curve, vol_surface):
        self.spot = spot
        self.strike = strike
        self.expiry_date = expiry_date
        self.risk_free_curve = risk_free_curve
        self.vol_surface = vol_surface

    def price(self):
        raise NotImplementedError("Must implement pricing method in subclass")

    def delta(self):
        raise NotImplementedError("Must implement delta in subclass")