#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0;
    int max_height = 0;
    
    for (const auto& size : sizes) {
        int w = size[0];
        int h = size[1];
        if (w < h) {
            swap(w, h); // w가 항상 더 크도록 설정
        }
        max_width = max(max_width, w);
        max_height = max(max_height, h);
    }
    
    int answer = max_width * max_height;
    return answer;
}
