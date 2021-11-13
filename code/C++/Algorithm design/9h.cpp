#include <iostream>
#include <cmath>

using namespace std;

int bai9h (int n)
{
    int i = 0;
    int x = 1;
    int m = sqrt(n);
    while (x <= m)
    {
        if (n % x == 0)
        {
            i += 2;
        }
        x += 1;
    }
    if (m * m == n)
    {
        i -= 1;
    }
    return i;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9h(n);
    cout<<a;
    return 0;
}
