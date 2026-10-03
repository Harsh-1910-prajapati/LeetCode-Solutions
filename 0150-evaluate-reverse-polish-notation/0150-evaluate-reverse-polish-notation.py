class Solution:
    def evalRPN(self, tokens):
        s = []

        for x in tokens:
            if x not in "+-*/":
                s.append(int(x))
            else:
                b = s.pop()
                a = s.pop()

                if x == "+":
                    s.append(a + b)
                elif x == "-":
                    s.append(a - b)
                elif x == "*":
                    s.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    if (a < 0) != (b < 0):
                        q = -q
                    s.append(q)

        return s[-1]