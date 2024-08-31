# input: array = [4, 2, 3, 1]
# output: ans = [-1, 4, 4, 3]

# Next grater of 4  from left => (None) means -1 
# Next grater of 2  from left  => 4
# Next greater of 3 from left => 4 
# Next greater of 1  from left => 3

def nearest_greater_to_left(array):
    ans = []
    stack = []
    n = len(array)
    for i in range(n):
        if len(stack) == 0:
            ans.append(-1)
        elif len(stack) > 0 and stack[-1] > array[i]:
            ans.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= array[i]:
            while len(stack) > 0 and stack[-1] <= array[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
        stack.append(array[i])
    return ans 

array = [4,2,3,1]
array2 = [1,3,2,4]
print(nearest_greater_to_left(array))
print(nearest_greater_to_left(array2))