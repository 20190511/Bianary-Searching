"""
A30. 가사 탐색 : 피드백
  1. ?? 를 aa 에서 zz 로 바꾸어서 찾으려는 문자열이 있는지
    bisect_left/right(값의 차) 를 이용해서 구하는 방식 이용.
  1-1. 해당 방식으로 풀기 위하여 배열값을 정배열/역배열을 준비해놓고
    ?(와일드카드) 가 앞(역배열)에있는지 뒤(정배열)에 있는지 확인해서 풀면된다.

  1-2. 이진탐색방식으로 선형적으로 풀려해봤으나 시간초과 떴음.


  알게된 문법:
  1. 문자열을 역으로 출력하고 싶다면
    a = a[::-1]
"""


from bisect import bisect_left, bisect_right
array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]

def count_array(arr, left, right):
    left_index = bisect_left(arr,left)
    right_index = bisect_right(arr,right)
    return right_index-left_index


def solution(words, queries):
    result = []
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
    for q in queries:
        res = 0
        if q[0] == "?":
            res = count_array(reverse_array[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z"))
        else:
            res = count_array(array[len(q)], q.replace("?","a"),q.replace("?","z"))
        result.append(res)
    return result
"""
def binary(querie):
    start = 0
    end = len(querie)-1
    pos = ""
    if querie[start] == "?":
        pos = "L"
        if querie[end] == "?":
            return ("A",len(querie))
    else:
        pos = "R"
    
    
    count = 0
    while start<=end:
        mid = (start+end)//2
        if pos == "L":
            if (querie[mid] == "?" and querie[mid+1] != "?"):
                count = mid+1
                break
            elif querie[mid] != "?":
                end = mid-1
            else:
                start = mid+1
        else:
            if (querie[mid] == "?" and querie[mid-1] != "?"):
                count = len(querie) - mid
                break
            elif querie[mid] != "?":
                start = mid+1
            else:
                end = mid-1
    return (pos, count)
               
def check(word, querie, pos, count):
    actual_count = len(querie)-count
    bools = True
    if actual_count == 0:
        return True
    
    if pos == "R":
        for i in range(actual_count):
            if word[i] != querie[i]:
                bools = False
    else:
        for i in range(actual_count):
            if word[len(word)-i-1] != querie[len(querie)-i-1]:
                bools = False
    return bools
            
                
def solution(words, queries):
    result = [0]*len(queries)
    for i in range(len(queries)):
        len_querie = len(queries[i])
        pos,count = binary(queries[i])
        for word in words:
            len_word = len(word)
            if len_word == len_querie:
                if pos == "A":
                    result[i] += 1
                else:
                    if check(word,queries[i],pos,count):
                        result[i] += 1
    return result
  """

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["?????", "fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))