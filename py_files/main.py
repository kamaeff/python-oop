class A:
    x = 10
    def __init__(self, val1, val2):
        self.y = 88
        self.first = val1
        self.second = val2


class B:
    def __init__(self):
        A.__init__(self, a, b)
    def sum(self):
        res = self.first + self.second
        return res

# Return sum of val1 and val2 from 2 different classes
try:
    a = float(input('Paste first number: '))
    b = float(input('Paste second number: '))
    out_2 = B()
    print(f'Res: {out_2.sum()}')
except ValueError:
    print(f'String must be int, float and not null (:')
