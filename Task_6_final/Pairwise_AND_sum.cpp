#include<bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	fstream inp("input.txt",ios::in);//input file read karo and double colon ke andar input file ka naam
	fstream out("output.txt",ios::out);// output file me write karo  and double colon ke andar ouput file ka naam.
	int a;
	inp>>a;// variable read kiya
	out<<a<<"\n"; // variable ko out kiya.
	return 0;
}