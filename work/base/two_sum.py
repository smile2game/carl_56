class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        O(n) 走一圈是必须的
        但是, find target - x : O(n) >> O(1) ,要用hashtable才能实现这个优化
        """
        hashtable = dict() # hashtable[value] = index
        for index,value in enumerate(nums):
            if target - value in hashtable: #这里是查询他的key
                return [hashtable[target - value],index]
            else:
                hashtable[value] = index
        return []