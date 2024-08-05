#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<vector<int>> patterns = {
        {1, 2, 3, 4, 5},
        {2, 1, 2, 3, 2, 4, 2, 5},
        {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
    };
    
    vector<int> scores(3, 0);
    
    for (size_t i = 0; i < answers.size(); ++i) {
        if (patterns[0][i % patterns[0].size()] == answers[i]) scores[0]++;
        if (patterns[1][i % patterns[1].size()] == answers[i]) scores[1]++;
        if (patterns[2][i % patterns[2].size()] == answers[i]) scores[2]++;
    }
    
    int max_score = *max_element(scores.begin(), scores.end());
    vector<int> result;
    for (int i = 0; i < 3; ++i) {
        if (scores[i] == max_score) result.push_back(i + 1);
    }
    
    return result;
}
