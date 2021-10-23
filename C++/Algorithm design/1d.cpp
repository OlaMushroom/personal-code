#include <iostream>
#include <cmath>

using namespace std;

double bai1d (int n)
{
    double S = 0;
    int i = 1;
    while (i <= n)
    {
        S = sqrt(S + 2.0);
        i = i + 1;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    double x = bai1d(n);
    cout<<x;
    return 0;
}
