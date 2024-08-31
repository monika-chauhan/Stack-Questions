How to identify the problem is related to stack ?
1. The problem given the array 
2. If we write the brute force approach to solve the problem: 
for i in range(n):
    for j in range(n): 

If the j is dependent on i then we can use stack data structure 
for i in range(n):
    for j in range(0,i) or for j in range(i,0) or for j in range(i,n) or for j in range(n,i)

then 100% sure We have to use the stack.