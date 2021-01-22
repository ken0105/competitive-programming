#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n = 0;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i<n; i++){
        cin >> a[i];
    }
    sort(a.begin(),a.end(), greater<int>());
    int alice,bob = 0;
    for (int i=0; i<n;i+=2){
        alice += a[i];
    }
    for (int i=1; i<n;i+=2){
        bob += a[i];
    }
    cout << alice - bob << endl;

}
