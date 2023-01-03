"""
p. 367
A 27. 정렬된 배열에서 특정 수 개수 구하기 : log(n) 조건
첫째줄에 배열요소개수 N 과 특정 값 x가 주어지고
둘째줄에 배열이 주어질 때,
배열 안의 x의 개수를 구하여라 단, log(n) 이 넘어가면 시간초과

7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3

7 2
2 2 2 2 2 2 3

7 2 
1 2 2 2 2 2 2


<<피드백>>
  1. 이런 가장작은 인덱스, 가장 큰 인덱스 값을 구하는 문제는,
  각각의 조건들을 모두 이진탐색기법으로 풀면 편하다.
  -> 가장 작은 인덱스값 이진탐색 1번, 가장 큰 인덱스값 이진탐색 1번씩 시행하여 푼다.

  2. first, final 모두 값이 같아서 값들을 줄여줄 때, start값을 바꾸면된다.
  2-1. [풀이집] 상관없이 mid 값으로 표현해도된다.!
"""
n,x = map(int, input().split())
strs = list(map(int, input().split()))


def first (strs, target, start, end):
  if start>end:
    return
  mid = (start+end)//2
  if (mid==0 or strs[mid-1]<strs[target]) and strs[mid]==strs[target]:
    return mid
  elif strs[mid] >= strs[target]:
    return first(strs,target,start,mid-1)
  elif strs[mid] < strs[target]:
    return first(strs,target,mid+1,end)
  """
  else:
    return first(strs,target,start-2,end)
  """

def final (strs,target,start,end):
  if start>end:
    return
  mid = (start+end)//2
  if (mid==end or strs[mid+1]>strs[target]) and strs[mid]==strs[target]:
    return mid
  elif strs[mid] > strs[target]:
    return final(strs, target, start, mid-1)
  elif strs[mid] <= strs[target]:
    return final(strs, target, mid+1, end)
  """
  else:
    return final (strs, target, start+2, end)
  """

small = first(strs,x, 0, n-1)
if small == -1:
  print(-1)
else:
  big = final(strs,x,0,n-1)
  print(big-small+1)

    
