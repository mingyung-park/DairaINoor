#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
using namespace std;
bool compare(pair<int, int>a,pair<int,int>b){
    return a.first<=b.first && a.second<= b.second;
}
int main(void){
    int n;
    int a,b;
    vector<pair<int,int>> v;
    cin>>n;
    for(int i = 0; i<n;i++){
        cin>> a >> b;
        v.push_back(make_pair(a,b));
    }
    sort(v.begin(),v.end(),compare);
    for(int i = 0; i<n;i++){
        cout<<v[i].first<<" "<<v[i].second<<endl;
    }
}