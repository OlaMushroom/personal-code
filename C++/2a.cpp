#include <iostream>
#include <cmath>

using namespace std;

int bai2a (int n, int m)
{
    int S = 0;
    int i = 1;
    int a = 1;
    while (i <= n)
    {
        a = (a * i) % m;
        S = (S + a) % m;
        i = i + 1;
    }
    return S;
}

int main()
{
    int n;
    int m;
    cin>>n>>m;
    int x = bai2a(n, m);
    cout<<x;
    return 0;
}
