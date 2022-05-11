class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def CreatListNode(nums):
    head = ListNode(0)
    cur = head
    for i in range(0,len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head.next


def PrintNode(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next