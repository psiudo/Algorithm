#include <vector>
using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    int n = arr.size();
    
    if (n == 0) return answer; // 빈 배열 처리
    
    answer.push_back(arr[0]); // 첫 번째 원소는 무조건 추가

    for (int i = 1; i < n; ++i) {
        if (arr[i] != arr[i - 1]) {
            answer.push_back(arr[i]);
        }
    }

    return answer;
}
