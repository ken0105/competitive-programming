#include <iostream>

using namespace std;

int N;
int A[210];         // 最大 200 個なので余裕を持って 210 に --- 200 以上ならなんでもよいです

int main() {
    int a,b,c,x = 0;
    int count = 0;
    cin >> a >> b >> c >> x;
    for (int i = 0; i <= a; i++){
        for (int j = 0; j <= b ; j++){
            for (int k=0; k <= c ; k++){
                int sum = 500*i + 100*j + 50 * k;
                if(sum == x){
                    count++;
                }
            }
        }
    }
    cout << count << endl;
}
