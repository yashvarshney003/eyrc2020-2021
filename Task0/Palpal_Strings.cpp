#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int T;
	cin>>T;
	while(T--)
	{
	    string S;
	    unordered_map<char,int> M; 
	    cin>>S;
	    for(int i=0;i<S.length();i++)
	    {
	        if(M.find(S[i])!=M.end())
	        M[S[i]]++;
	        else
	        M[S[i]]=1;
	    }
	    int pa=0,ind=0;
	    for(auto x: M)
	    {
	        pa+=x.second/2;
	        ind+=x.second%2;
	    }
	    if(pa>=ind)
	    cout<<"YES"<<endl;
	    else
	    cout<<"NO"<<endl;
	}
	return 0;
}

