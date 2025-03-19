class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        p = head 
        nums = []
        while p:
            nums.append(p.val)
            p = p.next
        nums.sort()
        p = head 
        for x in nums:
            p.val = x
            p = p.next
        return head
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sort_func(head,tail):
            if not head: return head 
            if head.next == tail: 
                head.next = None
                return head
            slow = fast = head #快慢指针
            while fast!=tail:
                slow = slow.next
                fast = fast.next
                if fast != tail: fast  = fast.next
            mid = slow #快指针到达末尾时候，慢指针刚好再中点
            return merge(sort_func(head,mid),sort_func(mid,tail))
        
        def merge(head1,head2):
            dummy_head = ListNode(0)
            cur,tmp1,tmp2 = dummy_head,head1,head2
            while tmp1 and tmp2:
                if tmp1.val <= tmp2.val:
                    cur.next = tmp1
                    tmp1 = tmp1.next
                else:
                    cur.next = tmp2
                    tmp2 = tmp2.next
                cur = cur.next
            if tmp1:
                cur.next = tmp1
            if tmp2:
                cur.next = tmp2
            return dummy_head.next

        return sort_func(head,None)