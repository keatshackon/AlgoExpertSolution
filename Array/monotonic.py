

# o(n) | space o(1)
# My Implmention
# def monotonic(arr):
# 	i=1;d=1
# 	t=0;
# 	foo = False
# 	while(t<len(arr)):
# 		if(arr[i] > arr[i+1]):
# 			if(d==1):
# 				pass
# 			else:
# 				return False
# 			i=0
# 			t+=1
# 		elif(arr[i] < arr[i+1]):
# 			if(i==1):
# 				pass
# 			else:
# 				return False
# 			d=0
# 			t+=1
# 		else:
# 			i=1;d=1
# 			t+=1
# 	return True



def breakdir(diff,preInt,curInt):
	if(len(arr)<=2):
		return True
	
	c = curInt- preInt
	if(diff > 0):
		return c<0
	return c>0

def monotonic(arr):
	diff = arr[1] - arr[0]
	for i in range(2,len(arr)):
		if(arr[i] - arr[i-1] == diff):
			diff = arr[i] - arr[i-1]
			continue;
		if(breakdir(diff,arr[i-1],arr[i])):
			return False
	return True





if __name__ == "__main__":
	print(monotonic([-100,100,200,1000,400,500]))