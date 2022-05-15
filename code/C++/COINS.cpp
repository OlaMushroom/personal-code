#include <bits/stdc++.h>
#define arrMAX 100000
using namespace std;

int n, m;
struct coins
{
    int a, b, c;
} arr[arrMAX];

void input ()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++) cin >> arr[i].a;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i].b;
        arr[i].c = arr[i].b - arr[i].a;
    }
}

bool comp (coins x, coins y)
{
    if (x.c < y.c) return 1;
    if (x.c == y.c)
    {
        if (x.b >= y.b) return 1;
    }
    else return 0;
}

void solve ()
{
    input(); sort(arr, arr+n, comp);
    for (int i = 0; i < n; i++)
    {
        if (m >= arr[i].c) m += arr[i].a;
    }
    cout << m;
}

int main()
{
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("COINS.INP","r",stdin);
    freopen("COINS.OUT","w",stdout);
    solve();
    return 0;
}
