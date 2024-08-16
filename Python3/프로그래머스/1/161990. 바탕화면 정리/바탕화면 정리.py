def solution(wallpaper):
    lux = len(wallpaper)  # 세로의 최대값보다 큰 초기값
    luy = len(wallpaper[0])  # 가로의 최대값보다 큰 초기값
    rdx = 0
    rdy = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)  # 끝점은 파일이 있는 칸의 다음 칸을 포함
                rdy = max(rdy, j + 1)  # 끝점은 파일이 있는 칸의 다음 칸을 포함

    return [lux, luy, rdx, rdy]
    