"""
 A29. 공유기 설치 (백준 2110번)
 https://www.acmicpc.net/problem/2110

<피드백>
  1. N개수가 터무니없이 크다면 이분탐색 의심해보기.
  2. 해당 문제는 공유기의 최대길이를 기준으로 가장왼쪽부터 공유기를 세워보면서
    최대 몇 개 까지 공유기를 세울 수 있는지 판단하여 풀 수 있다.
      A. 공유기를 세워보니 세울 수 있는 공유기 수가 c보다 크다 -> 범위를 (최대크기) mid+1 만큼 키워서 재탐색
      B. 공유기를 세워보니 세울 수 있는 공유기 수가 c보다 작다 -> 범위를 (최대크기) mid-1 만큼 좁혀서 재탐색
 
7 4
1 
4 
7 
18 
29 
38 
49

4 3
1
3
5
7
"""
n, c = map(int, input().split())
path = []
for i in range(n):
  path.append(int(input()))
path.sort() #NlogN

end = path[n-1] - path[0]
start = 1
result = start
while start <= end:
  mid = (start+end)//2
  value = path[0]
  count = 1

  for i in range(1, n):
    if path[i]-value >= mid:
      count += 1
      value = path[i]
      
  if count >= c:
    start = mid+1
    result = mid
  else:
    end = mid-1

print(result)