

# O(n^2) time | O(n) space
def ThreeNumberSum(arr,target):
	arr.sort()
	# print(arr,target)
	res=[]
	for i in range(len(arr)-2):
		k = arr[i]
		l = i+1
		r = len(arr)-1
		while(l<r):
			if(k+arr[l]+arr[r] == target):
				res.append([k,arr[l],arr[r]])
				l+=1
				r-=1
			elif (target < k+arr[l]+arr[r]):
				r=r-1
			elif(target > k+arr[l]+arr[r]):
				l = l+1
	return res


if __name__ == "__main__":
	print(ThreeNumberSum([-1,2,4,5,7,8,8],18))