#include <iostream>
#include <cmath>

using namespace std;

double bai1f (int n)
{
    double S = n;
    int i = n - 1;
    while (i >= 1)
    {
        S = i + 1.0/S;
        i = i - 1;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    double x = bai1f(n);
    cout<<x;
    return 0;
}
