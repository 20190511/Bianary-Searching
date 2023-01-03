"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""


n = int(input())
s = list(map(int, input().split()))

def binary(s, start, end):
  if start > end:
    return None
  mid = (start+end)//2
  if s[mid] == mid:
    return mid
  elif s[mid] < mid:
    return binary(s,mid+1, end)
  else:
    return binary(s,start, mid-1)


result = binary(s, 0, n-1)
if result == None:
  print(-1)
else:
  print(result)