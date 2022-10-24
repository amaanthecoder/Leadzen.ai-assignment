class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def make_list(elements):
    head = ListNode(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = ListNode(element)
    return head


def get_node(head, pos):
    if pos != -1:
        p = 0
        ptr = head
        while p < pos:
            ptr = ptr.next
            p += 1
        return ptr


class Solution:
    def hasCycle(self, head: [ListNode]):
        hare = head
        turtle = head
        while turtle and hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False


elements = list(map(int, input().split()))
head = make_list(elements)
last_node = get_node(head, len(elements) - 1) 
pos = int(input())
last_node.next = get_node(head, pos)
s = Solution()
answer = s.hasCycle(head)
print(answer)
