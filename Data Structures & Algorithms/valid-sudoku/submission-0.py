class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                block = board[i][j]
                if block == ".":
                    continue

                box_index = (i // 3) * 3 + (j // 3)
                if block in rows[i] or block in cols[j] or block in boxes[box_index]:
                    return False

                rows[i].add(block)
                cols[j].add(block)
                boxes[box_index].add(block)

        return True