A, B, V = map(int, input().split())
cnt = ((V - A) - 1) // (A - B) + 2
print(cnt)
