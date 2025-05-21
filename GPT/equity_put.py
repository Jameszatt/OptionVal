from .base_option import OptionBase

class AmericanPut(OptionBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def price(self):
        # use binomial/trinomial or QuantLib American engine
        pass

    def delta(self):
        # approximate or analytic if available
        pass