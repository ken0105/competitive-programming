#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n = 0;
    cin >> n;
    vector<int> a(n);
    for(int i=0; i<n;i++){
        cin >> a[i];
    }
    sort(a.begin(),a.end(), greater<int>());
    int current_size = 0;
    int counter = 0;
    for(int i=0;i<n;i++){
        if (current_size != a[i]){
            current_size = a[i];
            counter++;
        }
    }
    cout << counter;
}
