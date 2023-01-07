'''
name: Mina Hanna
studentID: 028157348

assignment:PA3 minheap
'''
import sys

class Solution:
	def __init__(self):
		self.A= []
		self.i =0
		self.heap_size=0

	def pa3 (self, arr: list[int], k: int )	-> int:


		self.A = arr
		self.heap_size = len(arr)
		self.heapsort(self.heap_size)
		retval = self.A[len(self.A)-k]# we return the array
		print(arr, k)


		return retval




	def buildheap(self):
		self.heap_size= len(self.A)# we set heapsize to the len of the array
		for i in range(self.heap_size//2,-1,-1):# we go through the floored array down to 1
			self.Heapify(self.heap_size,i)
	def left(self, i):
		return 2 * i + 1 # gets the left child index

	def right(self, i):
		return 2 * i + 2 # gets the right side index

	def Heapify(self,heap_size,i):
		l = self.left(i)
		r = self.right(i)
		smallest = i
		if ((l < heap_size) and (self.A[l] <= self.A[i])): # if the left side of the len of the array is smaller and the i
			smallest = l
		if ((r < heap_size) and (self.A[r] <= self.A[smallest])):# if the right side is smaller then the  len of the array and is smaller then the smallest
			smallest = r
		if smallest != i:
			self.A[i], self.A[smallest] = self.A[smallest], self.A[i] # it will i and the smallest
			self.Heapify(heap_size,smallest)



	def heapsort(self,heap_size):
		self.buildheap()
		for i in range(len(self.A)-1,-1,-1): # the length of the array and down to 1
			self.A[0], self.A[i] = self.A[i], self.A[0] # we swap 0 and i off the array
			heap_size -=1 # we go down 1 of the len of the array
			self.Heapify(heap_size, 0)

if __name__ == '__main__':
	arr = []
	arrtemp = sys.argv[1].split(",")
	for item in arrtemp:
		arr.append(int(item))

	k = int(sys.argv[2])
	obj = Solution()
	ret = obj.pa3(arr, k)
	print(ret)