#include <iostream>
#include <cmath>

using namespace std;

int bai9a (int n)
{
    int i = 0;
    while (n != 0)
    {
        n /= 10;
        i++;
    }
    return i;
}

int main()
{
    int n;
    cin>>n;
    int a = bai9a(n);
    cout<<a;
    return 0;
}
