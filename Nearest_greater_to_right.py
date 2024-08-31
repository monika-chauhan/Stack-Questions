# input: arr = [1, 3, 2, 4] 
# output: ans = [3, 4, 4, -1]

# Next grater of 1 => 3 
# Next grater of 3 => 4
# Next greater of 2 => 4 
# Next greater of 4 => (None) means -1

def nearest_greater_to_right(array):
    ans = []
    stack = []
    n = len(array)
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            ans.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            ans.append(stack[-1])
        elif len(stack) > 0 and stack[-1] < array[i]:
            while len(stack) > 0  and stack[-1] <= array[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
     
        stack.append(array[i])
  
        
    return ans[::-1]

array = [1,3,2,4]
print(nearest_greater_to_right(array))

