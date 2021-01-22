#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

#define ll long long
#define rep(i, n) for(int i = 0; i< (int)(n); i++)

using namespace std;

int main() {
    int n, k = 0;
    cin >> n >> k;
    vector<int> p(n);
    int sum = 0;
    rep(i, n){
        cin >> p[i];
    }
    sort(p.begin(), p.end());
    rep(i, k) {
        sum += p[i];
    }
    cout << sum;

}


