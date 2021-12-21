#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double baitap (int n)
{
    int i = 0;
    int x = 0;
    double S = 0;
    while (n != 0)
    {
        x = n % 10;
        if (x % 2 == 0)
        {
            S += x;
            i++;
        }
        n /= 10;
    }
    if (S != 0)
    {
        S /= i;
    }
    return S;
}

int main()
{
    freopen("TASK35.INP","r",stdin);
    freopen("TASK35.OUT","w",stdout);
    int n;
    cin>>n;
    double a = baitap(n);
    if (a == 0)
    {
        cout<<"-1";
    }
    else
    {
        cout<<setprecision(2)<<fixed<<a;
    }
    return 0;
}
