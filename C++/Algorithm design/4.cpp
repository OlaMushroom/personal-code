#include <iostream>
#include <cmath>

using namespace std;

int bai4 (int n)
{
    double S = 0;
    int x = 0;
    while (S < n)
    {
        x++;
        S = S + sqrt(x);
    }
    return x;
}

int main()
{
    int n;
    cin>>n;
    int a = bai4(n);
    cout<<a;
    return 0;
}
