"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

"""
from ListNode import ListNode
from ListNode import PrintNode
from ListNode import CreatListNode


"""方法一：递归"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        head.next = self.removeElements(head.next,val)
        if head.val == val:
            return head.next
        else:
            return head


"""方法二：迭代"""
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newhead = ListNode(0)
        newhead.next = head
        cur = newhead
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return newhead.next



if __name__ == '__main__':
    s = Solution()
    nums = [1,2,6,3,4,5,6]
    val = 6
    head = CreatListNode(nums)
    PrintNode(s.removeElements(head, val))

