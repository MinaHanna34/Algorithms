'''
Please use the code template below to complete your assignment.
Your code must go under pa1 method. 
Do not change any other code. 
The evaluation code uses this templete to run your test cases.
Any changes other than pa1 method would cause the evaluation method 
stop working and you will not get credit for your submission.

name: Mina Hanna
studentID: 028157348

assignment:PA1
'''
import sys
class Solution:
    def pa1 (self, s: str )	-> bool:
      sys = []
      for a in s:
          if a in ['{', '(', "["]:
              sys.append(a)

          elif a == '}' and len(sys) != 0 and sys[-1] == '{':
              sys.pop()
          elif a == ')' and len(sys) != 0 and sys[-1] == '(':
              sys.pop()
          elif a == ']' and len(sys) != 0 and sys[-1] == '[':
              sys.pop()

          else:
              return False
      return sys == []



if __name__ == '__main__':
	s = sys.argv[1]
	obj = Solution()
	ret = obj.pa1(s)
	print(ret)
