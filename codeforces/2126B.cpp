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


bool cmp(const tuple<ll, ll, ll>& a, const tuple<ll, ll, ll>& b) {
    return get<0>(a) < get<0>(b);
}


void solve()
{
    ll n,k;
    cin>>n>>k;
    vector<tuple<ll, ll, ll>> v(n);
    for(int i = 0;i<n;i++){
        ll l,r,x;
        cin>>l>>r>>x;
        v[i] = make_tuple(l,r,x);
    }
    priority_queue<ll>pq;
    ll i = 0;
    
    while (true) {
        ll best_x = -1;
        while (i < n && get<0>(v[i]) <= k) {
            if (get<2>(v[i]) > k) {
                best_x = max(best_x, get<2>(v[i]));
            }
            i++;
        }
        if (best_x == -1) break;
        k = best_x;
    }

    cout << k << "\n";
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
