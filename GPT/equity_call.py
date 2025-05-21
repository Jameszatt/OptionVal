from .base_option import OptionBase

class EuropeanCall(OptionBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def price(self):
        # implement Black-Scholes or use QuantLib engine
        pass

    def delta(self):
        # compute analytic delta
        pass