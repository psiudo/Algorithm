#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> wallpaper) {
    int lux = 50, luy = 50;  // 최대 크기보다 큰 초기값 설정
    int rdx = 0, rdy = 0;

    for (int i = 0; i < wallpaper.size(); i++) {
        for (int j = 0; j < wallpaper[i].size(); j++) {
            if (wallpaper[i][j] == '#') {
                lux = min(lux, i);  // 가장 위쪽의 파일 위치
                luy = min(luy, j);  // 가장 왼쪽의 파일 위치
                rdx = max(rdx, i + 1);  // 가장 아래쪽의 파일 위치 (드래그 끝점은 다음 칸까지 포함)
                rdy = max(rdy, j + 1);  // 가장 오른쪽의 파일 위치 (드래그 끝점은 다음 칸까지 포함)
            }
        }
    }

    return {lux, luy, rdx, rdy};
}
