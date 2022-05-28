#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long func(long long n)
{
    int i = 0;
    int S = 0;
    int m = 10;
    int x = 0;
    while (n != 0)
    {
        S = n % 10;
        if (S >= m)
        {
            i++;
            if (i > x)
            {
                x = i;
            }
        }
        else
        {
            i = 1;
        }
        m = S;
        n /= 10;
    }
    return x;
}

int main()
{
    freopen("TASK27.INP","r",stdin);
    freopen("TASK27.OUT","w",stdout);
    long long n; cin>>n;
    int a = func(n);
    cout<<a;
    return 0;
}
