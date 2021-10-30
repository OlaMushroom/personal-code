#include <iostream>
#include <cmath>

using namespace std;

int bai9c (int n)
{
    int i = 0;
    int x = 0;
    int y = n % 10;
    while (n != 0)
    {
        x = n % 10;
        i = i + abs(x - y);
        y = x;
        n /= 10;
    }
    return i;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9c(n);
    cout<<a;
    return 0;
}
