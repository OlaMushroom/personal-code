#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int baitap (int n)
{
    int i = 1;
    int S = 0;
    while (i <= n)
    {
        if (n % i == 0)
        {
            if (i % 2 == 0)
            {
                S += i;
            }
        }
        i++;
    }
    return S;
}

int main()
{
    freopen("TASK39.INP","r",stdin);
    freopen("TASK39.OUT","w",stdout);
    int n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
