from .base_option import OptionBase

class UpAndInBarrierCall(OptionBase):
    def __init__(self, barrier, **kwargs):
        super().__init__(**kwargs)
        self.barrier = barrier

    def price(self):
        # implement barrier pricing via QuantLib
        pass

    def delta(self):
        pass