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
    ll total = 0;
    bool flag = false;
    string s = "";
    while (n--)
    {
        char c;
        ll l;
        cin >> c >> l;
        if (total + l <= 100)
        {
            s += string(l, c);
            total += l;
        }
        else
        {
            flag = true;
        }
    }
    if (flag)
    {
        cout << "Too Long" << "\n";
    }
    else
    {
        cout << s << "\n";
    }
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
