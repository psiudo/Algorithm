#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    vector<int> updatedLost;
    vector<int> updatedReserve;
    
    // 여벌 체육복이 있지만 도난당한 학생을 처리합니다.
    for (int lostStudent : lost) {
        if (find(reserve.begin(), reserve.end(), lostStudent) != reserve.end()) {
            reserve.erase(find(reserve.begin(), reserve.end(), lostStudent));
        } else {
            updatedLost.push_back(lostStudent);
        }
    }

    updatedReserve = reserve;

    // 체육복을 빌려줄 수 있는 경우를 처리합니다.
    sort(updatedReserve.begin(), updatedReserve.end());  // 빌려주는 학생을 순서대로 정렬
    for (int reserveStudent : updatedReserve) {
        auto it = find(updatedLost.begin(), updatedLost.end(), reserveStudent - 1);
        if (it != updatedLost.end()) {
            updatedLost.erase(it);  // 앞번호 학생에게 빌려줌
        } else {
            it = find(updatedLost.begin(), updatedLost.end(), reserveStudent + 1);
            if (it != updatedLost.end()) {
                updatedLost.erase(it);  // 뒷번호 학생에게 빌려줌
            }
        }
    }

    // 체육수업을 들을 수 있는 학생 수를 반환합니다.
    return n - updatedLost.size();
}
