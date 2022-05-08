#include <bits/stdc++.h>
#include <vector>
#define arrMAX 100001
using namespace std;

int n; long long out, arr[arrMAX];

void input ()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        cin >> arr[i];
        out += arr[i];
    }
}

void solve ()
{
    input(); sort (arr, arr+n);
    arr[n + 1] = arr[n] + 1;
    long long S = out;
    long long x = 0;
    for (int i = 0; i < n; i++)
    {
        x += arr[i];
        if (arr[i] != arr[i + 1])
        {
            if (x < S) S = x;
            x = 0;
        }
    }
    cout << (out -= S);
}

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("BONUS.INP","r",stdin);
    freopen("BONUS.OUT","w",stdout);
    solve();
    return 0;
}
