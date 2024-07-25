#include <string>
using namespace std;

int solution(string s) {
    int result = 0; // 최종 결과를 저장할 변수
    int sign = 1; // 부호를 저장할 변수, 기본값은 양수

    // 첫 문자가 부호인 경우
    if (s[0] == '-') {
        sign = -1; // 음수로 설정
        s = s.substr(1); // 부호를 제외한 나머지 문자열로 변경
    } else if (s[0] == '+') {
        s = s.substr(1); // 부호를 제외한 나머지 문자열로 변경
    }

    // 문자열을 순회하면서 숫자로 변환
    for (char c : s) {
        result = result * 10 + (c - '0'); // 각 문자를 숫자로 변환하여 결과에 더함
    }

    return sign * result; // 부호를 반영하여 최종 결과 반환
}
