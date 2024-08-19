#include <vector>
#include <algorithm>

using namespace std;

int solution(int k, int m, vector<int> score) {
    // 사과 점수를 내림차순으로 정렬
    sort(score.rbegin(), score.rend());
    
    int totalProfit = 0;
    int count = 0;

    // 상자 단위로 처리
    for (int s : score) {
        count++;
        if (count == m) {
            totalProfit += s * m;  // 상자에 담긴 사과의 점수 * m (상자에 담긴 사과 개수)
            count = 0;  // 상자 포장이 끝났으므로 카운트 초기화
        }
    }
    
    return totalProfit;
}
