def solution(park, routes):
    # 방향 이동을 위한 좌표 변화량 설정
    dx = [-1, 1, 0, 0]  # W, E, N, S 순서
    dy = [0, 0, -1, 1]

    h = len(park)  # 공원의 세로 길이
    w = len(park[0])  # 공원의 가로 길이
    x, y = 0, 0

    # 시작 지점(S) 찾기
    for i in range(w):
        for j in range(h):
            if park[j][i] == 'S':
                x = i
                y = j
                break

    # 명령을 순서대로 수행
    for route in routes:
        direction = route[0]
        distance = int(route[2:])

        # 이동할 방향 설정
        if direction == 'N':
            dir_index = 2
        elif direction == 'S':
            dir_index = 3
        elif direction == 'W':
            dir_index = 0
        else:
            dir_index = 1

        # 이동 가능한지 사전에 확인
        temp_x = x
        temp_y = y
        can_move = True

        # 가상으로 이동하며 위치가 유효한지 확인
        for i in range(distance):
            temp_x += dx[dir_index]
            temp_y += dy[dir_index]
            if temp_x < 0 or temp_y < 0 or temp_x >= w or temp_y >= h or park[temp_y][temp_x] == 'X':
                can_move = False                
                break

        # 이동이 가능한 경우에만 실제 좌표 갱신
        if can_move:
            x = temp_x
            y = temp_y
        else:
            # 이동이 불가능한 경우 temp_x, temp_y를 원래 좌표로 되돌림
            temp_x = x
            temp_y = y

    return [y, x]  # 최종 위치 반환
