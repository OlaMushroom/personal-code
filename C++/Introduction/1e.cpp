#include <iostream>
#include <cmath>

using namespace std;

int bai1e (int n)
{
    int S = 1;
    while (n > 1)
    {
        S = S * n;
        n -= 2;
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
