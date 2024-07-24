#include <string>
#include <iostream>
using namespace std;

bool solution(string s) {
    int count = 0;

    for (char ch : s) {
        if (ch == 'p' || ch == 'P') count++;
        if (ch == 'y' || ch == 'Y') count--;
    }

    if (count == 0) {
        cout << "True" << endl;
        return true;
    } else {
        cout << "False" << endl;
        return false;
    }
}

int main() {
    string input = "pPoooyY";
    solution(input);
    return 0;
}
