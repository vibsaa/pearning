class fixedfloat:
    def __init__(self,amount):
        self.amount=amount
    def __repr__(self):
        return f'<fixedfloat {self.amount:.2f}>'
    @classmethod    
    def fromsum(cls,val1, val2):
        return cls(val1+val2)
    
class dollar(fixedfloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol='$'
    def __repr__(self):
        return f"<dollar {self.symbol}{self.amount:.2f}>"

print(dollar.fromsum(17.4483,19))