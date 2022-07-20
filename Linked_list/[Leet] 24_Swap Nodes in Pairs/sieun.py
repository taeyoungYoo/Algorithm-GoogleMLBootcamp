# 시은 풀이 - 23ms
class Solution(object):
    def swapPairs(self, head):
        list = ListNode()
        node = ListNode()
        list.next = node

        while head:
            if head.next:
                # swap
                node1 = ListNode(head.val)
                node2 = ListNode(head.next.val, node1)
                # 연결
                node.next = node2
                # 이동
                node = node.next.next
                head = head.next.next
            else:
                # 연결
                node.next = ListNode(head.val)
                # 이동
                head = head.next

        return list.next.next

# 교재 풀이 - 23ms
class Solution(object):
    def swapPairs(self, head):
        if head and head.next:
            next = head.next
            # 스왑 재귀 호출
            head.next = self.swapPairs(next.next)
            next.next = head
            return next
        return head
