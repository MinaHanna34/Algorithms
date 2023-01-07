'''
name: Mina Hanna
studentID: 028157348

assignment:PA3 qickfind
'''
import sys
class Solution:

	def pa3 (self, arr: list[int], k: int )	-> int:

		kthsmallest = self.kthsmallest
		retval = self.kthsmallest
		print(arr, k)
		return self.kthsmallest(arr,k) # we returned the kthsmallest to get the smallest value
	def partition(array, arr,low, high):
		i = low - 1
		pivot = arr[high]
		for x in range(low, high): # The loop goes through the list until i the low is <= to the pivot
			if arr[x] <= pivot:
				i = i + 1
				(arr[i], arr[x]) = (arr[x], arr[i]) # we swap the i and the x
		(arr[i + 1], arr[high]) = (arr[high], arr[i + 1]) #we will swap the pivot and the highest element of i
		return i + 1 # return it when it is done
	def kthsmallest(self,arr: list, k:int):

		q = self.partition(arr, 0,len(arr)-1)
		if (q==k-1): # if the partition funcation is 0 then it will return
			return arr[q]
		if (q>k-1): #if q is bigger then 0 then it will return the kthsmallest
			return self.kthsmallest(arr[0:q],k)# we start at 0 of the array then go to q
		return self.kthsmallest(arr[q+1:len(arr)], k-q-1)# we add 1 to q then see the length of the array. We then make q the smallest element
if __name__ == '__main__':
	arr = []
	arrtemp = sys.argv[1].split(",")
	for item in arrtemp:
		arr.append(int(item))

	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)

