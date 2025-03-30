N = int(input())                                                                        
arr = []                                                                                
for i in range(N):                                                                      
    arr.append(list(map(int, input().split())))                                         
                                                                                        
result = []                                                                             
result.append(arr[0])                                                                   
for j in range(N - 1):                                                                  
    temp = []                                                                           
    temp.append(min(arr[j + 1][0] + result[j][1], arr[j + 1][0] + result[j][2]))        
    temp.append(min(arr[j + 1][1] + result[j][0], arr[j + 1][1] + result[j][2]))        
    temp.append(min(arr[j + 1][2] + result[j][0], arr[j + 1][2] + result[j][1]))        
    result.append(temp)                                                                 
                                                                                        
print(min(result[-1]))                                                                  
                                                                                        