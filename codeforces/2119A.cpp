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
    int a,b,x,y;
    cin>>a>>b>>x>>y;
    if(a==b+1 && a%2==1){
        cout<<y<<"\n";
        return;
    }
    if(a>b){
        cout<<-1<<"\n";
        return;
    }
    int total = 0;
    for(int i = a;i<b;i++){
        if(i%2==0){
            total += min(x,y);
        }
        else{
            total+=x;
        }
    }
    cout<<total<<"\n";
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
