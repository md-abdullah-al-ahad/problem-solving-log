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
    deque<pair<ll, ll>> dq;
    while (n--)
    {
        int task;
        cin >> task;
        if (task == 1)
        {
            ll c, x;
            cin >> c >> x;
            dq.push_back({c, x});
        }
        else
        {
            ll k;
            cin >> k;
            ll sum = 0;
            while (k > 0)
            {
                ll f1 = dq.front().first;
                ll f2 = dq.front().second;
                ll t = min(k, f1);
                sum += t * f2;
                dq.front().first -= t;
                k -= t;
                if (dq.front().first == 0)
                {
                    dq.pop_front();
                }
            }
            cout << sum << '\n';
        }
    }
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
