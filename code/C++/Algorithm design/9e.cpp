#include <iostream>
#include <cmath>

using namespace std;

int bai9e (int n)
{
    int i = 0;
    int S = -1;
    while (n != 0)
    {
        if (n % 2 == 0)
            {
                i = n % 10;
                if (i > S)
                {
                    S = i;
                }
            }
        n /= 10;
    }
    return S;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9e(n);
    cout<<a;
    return 0;
}
