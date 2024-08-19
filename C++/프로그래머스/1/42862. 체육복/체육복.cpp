#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    // 여벌 체육복이 있지만 도난당한 학생을 처리합니다.
    vector<int> new_lost;
    vector<int> new_reserve;
    
    for (int l : lost) {
        if (find(reserve.begin(), reserve.end(), l) != reserve.end()) {
            reserve.erase(find(reserve.begin(), reserve.end(), l));
        } else {
            new_lost.push_back(l);
        }
    }

    new_reserve = reserve;

    // 체육복을 빌려줄 수 있는 경우를 처리합니다.
    sort(new_reserve.begin(), new_reserve.end());  // 빌려주는 학생을 순서대로 정렬
    for (int r : new_reserve) {
        auto it = find(new_lost.begin(), new_lost.end(), r - 1);
        if (it != new_lost.end()) {
            new_lost.erase(it);  // 앞번호 학생에게 빌려줌
        } else {
            it = find(new_lost.begin(), new_lost.end(), r + 1);
            if (it != new_lost.end()) {
                new_lost.erase(it);  // 뒷번호 학생에게 빌려줌
            }
        }
    }

    // 체육수업을 들을 수 있는 학생 수를 반환합니다.
    return n - new_lost.size();
}
