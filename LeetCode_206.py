"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""

from ListNode import ListNode
from ListNode import PrintNode
from ListNode import CreatListNode

"""方式一：迭代"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre_node = None
        cur_node = head
        while cur_node is not None:
            tmp = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = tmp
        return pre_node


"""方式二：递归"""
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead


if __name__ == '__main__':
    s = Solution2()
    nums = [1, 2, 6, 3, 4, 5, 6]
    head = CreatListNode(nums)
    PrintNode(s.reverseList(head))
