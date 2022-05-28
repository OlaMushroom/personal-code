#include <iostream>

using namespace std;

double bai1b (int n)
{
    double S = 0;
    int i = 2;
    while (i <= n)
    {
        S = S + (double)(i-1)/i;
        i = i + 1;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    double x = bai1b(n);
    cout<<x;
    return 0;
}
