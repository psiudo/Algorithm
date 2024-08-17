#include <string>
#include <vector>

using namespace std;

// 방향 이동을 위한 좌표 변화량 설정
int dx[] = {-1, 1, 0, 0}; // W, E, N, S 순서
int dy[] = {0, 0, -1, 1};

vector<int> solution(vector<string> park, vector<string> routes) {
    int h = park.size(); // 공원의 세로 길이
    int w = park[0].size(); // 공원의 가로 길이
    int x = 0, y = 0;

    // 시작 지점(S) 찾기
    for (int i = 0; i < w; i++) {
        for (int j = 0; j < h; j++) {
            if (park[j][i] == 'S') {
                x = i;
                y = j;
                break;
            }
        }
    }

    // 명령을 순서대로 수행
    for (string route : routes) {
        char direction = route[0];
        int distance = stoi(route.substr(2));

        // 이동할 방향 설정
        int dir_index;
        if (direction == 'N') dir_index = 2;
        else if (direction == 'S') dir_index = 3;
        else if (direction == 'W') dir_index = 0;
        else if (direction == 'E') dir_index = 1;

        // 이동 가능한지 사전에 확인
        int temp_x = x, temp_y = y;
        bool can_move = true;

        // 가상으로 이동하며 위치가 유효한지 확인
        for (int i = 0; i < distance; i++) {
            temp_x += dx[dir_index];
            temp_y += dy[dir_index];
            if (temp_x < 0 || temp_y < 0 || temp_x >= w || temp_y >= h || park[temp_y][temp_x] == 'X') {
                can_move = false;                
            }
        }

        // 이동이 가능한 경우에만 실제 좌표 갱신
        if (can_move) {
            x = temp_x;
            y = temp_y;
        } else {
            // 이동이 불가능한 경우 temp_x, temp_y를 원래 좌표로 되돌림
            temp_x = x;
            temp_y = y;
        }
    }

    return {y, x}; // 최종 위치 반환
}
