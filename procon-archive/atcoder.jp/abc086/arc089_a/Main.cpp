#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;
int t[100010];
int x[100010];
int y[100010];

int main() {
    int N;
    cin >> N;
    for (int i = 0; i < N; ++i) cin >> t[i+1] >> x[i+1] >> y[i+1];

    for (int i = 1; i <= N; i++) {
        int distance = t[i] - t[i-1];
        bool isDistanceEven = distance % 2 == 0;
        int targetDistance = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1]);
        bool isTargetDistanceEven = targetDistance % 2 == 0;
        if(distance < targetDistance || isDistanceEven != isTargetDistanceEven){
            cout << "No" << endl;
            exit(0);
        }
    }
    cout << "Yes" << endl;
    exit(0);
}


