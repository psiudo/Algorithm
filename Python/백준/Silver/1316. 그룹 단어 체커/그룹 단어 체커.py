n = int(input())

count = 0
visited = set()

for _ in range(n) :
    word = input()

    visited = set()
    visited.add(word[0])

    for i in range(1, len(word)) :
        if word[i] != word[i-1] and word[i] in visited :
            break
        elif word[i] != word[i-1] and word[i] not in visited :
            visited.add(word[i])
    else :
        count += 1

print(count)

