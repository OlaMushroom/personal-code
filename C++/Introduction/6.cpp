#include <iostream>
#include <cmath>

using namespace std;

int bai6 (int n)
{
    int F1 = 1;
    int F2 = 1;
    int F = 1;
    int i = 3;
    while (i <= n)
    {
        F = F1 + F2;
        F1 = F2;
        F2 = F;
        i++;
    }
    return F;
}

int main()
{
    int n;
    cin>>n;
    int a = bai6(n);
    cout<<a;
    return 0;
}
