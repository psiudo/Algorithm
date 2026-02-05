N = int(input())
raw_lst = []
for _ in range(N) :
    raw_lst.append(int(input()))
####################################################
def mergesort(s_idx, e_idx, lst) :
    # # 기저 리스트
    # if e_idx - s_idx <= 1 :
    #     return lst
    """
    이렇게 하면 반환할 곳이 없는 첫 호출에서
    정렬하지 않고 반환한다.
    항상, 첫호출 - 중간 호출 - 마지막 호출을 모두 정상 작동하는지 생각하자
    """
    if len(lst) == 1 :
        return lst


    l, m, r = 0, len(lst)//2 , len(lst)
    # l부터 m-1까지 / m부터 r까지 : 홀수개라면 마지막 r인덱스가 남는다.
    lst1 = mergesort(l, m, lst[l:m])
    lst2 = mergesort(m, r, lst[m:r])

    up_lst = [] # 위로 반환해 줄 리스트

    left_lst_ptr, right_lst_ptr = 0, 0
    while left_lst_ptr <= m-1 and right_lst_ptr <= r-m-1 :
        if lst1[left_lst_ptr] <= lst2[right_lst_ptr] :
            up_lst.append(lst1[left_lst_ptr])
            left_lst_ptr += 1
        else :
            up_lst.append(lst2[right_lst_ptr])
            right_lst_ptr += 1

    if left_lst_ptr >= right_lst_ptr :
        up_lst = up_lst + lst2[right_lst_ptr:]
    elif left_lst_ptr <= right_lst_ptr :
        # up_lst + lst1[left_lst_ptr:] 연산했으면 반환하기!!!!!!!!!
        up_lst = up_lst + lst1[left_lst_ptr:]

    return up_lst

ans = mergesort(0, len(raw_lst)-1, raw_lst)
for i in range(N) :
    print(ans[i])
