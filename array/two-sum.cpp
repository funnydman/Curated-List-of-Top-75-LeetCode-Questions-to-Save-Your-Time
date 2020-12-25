#include <bits/stdc++.h>
#include "vector"

using namespace std;

vector<int> two_sum(vector<int> &nums, int target) {
    map<int, int> table;
    for (int i = 0; i < nums.size(); i++) {
        int diff = target - nums[i];
        if (table.count(nums[i])) {
            return {table[nums[i]], i};
        }
        table[diff] = i;
    }
    return {0, 0};
}

int main() {
    vector<int> nums = {3, 2, 4};

    vector<int> res = two_sum(nums, 6);
    for (auto e: res) {
        cout << e << endl;
    }

}
