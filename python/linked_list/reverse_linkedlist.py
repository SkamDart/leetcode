# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    @staticmethod
    def reverse_iter(node):
        prev = None
        cur = node
        while cur is not None:
            tmp_next = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_next
        return prev

    def reverse_rec(self, node):
      if node is None or node.next is None:
        return node
        
      cur = self.reverse_rec(node.next)
      node.next.next = node
      node.next = None
      return cur
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_iter(head)
