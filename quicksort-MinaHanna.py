'''
name1: Mina Hanna
assignment:PA2 quick sort
'''
import sys
import random
import time

class Solution:
	
	#This function returns a descending sorted array.
	def function_a (self, elements_count: int) -> list:
		output = []
		for i in range(elements_count,0, -1):
			output.append(i)
		return output

	#This function returns an ascending sorted array.	
	def function_b (self, elements_count: int) -> list:
		output = []
		for i in range(1, elements_count+1):
			output.append(i)
		return output

	def function_c(self, elements_count: int, seed: int):
		output = []
		random.seed(seed)
		for i in range(0,elements_count+1):
			output.append(random.randint(1,1000000))

		return output


	def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		if input_type == "a":
			output = self.function_a(elements_count)
		if 	input_type == "b":
			output = self.function_b(elements_count)
		if 	input_type == "c":
			output = self.function_c(elements_count, seed)
		return output	

	def pa2_quicksort(self, input_type: str, elements_count: int, seed: int) -> list:
		output = []
		query_list = self.select_input(input_type, elements_count, seed)

		n = len(query_list)
		st = time.process_time()

		def quicksort(query_list,p,r):
			if p < r:
				q = partition(query_list, p, r)#q gets the partition
				quicksort(query_list, p, q - 1)
				quicksort(query_list, q + 1, r)
				#quicksort will organize the list until the poviot is bigger.
		def partition(query_list, p, r):
			x= query_list[r]
			i = p-1
			j=p
			for index in range (j,r-1) :
				#this loop will go through the list then go in a descending order
				if query_list[j] <= x:
					i = i + 1
					query_list[i],query_list[j]= query_list[j],query_list[i] # This will switch the index of the array with p
					query_list[i+1], query_list[r]= query_list[r],query_list[i+1] # this will go through the array until r is in place
			return i +1

		p= random.randrange(0,n-1)
		r= n-1
		quicksort(query_list,p,r)
		et = time.process_time()
		res = et - st

		return [query_list, res]




if __name__ == '__main__':
	input_type = sys.argv[1]
	elements_count = int(sys.argv[2])
	seed = sys.argv[3]

	obj = Solution()
	ret = obj.pa2_quicksort(input_type, elements_count, seed)
	print(ret)

