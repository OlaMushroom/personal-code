#include <bits/stdc++.h>

using namespace std;

long long a[1000000], b[1000000], n;

void input ()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int j = 0; j < n; j++)
    {
        cin >> b[j];
    }
}

void feed ()
{
    sort(a, a+n); sort(b, b+n);
    long long S = 0;
    for (int i = 0; i < n; i++)
    {
        S += (a[i] * b[i]);
    }
    cout << S;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    freopen("FEED.INP","r",stdin);
    freopen("FEED.OUT","w",stdout);
    input(); feed();
    return 0;
}
