class Solution(object):
    def divide(self, dividend, divisor):
        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        if sign < 0:
            result = -result

        if result > 2**31 - 1:
            return 2**31 - 1

        if result < -2**31:
            return -2**31

        return result