class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            j = i
            length = 0

            while j < len(words) and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1

            count = j - i
            spaces = maxWidth - length

            if j == len(words) or count == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                base = spaces // (count - 1)
                extra = spaces % (count - 1)
                line = ""

                for k in range(count - 1):
                    line += words[i + k]
                    line += " " * (base + (1 if k < extra else 0))

                line += words[j - 1]

            res.append(line)
            i = j

        return res