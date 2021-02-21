#include<bits/stdc++.h>
using namespace std;

int main()
{
   int n,x,y;
   cin>>n>>x>>y;
   int a[n];
   int b[n];
   for( int i =0;i<n;i++) 
   cin>>a[i];
    for( int i =0;i<n;i++) 
   cin>>b[i];
   int profit = 0;
   int x_count= 0;
   int y_count= 0 ;


   //code
   for ( int i =0 ;i <n;i++)
   {
	   if(x_count < x && y_count <y)
	   {
            if(a[i] >  b[i])
			{
				x_count+=1;
				profit += a[i]; 
				continue;
			}
else if(a[i] == b[i])
{
	if(x-x_count > y - y_count)
	{
		x_count+=1;
				profit += a[i]; 
				continue;
	}
	else{
		y_count +=1;
				 profit += b[i];
				 continue;

	}
	     
}



else{
	y_count +=1;
	profit +=b[i];
	continue;
}
	   }
	   if(x_count == x && y_count < y)
	         {
				 y_count +=1;
				 profit += b[i];
				 continue;
			 }
		if(y_count == y && x_count < x)
	         {
				 x_count +=1;
				 profit += a[i];
				 continue;
			 }
			 cout<<"profit is " <<profit<<"\n";
	  
   }
   cout<<profit;
	return 0;
}