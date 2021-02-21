#include<bits/stdc++.h>
using namespace std;
long long int num_of_zeros(int n)
{ long l count = 0;
 
    // Keep dividing n by powers of 
    // 5 and update count
    for (int i = 5; n / i >= 1; i *= 5)
        count += n / i;
 
    return count;

}
int main()
{
	int t;
	 cin>>t;
	 while(t--)
	 { int n;
		 cin>> n;
		 cout<<num_of_zeros(n)<<"\n";
	 }
	return 0;

}