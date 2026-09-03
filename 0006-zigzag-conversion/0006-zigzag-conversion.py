class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
            
        result = [''] * numRows
        index = 0
        step = 1
        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows -1:
                step =- 1
            index += step
        return ''.join(result)