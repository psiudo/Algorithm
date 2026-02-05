import sys

def nqueen(row, col, diag_l, diag_r):
    if row == N:
        return 1
    count = 0
    available = ((1 << N) - 1) & ~(col | diag_l | diag_r)
    while available:
        pos = available & -available
        available -= pos
        count += nqueen(row+1, col|pos, (diag_l|pos)<<1, (diag_r|pos)>>1)
    return count

N = int(sys.stdin.readline())
print(nqueen(0, 0, 0, 0))