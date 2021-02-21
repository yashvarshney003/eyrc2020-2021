#include<bits/stdc++.h>
using namespace std;
 int main()
 {
	  int t;
	   cin>>t;
	   while (t--)

	   {
		    int n;
			map <int ,int> val;
			cin>>n;
			int arr[n];
			for(int i =0 ;i<n ;i++)
			{
			cin>>arr[i];
			val[i] = arr[i];
			}
			int k;
			cin>>k;
			sort(arr,arr+n);
			int value = val[k-1];
			for( int i =0;i<n;i++)
			{
				if(arr[i] == value)
				{
					cout<<i+1<<"\n";
					break;
				}
			}


		   
	   }
	   
	 return 0;
 }