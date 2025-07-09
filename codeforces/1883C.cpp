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
    int n, k;
    cin >> n >> k;
    int even = 0;
    int ans = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        if (num % 2 == 0)
            even++;
        int fval = ceil(1.0 * num / k);
        fval = k * fval - num;
        ans = min(fval, ans);
    }

    if (k != 4)
    {
        cout << ans << "\n";
        return;
    }

    if (n == 1)
    {
        cout << ans <<"\n";
        return;
    }

    if (even >= 2)
    {
        cout << 0 << "\n";
        return;
    }
    cout << min(ans, 2 - even) << "\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;
    while (t--)
        solve();

    return 0;
}
