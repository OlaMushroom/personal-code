#include <iostream>
#include <cmath>

using namespace std;

int bai9d (int n)
{
    int i = 0;
    int x = 0;
    int y = n % 10;
    while (n != 0)
    {
        x = n % 10;
        if (i < abs(x - y))
        {
            i = abs(x - y);
        }
        y = x;
        n /= 10;
    }
    return i;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9d(n);
    cout<<a;
    return 0;
}
