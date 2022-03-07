#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

long long func (long long n, long long a, long long b)
{
    long long x = a;
    long long y = b;
    while (y != 0)
    {
        long long z = x % y;
        x = y; y = z;
    }
    long long i = n / (a * b / x);
    return i;
}

int main()
{
    freopen("TASK60.INP","r",stdin);
    freopen("TASK60.OUT","w",stdout);
    long long n; long long a; long long b;
    cin>>n>>a>>b;
    long long out = func(n,a,b);
    cout<<out;
    return 0;
}
