#include <iostream>

int divide(int i);

using namespace std;

int main() {
    int n, a, b = 0;
    cin >> n >> a >> b;
    int count = 0;
    for (int i = 0; i <= n; i++) {
        int sum = 0;
        sum = divide(i);
        if (a <= sum && sum <= b) {
            count += i;
        }
    }
    cout << count << endl;
}

int divide(int i) {
    int sum = 0;
    while (i > 0) {
        sum += i % 10;
        i = i / 10;
    }
    return sum;
}
