# time complexity o(n^2) and space complexity o(1)
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    dic = {}
    for i in range(len(array)):
        if array[i] in dic:
            return [dic[array[i]], i]
        else:
            dic[targetSum-array[i]] = i
        print(dic)
    return []



# O(nlog(n)) | O(1) space
# def twoNumberSum(array, targetSum):
#     array.sort()
#     left = 0
#     right = len(array) - 1
#     while left < right:
#         currentSum = array[left] + array[right]
#         if currentSum == targetSum:
#             return [array[left], array[right]]
#         elif currentSum < targetSum:
#             left += 1
#         elif currentSum > targetSum:
#             right -= 1
#     return []


if __name__ == "__main__":
    print(twoNumberSum([12,23,4,5,65,6,7,3],15))
