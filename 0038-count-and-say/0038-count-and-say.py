class Solution(object):
    def countAndSay(self, n):
        result = "1"

        for _ in range(n - 1):
            current = ""
            i = 0

            while i < len(result):
                j = i

                while j < len(result) and result[j] == result[i]:
                    j += 1

                current += str(j - i) + result[i]
                i = j

            result = current

        return result