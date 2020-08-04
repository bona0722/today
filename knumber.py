def solution(array, commands):
    answer = []
    temp = []
    i, j = 0,1
    for arr in commands:
        k = arr[2]
        temp = array[arr[i]-1: arr[j]]
        temp.sort()
        answer.append(temp[k-1])

    return answer

    # return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
    # lambda를 이용하여 코드 두 줄로 끝낼 수 있다.