#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<ll, ll> pi;
#define f first
#define s second
#define pb push_back
#define mp make_pair
#define endl "\n"
#define yes cout << "Yes" << endl
#define no cout << "No" << endl
#define rep(i, a, b) for (ll i = a; i < b; i++)

void solve()
{
    int n, s;
    cin >> n >> s;
    vi a(n);
    int total = 0, c0 = 0, c1 = 0, c2 = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        total += a[i];
        if (a[i] == 0)
            c0++;
        if (a[i] == 1)
            c1++;
        if (a[i] == 2)
            c2++;
    }
    if (s - total > 1 || s - total == 0)
    {
        cout << -1 << "\n";
        return;
    }
    vi v;
    for (int i = 0; i < c0; i++)
    {
        v.push_back(0);
    }
    for (int i = 0; i < c2; i++)
    {
        v.push_back(2);
    }
    for (int i = 0; i < c1; i++)
    {
        v.push_back(1);
    }
    for (int i = 0; i < n; i++)
    {
        cout << v[i] << " ";
    }
    cout << "\n";
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t(1);
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
