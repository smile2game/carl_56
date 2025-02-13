import sys
n = int(input())
data = [0] * n
for i in range(n):
    data[i] = int(input())
# print(data)


presum = [0] * n
presum[0] = data[0]
for i in range(1,n):
    presum[i] = data[i] + presum[i-1]

# print(f"presum is {presum}")
    
for line in sys.stdin:
    a,b = map(int,line.strip().split())
    # print(f"a is {a},b is {b}")
    if a == 0:
        print(presum[b])
    else:
        print(presum[b]-presum[a-1])