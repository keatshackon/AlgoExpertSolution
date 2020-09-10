#my implemetation 0(n^2) | space o(1)

# def smallestDifferences(arr1,arr2):
# 	res = [[0,0]]
# 	k = 100000000
# 	for i in range(len(arr1)):
# 		for j in range(len(arr2)):
# 			if(arr1[i] >= arr2[j]):
# 				if(arr1[i] - arr2[j] < k):
# 					k = arr1[i] - arr2[j]
# 					res.pop(0)
# 					res.append([arr1[i] , arr2[j]])
# 			elif(arr2[j] - arr1[i] < k):
# 				k = arr2[j] - arr1[i]
# 				res.pop(0)
# 				res.append([arr1[i] , arr2[j]])
# 		# print(res)
# 	return res



# o(nlog(n) + mlog(m)) | space o(1)
#my implemetation

# def smallestDifferences(arr1,arr2):
# 	d=100000000;
# 	res = []
# 	arr1.sort();arr2.sort()
# 	i=0;j=0
# 	while(i < len(arr1) and j < len(arr2)):
# 		if(arr1[i] > arr2[j]):
# 			if(arr1[i] - arr2[j] < d ):
# 				d = arr1[i] - arr2[j]
# 				res = [[arr1[i],arr2[j]]]
# 			i+=1
# 		elif(arr1[i] < arr2[j]):
# 			if(arr2[j] - arr1[i] < d):
# 				d = arr2[j] - arr1[i]
# 				res = [[arr1[i],arr2[j]]]
# 			j+=1
# 		else:
# 			return res[[arr1[i],arr2[j]]]

# 	return res



def smallestDifferences(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	idxOne = 0
	idxTwo = 0
	smallest = float("inf")
	current = float("inf")
	smallestPair = []
	while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
		firstNum = arrayOne[idxOne]
		secondNum = arrayTwo[idxTwo]
		if firstNum < secondNum:
			current = secondNum - firstNum
			idxOne += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			idxTwo += 1
		else:
			return [firstNum, secondNum]
		if smallest > current:
			smallest = current
			smallestPair = [firstNum, secondNum]
	return smallestPair


if __name__ == "__main__":
	print(smallestDifferences([-100,23,223,13],[20,-101,300,5032]))


