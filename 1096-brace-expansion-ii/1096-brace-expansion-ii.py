class Solution:
    def braceExpansionII(self, expression):
        def merge(a, b):
            return {x + y for x in a for y in b}

        def solve(s):
            result = set()
            current = {""}
            i = 0

            while i < len(s):
                if s[i] == '{':
                    count = 1
                    j = i + 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    inside = s[i + 1:j - 1]
                    parts = []
                    start = 0
                    depth = 0

                    for k, ch in enumerate(inside):
                        if ch == '{':
                            depth += 1
                        elif ch == '}':
                            depth -= 1
                        elif ch == ',' and depth == 0:
                            parts.append(inside[start:k])
                            start = k + 1

                    parts.append(inside[start:])

                    group = set()
                    for part in parts:
                        group |= solve(part)

                    current = merge(current, group)
                    i = j

                elif s[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                else:
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1

                    current = merge(current, {s[i:j]})
                    i = j

            result |= current
            return result

        return sorted(solve(expression))