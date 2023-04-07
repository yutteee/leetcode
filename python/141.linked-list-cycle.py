#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 連結リストの要素を記録していく
        # 次の要素が記録した配列の中にあった場合、ループは成功する
        # ループが失敗する条件は？
        # 1. head, nextがない時
        # 2. nextが記録した配列の中にない時

        if head == None:
            return False
        
        current = head
        next = head.next

        tmp = []

        while next != None:
            # もしtmpに含まれていたらtrueを返す
            if next in tmp:
                return True
            tmp.append(current)
            current = current.next
            next = next.next

        return False
# @lc code=end

