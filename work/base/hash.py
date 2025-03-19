class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        直接无脑用 {} 就完事了
        但是dict比数组慢占用空间多
        """
        cnt_hash = {} #num:cnt
        for num in nums1:
            cnt_hash[num] = cnt_hash.get(num,0) + 1 
        
        res = set()
        for num in nums2:
            if num in cnt_hash:
                res.add(num)
                del cnt_hash[num]
        return list(res)

