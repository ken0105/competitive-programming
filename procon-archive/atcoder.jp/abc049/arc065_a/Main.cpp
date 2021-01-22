#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
bool dp[100010];

int main() {
    string divide[4] = {"dream", "dreamer", "erase", "eraser"};
    string s;
    cin >> s;
    dp[0] = true;
    for (int i = 0; i < s.length(); i++) {
        if (!dp[i]) {
            continue;
        }
        for (string o:divide) {
            if (o == s.substr(i, o.length())) {
                dp[i + o.length()] = true;
            }
        }
    }
    string result = "NO";
    if (dp[s.length()]) {
        result = "YES";
    }

    cout << result;
//    return 0;
}


