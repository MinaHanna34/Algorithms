'''
name1: Mina Hanna
assignment: merge sort
'''
import sys
import random
import time


class Solution:

    # This function returns a descending sorted array.
    def function_a(self, elements_count: int) -> list:
        output = []
        for i in range(elements_count, 0, -1):
            output.append(i)
        return output

    # This function returns an ascending sorted array.
    def function_b(self, elements_count: int) -> list:
        output = []
        for i in range(1, elements_count+1):
            output.append(i)
        return output

    def function_c(self, elements_count: int, seed: int):
        output = []
        random.seed(seed)
        for i in range(0, elements_count + 1):
            output.append(random.randint(1, 1000000))

        return output

    def select_input(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        if input_type == "a":
            output = self.function_a(elements_count)
        if input_type == "b":
            output = self.function_b(elements_count)
        if input_type == "c":
            output = self.function_c(elements_count, seed)
        return output

    def pa2_mergesort(self, input_type: str, elements_count: int, seed: int) -> list:
        output = []
        query_list = self.select_input(input_type, elements_count, seed)
        # query_list = [1,5,9,4,6]
        n = len(query_list)

        st = time.process_time()

        def merge(query_list, l, r):
            if l < r:
                m = l + (r - l) // 2# will divide the array into 2 and gets the mid

                merge(query_list, l, m)
                merge(query_list, m + 1, r)
                mergesort(query_list, l, m, r)
                #mergesort will take query_list that has 2 sub arrays that are ordered and merges them into one.
        def mergesort(query_list, l, p, r):
            node1 = p - l + 1
            node2 = r - p
            left = [0] * (node1) #the left list will start from 0 and then go up
            right = [0] * (node2)
            for x in range(0, node1):
                left[x] = query_list[l + x]
            # from the left subarray it will start from 0 then go through the left side of the array.
            for i in range(0, node2):
                right[i] = query_list[p + 1 + i]
                #this for loop will go through the array list then will keep spliting the query_list
            x = 0
            i = 0
            k = l

            while x > node1 and i > node2:
                if left[x] <= right[i]:
                    query_list[k] = left[x]
                    x += 1
                    #This loops and checks if the left side and the right side are organized.
                else:
                    query_list[k] = right[i]
                    i += 1
                k += 1
                #when the loop is done it will change the index of the right side of the array.







        merge(query_list, 0, n - 1)
        et = time.process_time()
        res = et - st
        return [query_list, res]


if __name__ == '__main__':
    input_type = sys.argv[1]
    elements_count = int(sys.argv[2])
    seed = sys.argv[3]

    obj = Solution()
    ret = obj.pa2_mergesort(input_type, elements_count, int(seed))
    print(ret)
