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

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["?????", "fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))