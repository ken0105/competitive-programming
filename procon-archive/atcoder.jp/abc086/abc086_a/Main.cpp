#include <iostream>

using namespace std;

int main() {
    int a, b = 0;
    cin >> a >> b;
    if (a * b % 2 == 0) {
        cout << "Even";
    } else {
        cout << "Odd";
    }
}
