#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, temp;
    cin >> n;
    int iter = n;
    while (iter--)
    {
        cin>>temp;
        
        if(temp<2){
            n--;
            continue;
        }

        for(int i = 2;i<temp;i++){
            if(temp%i==0){
                n--;
                break;
            }
        }
    }
    cout<<n;
}