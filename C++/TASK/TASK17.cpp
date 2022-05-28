#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

long long baitap(long long n)
{
    int i = 0;
    long long S = 0;
    while (n != 0)
    {
        S = n % 10;
        if (S == 2 || S == 3 || S == 5 || S == 7)
        {
            i++;
        }
        n /= 10;
    }
    return i;
}

int main()
{
    freopen("TASK17.INP","r",stdin);
    freopen("TASK17.OUT","w",stdout);
    long long n;
    cin>>n;
    int a = baitap(n);
    cout<<a;
    return 0;
}
