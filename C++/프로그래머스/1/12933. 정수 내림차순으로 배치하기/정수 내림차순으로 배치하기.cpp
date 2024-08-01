#include <vector>
#include <algorithm>

using namespace std;

long long solution(long long n) {
    vector<int> digits;
    
    // 자릿수를 벡터에 저장
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    
    // 벡터를 내림차순으로 정렬
    sort(digits.begin(), digits.end(), greater<int>());
    
    // 정렬된 자릿수를 이용해 다시 정수로 변환
    long long answer = 0;
    for (int digit : digits) {
        answer = answer * 10 + digit;
    }
    
    return answer;
}
