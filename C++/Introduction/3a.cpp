#include <iostream>
#include <cmath>

using namespace std;

double bai3a (int n, double x)
{
    double S = 0;
    int i = 1;
    int m = 1;
    double a = 1;
    while (i <= n)
    {
        m *= i;
        a *= x;
        if (i % 2 == 0)
        {
            S = S - a/(double)m;
        }
        else
        {
            S = S + a/(double)m;
        }
        i++;
    }
    return S;
}

int main()
{
    int n; double x;
    cin>>n>>x;
    double z = bai3a(n,x);
    cout<<z;
    return 0;
}
