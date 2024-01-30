"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseSublist(self, head):

        # take the head (first node) of a k group, reverse the group
        # return the new head and the tail of the group
        tail = head
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev, tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # define edge case
        if k == 1:
            return head

        # initialization:
        # prev_tail: dummy; k_head: head
        dummy = ListNode([0])
        prev_tail = dummy
        k_head = head
        # enum and start of traversal
        enum = 1
        curr = head

        while enum < k and curr:
            # traverse k nodes
            curr = curr.next
            enum += 1
            # when we get k nodes
            if enum == k:
                if curr:
                    # mark nxt_head
                    nxt_head = curr.next
                    # break the k group
                    curr.next = None
                    # reverse the k group and get the k_head and k_tail
                    k_head, k_tail = self.reverseSublist(k_head)
                    # link k_head to prev_tail
                    prev_tail.next = k_head
                    # update prev_tail and k_head
                    prev_tail = k_tail
                    k_head = nxt_head
                    # update new start of the traaversal and enum
                    curr = nxt_head
                    enum = 1
            # when we finish traversal and not reach k
            if not curr:
                # link k_head to prev_tail
                prev_tail.next = k_head

        return dummy.next
