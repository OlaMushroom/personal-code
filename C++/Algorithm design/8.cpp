#include <iostream>
#include <cmath>

using namespace std;

int bai8 (int a,int b,int n)
{
    int x = 0;
    int y = 0;
    int S = 0;
    int Z = 0;
    while (x <= n/a)
    {
        y = (n - a*x)/b;
        S = a*x + b*y;
        if (S > Z)
        {
            Z = S;
        }
        x++;
    }
    return Z;
}

int main()
{
    int a;
    int b;
    int n;
    cin>>a>>b>>n;
    int z = bai8(a,b,n);
    cout<<z;
    return 0;
}
