#include <iostream>
#include <cmath>

using namespace std;

int bai7 (int n)
{
    int S = 1;
    int F = 1;
    int i = 2;
    while (i <= n)
    {
        F = S * i;
        S += F;
        i++;
    }
    return F;
}

int main()
{
    int n;
    cin>>n;
    int a = bai7(n);
    cout<<a;
    return 0;
}
