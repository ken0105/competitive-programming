#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;


int main() {
    string s = "";
    string t = "";
    cin >> s >> t;
    int counter = 0;
    for(int i = 0; i< s.length(); i++){
        if(s[i] != t[i]) {
            counter++;
        }
    }
    cout << counter;
}


