#include <iostream>
#include <cmath>

using namespace std;

int bai2b (int n, int m, int k)
{
    int S = 1;
    int i = 1;
    int a = 1;
    while (i <= n)
    {
        a = (a * k) % m;
        S = (S + a) % m;
        i = i + 1;
    }
    return S;
}

int main()
{
    int n;
    int m;
    int k;
    cin>>n>>m>>k;
    int x = bai2b(n, m, k);
    cout<<x;
    return 0;
}
