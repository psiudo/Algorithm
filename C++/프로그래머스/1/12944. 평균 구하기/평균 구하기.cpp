#include <iostream>
#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    for (int i = 0; i < arr.size(); i++) {
        answer = (answer * (i) + arr[i]) / (i+1);

    }

    return answer;
}

int main(){
    vector<int> arr1 = {1,2,3,4};
    cout << "average: " << solution(arr1) << endl;

    vector<int> arr2 = {5, 5};
    cout << "average: " << solution(arr2) << endl;

    return 0;

}