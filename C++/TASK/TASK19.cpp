#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap(long long n)
{
    int i = 0;
    int x = 1;
    int m = sqrt(n);
    while (x <= m)
    {
        if (n % x == 0)
        {
            i += 2;
        }
        x += 1;
    }
    if (m * m == n)
    {
        i -= 1;
    }
    return i;
}

int main()
{
    freopen("TASK19.INP","r",stdin);
    freopen("TASK19.OUT","w",stdout);
    long long n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
