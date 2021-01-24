#include<bits/stdc++.h>
using namespace std;

typedef long long ll;


void moveElement(vector<ll> &v,int t){

	int i = 0;
	int j = v.size()-1;;
	while(i<j){
		while(v[i] != t && i<v.size()){
			i++;
		}
		while(v[j] == t && j>=0){
			j--;
		}
		if(v[i] == t && v[j] != t){
			swap(v[i],v[j]);
		}
		i++;
		j--;
		
	}

}

int main(){
	ll t;
	std::vector<ll> v= {2,24,33,54,5,46,6};
	t = 100;
	moveElement(v,t);

	for(auto q:v){
		cout<<q<<" ";
	}
	return 0;

}


