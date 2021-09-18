from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    start_letter = word[0]
    m = len(board)
    n = len(board[0])
    visited_blocks = {}
    for i in range(m):
        for j in range(n):

            if board[i][j] == start_letter:
                block_no = m * i + j
                visited_blocks[block_no] = True
                start_block = block_no
                if check(board, word[1:], start_block, visited_blocks, m, n):
                    return True
    return False


def check(board: List[List[str]], word: str, start_block: int, visited_blocks: dict, m: int, n: int) -> bool:
    if start_block < 0 or start_block > m * n - 1:
        return False
    index = get_index(start_block, m, n)
    i = index[0]
    j = index[1]
    if word[0] == board[i][j]:
        visited_blocks[m * i + j] = True
        return True
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    length = len(word)
    if 0 <= i - 1 <= m - 1 and (m * (i - 1) + j not in visited_blocks):
        visited_blocks[m * (i - 1) + j] = True
        if length == 1:
            return True
        c1 = check(board, word[1:], m * (i - 1) + j, visited_blocks, m, n)
    if 0 <= i + 1 <= m - 1 and (m * (i + 1) + j not in visited_blocks):
        visited_blocks[m * (i + 1) + j] = True
        if length == 1:
            return True
        c2 = check(board, word[1:], m * (i + 1) + j, visited_blocks, m, n)
    if 0 <= j - 1 <= n - 1 and (m * i + j - 1 not in visited_blocks):
        visited_blocks[m * i + (j - 1)] = True
        if length == 1:
            return True
        c3 = check(board, word[1:], m * i + j - 1, visited_blocks, m, n)
    if 0 <= j + 1 <= n - 1 and (m * i + j + 1 not in visited_blocks):
        visited_blocks[m * i + j + 1] = True
        if length == 1:
            return True
        c4 = check(board, word[1:], m * i + j + 1, visited_blocks, m, n)
    if c1 or c2 or c3 or c4:
        return True
    else:
        visited_blocks[m * i + j] = False
    return False


def get_index(block_no: int, m, n: int) -> [int, int]:
    i = block_no // m
    j = block_no - m * i
    return [i, j]


def get_block_no(m, i, j: int) -> int:
    return m * i + j


if __name__ == '__main__':
    print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
