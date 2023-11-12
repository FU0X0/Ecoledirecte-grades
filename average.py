class Avg:
    def __init__(self):
        self.avg = 0
        self.fullCoef = 0
    def add(self, grade:float, divisor:int, coef:float=1):
        grade, divisor, coef = float(grade), int(divisor), float(coef)
        self.avg += grade / divisor * coef
        self.fullCoef += coef
    def get(self, divisor:int=20):
        try:
            return self.avg / self.fullCoef * divisor
        except ZeroDivisionError:
            return False