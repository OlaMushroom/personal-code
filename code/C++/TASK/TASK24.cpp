#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long func(long long n)
{
    int i = 0;
    int S = 0;
    int m = n % 10;
    while (n != 0)
    {
        S = n % 10;
        if (S != 0 && m == 0)
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
    freopen("TASK24.INP","r",stdin);
    freopen("TASK24.OUT","w",stdout);
    long long n; cin>>n;
    int a = func(n);
    cout<<a;
    return 0;
}
