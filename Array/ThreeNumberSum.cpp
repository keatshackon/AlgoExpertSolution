#include<bits/stdc++.h>
using namespace std;
typedef long long ll;;

// o(n^2) | s(1)
vector<ll> ThreeSum(vector<ll> v,int target){

	sort(v.begin(), v.end());
	
	for(int i = 0;i < v.size()-2;i++){
		int j = i+1;
		int k = v.size()-1;
		while(j < v.size()){
			if((v[i]+v[j]+v[k]) == target){
				return  { v[i],v[j],v[k] };
			}else if((v[i]+v[j]+v[k]) > target){
				k--;
			}else{
				j++;
			}
		}
	}
	return {-100,-100,-100};
}


int main(){


	vector<ll> v = {12,3,1,2,-6,5,-8,6};
	ll t = 0;

	vector<ll> res = ThreeSum(v,t);
	cout<<res[0]<<" "<<res[1]<<" "<<res[2];
	return 0;

}



