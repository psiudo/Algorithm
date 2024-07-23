def solution(arr):
    answer=0
    for i in range(len(arr)):
        answer= (answer*i + arr[i])/(i+1)
    return answer

def main():
    arr1 = [1, 2, 3, 4]
    print(f"average: {solution(arr1)}")

    
    arr2 = [5, 5]
    print(f"average: {solution(arr2)}")

if __name__ == "__main__":
    main()