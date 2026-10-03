class MinStack:

    def __init__(self):
        self.s = []

    def push(self, val):
        self.s.append((val, min(val, self.s[-1][1]) if self.s else val))

    def pop(self):
        self.s.pop()

    def top(self):
        return self.s[-1][0]

    def getMin(self):
        return self.s[-1][1]