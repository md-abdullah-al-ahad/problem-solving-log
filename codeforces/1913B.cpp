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
    string s;
    cin >> s;
    int n = s.size();
    if (n == 1)
    {
        cout << 1 << "\n";
        return;
    }
    int one = 0, zero = 0;
    for (int i = 0; i < n; i++)
    {
        if (s[i] == '1')
            one++;
        else
            zero++;
    }
    int total = 0;
    int i = 0;
    while (i < n)
    {
        if (s[i] == '1')
        {
            if (zero == 0)
            {
                break;
            }
            zero--;
            total++;
        }
        else
        {
            if (one == 0)
            {
                break;
            }
            one--;
            total++;
        }
        i++;
    }
    cout << n - total << "\n";
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll t(1);
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
