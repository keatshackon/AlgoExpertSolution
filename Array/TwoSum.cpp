/*
	Find Two Number Whose  Sum Is equal to taget value!
	and number in array don't have  duplicate(distinct array
	element)

*/


#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

// o(nlog(n)) | o(1)
vector<ll> TwoSum2(std::vector<ll> &v,int target){

	sort(v.begin(), v.end());

	int i=0;
	int j = v.size()-1;
	while(i<j){
		if((v[i] + v[j]) == target){
			return {v[i],v[j]};
		}else if((v[i] + v[j]) > target){
			j--;
		}else{
			i++;
		}
	}
	return {-100,-100};
}

// o(n) | s(n)
vector<ll> TwoSum1(std::vector<ll> &v,int target){

	unordered_map<int, int> m;

	for(int i=0;i<v.size();i++){
		if(m.count(v[i]) == 0){
			m[target - v[i]] = 1; 
		}else{
			return {v[i],target-v[i]};
		}
	}
	return {-100,-100};
}

int main(){
	
	vector<ll> v = {3,5,-4,8,11,1,-1,6};
	ll n,q,target;
	target = 10;
	// for(int i = 0;i < n;i++){
	// 	cin>>q;
	// 	v.push_back(q);
	// }
	vector<ll> res =  TwoSum2(v,target);

	cout<<res[0]<<" "<<res[1];

	return 0;


}