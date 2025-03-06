# def bit_sum(x):
#     s = 0
#     while x:
#         m, x = divmod(x, 10)  # 这里改为 divmod(x, 10)
#         s += m
#     print(f"s is {s}")
#     return s

# t = bit_sum(25)

#商 余数
import pdb 

def bit_sum(x):
    print("进入函数")
    s = 0
    while x:
        # x, m = divmod(x, 10)  # 这里改为 divmod(x, 10) #用商 divmod >> 商。。。余数
        m = x%10
        x = x//10
        print(f"x is {x},m is {m}")
        s += m #加余数 
    print(f"s is {s}")
    return s


s = bit_sum(25)
print(f"s is {s}")