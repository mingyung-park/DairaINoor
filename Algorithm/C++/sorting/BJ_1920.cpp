#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binary_search(vector<int> &v, int target)
{
    int low = 0;
    int high = v.size() - 1;
    int mid;

    while (low <= high)
    {
        mid = low + (high - low) / 2;

        if (v[mid] == target)
        {
            return 1;
        }
        else if (v[mid] < target)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }

    return 0;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    
    int n, m;
    int temp;
    vector<int> v;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin>>temp;
        v.push_back(temp);
    }
    sort(v.begin(), v.end());

    cin >> m;
    for (int i = 0; i < m; i++)
    {
        cin>>temp;
        cout<<binary_search(v,temp)<<"\n";
    }
}