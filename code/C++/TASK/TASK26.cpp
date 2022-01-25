#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long func(long long n)
{
    int i = 0;
    int S = 0;
    int m = 10;
    while (n != 0)
    {
        S = n % 10;
        if (S < m)
        {
            i++;
        }
        m = S;
        n /= 10;
    }
    return i;
}

int main()
{
    freopen("TASK26.INP","r",stdin);
    freopen("TASK26.OUT","w",stdout);
    long long n; cin>>n;
    int a = func(n);
    cout<<a;
    return 0;
}
