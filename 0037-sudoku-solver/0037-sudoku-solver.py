class Solution(object):
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def solve():
            if not empty:
                return True

            best = -1
            options = None

            for i in range(len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + c // 3

                possible = set("123456789") - rows[r] - cols[c] - boxes[b]

                if not possible:
                    return False

                if options is None or len(possible) < len(options):
                    options = possible
                    best = i

                    if len(options) == 1:
                        break

            r, c = empty.pop(best)
            b = (r // 3) * 3 + c // 3

            for num in options:
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[b].add(num)

                if solve():
                    return True

                board[r][c] = "."
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[b].remove(num)

            empty.insert(best, (r, c))
            return False

        solve()