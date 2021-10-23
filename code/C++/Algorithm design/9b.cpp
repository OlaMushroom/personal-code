#include <iostream>
#include <cmath>

using namespace std;

int bai9b (int n)
{
    int i = 0;
    int S = 0;
    while (n != 0)
    {
        i = n % 10;
        S = S * 10 + i;
        n /= 10;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9b(n);
    cout<<a;
    return 0;
}
