#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

long long baitap (long long n)
{
    long long i = 1;
    long long x = 0;
    long long S = 0;
    long long m = sqrt(n);
    while (i <= m)
    {
        if (n % i == 0)
        {
            x = n / i;
            if (i % 2 == 0)
            {
                S += i;
            }
            if (x % 2 == 0)
            {
                S += x;
            }
        }
        i++;
    }
    if (m % 2 == 0)
    {
        if (m * m == n)
        {
            S -= m;
        }
    }
    return S;
}

int main()
{
    freopen("TASK40.INP","r",stdin);
    freopen("TASK40.OUT","w",stdout);
    long long n;
    cin>>n;
    long long a = baitap(n);
    cout<<a;
    return 0;
}

