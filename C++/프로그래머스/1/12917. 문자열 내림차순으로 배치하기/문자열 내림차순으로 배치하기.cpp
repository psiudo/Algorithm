#include <string>
#include <algorithm>

using namespace std;

string solution(string s) {
    // 문자열을 내림차순으로 정렬
    sort(s.begin(), s.end(), greater<char>());
    return s;
}
