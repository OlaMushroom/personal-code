#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap(long long n)
{
    int i = 0;
    int S = 0;
    while (n != 0)
    {
        S = n % 10;
        if (S == 1 || S == 4 || S == 9)
        {
            i++;
        }
        n /= 10;
    }
    return i;
}

int main()
{
    freopen("TASK23.INP","r",stdin);
    freopen("TASK23.OUT","w",stdout);
    long long n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
