#include <iostream>
#include <cmath>

using namespace std;

double bai1c (int n)
{
    double S = 0;
    int i = 1;
    int m = 1;
    while (i <= n)
    {
        m = m * i;
        if (i % 2 == 0)
        {
            S = S - 1.0/m;
        }
        else
        {
            S = S + 1.0/m;
        }
        i = i + 1;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    double x = bai1c(n);
    cout<<x;
    return 0;
}
