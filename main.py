
"""
문제 P.201
첫째줄에 떡의 개수 N과 요청한 떡의 길이 M 이 주어진다.
  (1<=N<=1,000,000 , 1<=M<=2,000,000,000)
둘째줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이다.

이때, 떡의 길이를 X만큼 잘라서 남은 길이의 총합이 M이 되게하는 X의 최댓값을 구하여라

<<풀이>>
target : 떡볶이 길이를 이진탐색으로 잡는다!
  (1에서 2씩 커져가는 방식으로..)
시간복잡도 : Nlog(M)

4 6
19 15 10 17

10 63
20 17 5 9 16 17 20 21 26 30
"""

target = 1
n, m = map(int, input().split())
dduk = list(map(int, input().split()))

count = 0
while True:
  count += 1
  sum = 0
  for item in dduk:
    if item - target > 0:
      sum += item - target
  if sum == m:
    break
  elif sum < m:
    target -= 1
  else:
    target *= 2
