#include <bits/stdc++.h>
#define arrMAX 1000000
using namespace std;

long long n, k;
vector<long long> arr;

void solve () {
    cin >> n >> k; int m = sqrt(n);
    for (int i = 1; i <= m; ++i) {
        if (n % i == 0) {
            arr.push_back(i);
            long long x = n / i;
            if (x != i) arr.push_back(x);
        }
    }
    if (k > arr.size()) cout << -1;
    else {
        sort(arr.begin(),arr.end());
        cout << arr[k - 1];
    }
}

int main()
{
    freopen("KTHDIV.INP","r",stdin);
    freopen("KTHDIV.OUT","w",stdout);
    solve();
    return 0;
}
