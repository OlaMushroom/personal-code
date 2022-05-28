#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap (long long n)
{
    n = abs(n);
    long long i = 0;
    if (n % 2 == 0)
    {
        i = n / 2;
    }
    else
    {
        i = (n + 1) / 2;
    }
    return i;
}

int main()
{
    freopen("TASK41.INP","r",stdin);
    freopen("TASK41.OUT","w",stdout);
    long long n;
    cin>>n;
    long long a = baitap(n);
    cout<<a;
    return 0;
}
