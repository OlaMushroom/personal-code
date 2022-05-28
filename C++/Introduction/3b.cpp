#include <iostream>
#include <cmath>

using namespace std;

double bai3b (int n, double x)
{
    double S = 0;
    int i = 1;
    int m = 1;
    while (i <= n)
    {
        m *= i;
        S = S * x + 1.0/m;
        i++;
    }
    return S;
}

int main()
{
    int n; double x;
    cin>>n>>x;
    double a = bai3b(n,x);
    cout<<a;
    return 0;
}
