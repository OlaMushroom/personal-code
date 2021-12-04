#include <cstdio>
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double baitap (int n)
{
    n = abs(n);
    int i = 0;
    double S = 0;
    int m = 0;
    while (n != 0)
    {
        m = n % 10;
        if (m != 0)
        {
            S += m;
            i++;
        }
        n /= 10;
    }
    S /= i;
    return S;
}

int main()
{
    freopen("TASK36.INP","r",stdin);
    freopen("TASK36.OUT","w",stdout);
    int n;
    cin>>n;
    double a = baitap(n);
    cout<<setprecision(2)<<fixed<<a;
    return 0;
}
