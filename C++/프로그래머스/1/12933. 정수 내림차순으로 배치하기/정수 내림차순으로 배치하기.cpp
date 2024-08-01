#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long solution(long long n) {
    // 숫자를 문자열로 변환
    string str = to_string(n);
    
    // 문자열을 내림차순으로 정렬
    sort(str.begin(), str.end(), greater<char>());
    
    // 정렬된 문자열을 다시 정수로 변환
    long long answer = stoll(str);
    
    return answer;
}
