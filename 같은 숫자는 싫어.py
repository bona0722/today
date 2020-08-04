def solution(arr):
    answer = [] 
    n, p = 0, 1
    while(p <= len(arr)-1):
        if(arr[n] != arr[p]):
            answer.append(arr[n])
        n += 1
        p += 1

    answer.append(arr[len(arr)-1]) 
    return answer

    # def solution(arr):
    #     a = []
    # for i in arr:
    #     if a[-1:] == [i]: continue 
    # 마지막 숫자가 [i]와 같으면 코드를 건너뛰기 건너뛰는건 continue 이용!
    #     a.append(i)
    # return a