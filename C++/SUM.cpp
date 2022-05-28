#include <bits/stdc++.h>
#include <vector>
#define arrMAX 10000000

using namespace std;

long long a[arrMAX], b[arrMAX];
long long S;

void solve ()
{
    cin >> S;
    long long i = 0, x = S * 2, y = sqrt(x);
    for (long long n = y; n >= 1; n--)
    {
        long long m = (x - (n * n) + n) / (n * 2);
        if ((x - (n * n) + n) % (n * 2) == 0 && m > 0)
        {
            a[i] = m;
            b[i] = a[i] + n - 1;
            i++;
        }
    }
    cout << i << "\n";
    for (long long j = 0; j < i; j++)
    {
        cout << a[j] << " " << b[j] << "\n";
    }
}

int main()
{
    freopen("SUM.INP","r",stdin);
    freopen("SUM.OUT","w",stdout);
    solve();
    return 0;
}
