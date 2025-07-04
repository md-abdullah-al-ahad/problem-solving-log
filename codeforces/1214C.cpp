#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<ll, ll> pi;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define endl "\n";
#define yes cout << "Yes" << endl;
#define no cout << "No" << endl;
#define rep(i, a, b) for (ll i = a; i < b; i++)

void solve()
{
    int n;
    cin >> n;
    string s;
    cin >> s;
    int total = 0;
    int opening = 0;
    int closing = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '(')
        {
            total++;
        }
        else
        {
            total--;
        }
        if (total < -1)
        {
            no;
            return;
        }
    }
    if (total != 0)
    {
        no;
        return;
    }
    yes;
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t(1);
    // cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
