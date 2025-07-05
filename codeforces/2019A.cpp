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
    vector<int> v(n);
    int mx = -1;
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
        mx = max(mx, v[i]);
    }
    if (n % 2 == 0)
    {
        cout <<mx + (n / 2) << "\n";
        return;
    }
    for (int i = 0; i < n; i++)
    {
        if (v[i] == mx)
        {
            if ((i + 1) % 2 == 1)
            {
                total = max(total, (n / 2) + 1);
            }
            else
            {
                total = max(total, (n / 2));
            }
        }
    }
    cout<<total+mx<<"\n";
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
