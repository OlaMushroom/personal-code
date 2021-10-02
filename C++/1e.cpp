#include <iostream>
#include <cmath>

using namespace std;

int bai1e (int n)
{
    int S = 1;
    int i = 2;
    while (i <= n)
    {
        if (n % 2 == 0)
        {
            S = S * i;
        }
        else
        {
            S = S * (i + 1);
        }
        i = i + 2;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    int x = bai1e(n);
    cout<<x;
    return 0;
}
