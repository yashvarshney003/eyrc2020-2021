#include <bits/stdc++.h>
using namespace std;

int main() 
{
	 int t;
	 cin>>t;
	 while(t--)
	 {
		  int n,flag = 0;
		  cin>>n ;
		  int arr[n];
		  for ( int i = 0; i<n ;i++)
		  cin>>arr[i];
		  for( int i =0 ;i<n-1;i++)
		  {
			  if(arr[i] < arr[i+1])
			  {
				  
				  flag = 1;
			  }
		  }
		  if(flag==1)
		  cout<<"yes"<<"\n";
		  else
		  cout<<"no"<<"\n";

	 }
	 return 0;
}