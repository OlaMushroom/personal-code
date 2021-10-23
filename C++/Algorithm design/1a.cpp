#include <iostream>
#include <cmath>

using namespace std;

double bai1a (int n)
{
    double S = 0;
    int i = 1;
    while (i <= n)
    {
        S = S + sqrt((double)i);
        i = i + 1;
    }
    return S;
}


int main()
{
    int n;
    cin>>n;
    double x = bai1a(n);
    cout<<x;
    return 0;
}
