import math

class QEDRenormalizationGroup:
    def __init__(self, alpha0=1/137):
        self.alpha0 = alpha0

    def run(self, q2):
        return self.alpha0 / (1 - (self.alpha0 / (3 * math.pi)) * math.log(q2 + 1e-12))
