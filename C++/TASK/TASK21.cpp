#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap(long long n)
{
    long long x = 1;
    long long S = 0;
    int m = sqrt(n);
    while (x <= m)
    {
        if (n % x == 0)
        {
            S += x + (n / x);
        }
        x += 1;
    }
    if (m * m == n)
    {
        S -= m;
    }
    return S;
}

int main()
{
    freopen("TASK21.INP","r",stdin);
    freopen("TASK21.OUT","w",stdout);
    long long n;
    cin>>n;
    long long a = baitap(n);
    cout<<a;
    return 0;
}
