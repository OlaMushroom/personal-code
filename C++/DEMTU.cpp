#include <bits/stdc++.h>
//#define arrMAX

using namespace std;

string s;

int solve(string s)
{
    int i = 0, cnt = 0, l = s.size();
    if (l == 0) return 0;
    while (s[i] == ' ') i++;
    for (i; i < l; i++)
    {
        if (s[i] == ' ' && s[i + 1] != ' ') cnt++;
    }
    if (s[l - 1] == ' ') cnt--;
    return cnt + 1;
}

int main()
{
    freopen("DEMTU.INP","r",stdin);
    freopen("DEMTU.OUT","w",stdout);
    while (getline(cin, s)) cout << solve(s) << endl;
    return 0;
}
