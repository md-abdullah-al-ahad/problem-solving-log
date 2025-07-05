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
    cin>>n;
    vector<int>v(n);
    map<int,int>mpp;
    for(int i = 0;i<n;i++){
        cin>>v[i];
        mpp[v[i]]++;
    }
    for(auto it:mpp){
        if(it.second>=3){
            cout<<it.first<<"\n";
            return;
        }
    }
    cout<<-1<<"\n";
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
