#include <iostream>
#include <cmath>

using namespace std;

int bai9f (int n)
{
    int i = 0;
    int S = 0;
    int x = n;
    while (x != 0)
    {
        i = x % 10;
        S = S * 10 + i;
        x /= 10;
    }
    if (S == n)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    int n;
    cin>>n;
    int a = bai9f(n);
    cout<<a;
    return 0;
}
