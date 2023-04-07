#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        current = head
        next = head.next

        while next != None:
            if current.val == next.val:
                current.next = next.next # 次の次に行く
                next = next.next
            else:
                current = current.next
                next = next.next

        return head
# @lc code=end

