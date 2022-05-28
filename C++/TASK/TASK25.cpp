#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap(long long n)
{
    int i = 0;
    int S = 0;
    int m = 0;
    while (n != 0)
    {
        S = n % 10;
        if (S != 0)
        {
            i++;
            if (i > m)
            {
                m = i;
            }
        }
        else
        {
            i = 0;
        }
        n /= 10;
    }
    return m;
}

int main()
{
    freopen("TASK25.INP","r",stdin);
    freopen("TASK25.OUT","w",stdout);
    long long n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
