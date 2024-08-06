#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int max_width = 0;
    int max_height = 0;

    for (int i = 0; i < sizes.size(); ++i) {
        int w = max(sizes[i][0], sizes[i][1]);
        int h = min(sizes[i][0], sizes[i][1]);
        
        max_width = max(max_width, w);
        max_height = max(max_height, h);
    }

    return max_width * max_height;
}
