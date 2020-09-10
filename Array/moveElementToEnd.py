

# def moveElementToEnd(arr,n):
# 	i=0
# 	x = len(arr) - arr.count(2)
# 	while(i<x):
# 		if(arr[i] == n):
# 			arr.pop(i)
# 			arr.append(n)
# 		else:
# 			i+=1
# 		# print(arr)
# 		# print(i)

# 	return arr


# o(n)) | spcae o(1)


# def moveElementToEnd(arr,n):
# 	i = 0
# 	j=len(arr)-1 
# 	while(i<j):
# 		if(arr[j]==n):
# 			j-=1
# 		if(arr[i]== n ):
# 			temp = arr[i]
# 			arr[i] = arr[j]
# 			arr[j] = temp
# 			j-=1
# 		elif(arr[i] != n):
# 			i+=1
# 	return arr;

def moveElementToEnd(arr,n):
	i=0;
	j=len(arr)-1
	while(i<j):
		while(i<j and arr[j]==n):
			j-=1
		if(arr[i] == n ):
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
		i+=1

	return arr
if __name__ == "__main__":
	print(moveElementToEnd([2,2,2,24424,44222,2111,21,2,2,2,2],2))
