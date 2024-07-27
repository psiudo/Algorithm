#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

int solution(vector<int> nums) {
    unordered_set<int> unique_pokemon(nums.begin(), nums.end());
    int max_pokemon_count = nums.size() / 2;
    int unique_pokemon_count = unique_pokemon.size();
    
    return min(max_pokemon_count, unique_pokemon_count);
}
