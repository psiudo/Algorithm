import sys
from collections import deque

def process_commands():
    # 입력 빠르게 받기
    input = sys.stdin.read
    data = input().splitlines()

    N = int(data[0])  # 명령 개수
    deque_structure = deque()
    output = []

    for i in range(1, N + 1):
        command = data[i]

        if command.startswith("1 "):  # 1 X: 앞에 넣기
            _, X = command.split()
            deque_structure.appendleft(int(X))

        elif command.startswith("2 "):  # 2 X: 뒤에 넣기
            _, X = command.split()
            deque_structure.append(int(X))

        elif command == "3":  # 3: 앞에서 빼고 출력
            if deque_structure:
                output.append(str(deque_structure.popleft()))
            else:
                output.append("-1")

        elif command == "4":  # 4: 뒤에서 빼고 출력
            if deque_structure:
                output.append(str(deque_structure.pop()))
            else:
                output.append("-1")

        elif command == "5":  # 5: 덱 크기 출력
            output.append(str(len(deque_structure)))

        elif command == "6":  # 6: 덱이 비어있는지 확인
            output.append("1" if not deque_structure else "0")

        elif command == "7":  # 7: 맨 앞의 값 출력
            if deque_structure:
                output.append(str(deque_structure[0]))
            else:
                output.append("-1")

        elif command == "8":  # 8: 맨 뒤의 값 출력
            if deque_structure:
                output.append(str(deque_structure[-1]))
            else:
                output.append("-1")

    sys.stdout.write("\n".join(output) + "\n")

process_commands()
