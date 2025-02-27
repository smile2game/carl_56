import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 出现频率高于k 就添加到 res中
        堆是一棵完全二叉树，树中每个结点的值都不小于（或不大于）其左右孩子的值。
        优先队列 >> 小顶堆 >> 头顶是最小的,弹出去,维护最大的在队列里
        
        堆中加入的是 元组，排序的方式是按照freq
        """
        #O(n)
        cnt_map = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            cnt_map[nums[i]] = cnt_map.get(nums[i], 0) + 1
        print(f"cnt_map is {cnt_map}")
        
        #O(m * logk) = O(n*logk) headq.headpush/headpop是O(n)
        #使用小顶堆而不是 直接对values()排序
        pri_que = []
        for key,freq in cnt_map.items():
            heapq.heappush(pri_que,(freq,key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
            print(f"pri_que is {pri_que}")

        O(k) = O(1)
        res = [0] * k
        for i in range(k-1,-1,-1): #倒着写入
            res[i] = heapq.heappop(pri_que)[1] #
        return res
        
