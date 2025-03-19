def qs(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x<pivot]
    mid = [x for x in nums if x==pivot]
    right = [x for x in nums if x>pivot]
    return qs(left) + mid + qs(right)

if __name__=="__main__":
    nums = [3,6,8,10,1,2,1,1]
    sorted_nums = qs(nums)
    print(f"sorted_nums is {sorted_nums}")
